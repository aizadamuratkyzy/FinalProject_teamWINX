"""
Configuration file for Master Server.
"""

CHUNK_SERVERS = [
    "http://chunkserver1:8001",
    "http://chunkserver2:8001",
    "http://chunkserver3:8001",
]

REPLICATION_FACTOR = 3
