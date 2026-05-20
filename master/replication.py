"""
Replication logic.
Owner: [Name]

Responsible for copying chunks to several chunkservers.
"""

import requests
from master.config import CHUNK_SERVERS, REPLICATION_FACTOR


def get_alive_servers():
    alive = []

    for server in CHUNK_SERVERS:
        try:
            response = requests.get(f"{server}/health", timeout=2)
            if response.status_code == 200:
                alive.append(server)
        except requests.RequestException:
            pass

    return alive


def replicate_chunk(chunk_id: str, data: bytes):
    alive_servers = get_alive_servers()

    if not alive_servers:
        raise RuntimeError("No alive chunkservers available")

    selected_servers = alive_servers[:REPLICATION_FACTOR]
    successful_replicas = []

    for server in selected_servers:
        try:
            response = requests.post(
                f"{server}/store/{chunk_id}",
                files={"file": (chunk_id, data)},
                timeout=5,
            )

            if response.status_code == 200:
                successful_replicas.append(server)

        except requests.RequestException:
            continue

    if not successful_replicas:
        raise RuntimeError("Failed to store chunk on chunkservers")

    return successful_replicas


def read_from_replicas(chunk_id: str, replicas):
    for server in replicas:
        try:
            response = requests.get(f"{server}/read/{chunk_id}", timeout=5)
            if response.status_code == 200:
                return response.content
        except requests.RequestException:
            continue

    raise RuntimeError("All replicas are unavailable")
