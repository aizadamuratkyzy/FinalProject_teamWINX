from pathlib import Path
import os

DATA_DIR = Path(os.getenv("DATA_DIR", "chunks_data"))
DATA_DIR.mkdir(parents=True, exist_ok=True)


def save_chunk(chunk_id: str, data: bytes):
    path = DATA_DIR / chunk_id
    path.write_bytes(data)


def read_chunk(chunk_id: str) -> bytes:
    path = DATA_DIR / chunk_id

    if not path.exists():
        raise FileNotFoundError("Chunk not found")

    return path.read_bytes()


def delete_chunk(chunk_id: str) -> bool:
    path = DATA_DIR / chunk_id

    if path.exists():
        path.unlink()
        return True

    return False


def list_chunks():
    chunks = []

    for item in DATA_DIR.iterdir():
        if item.is_file():
            chunks.append({
                "chunk_id": item.name,
                "size": item.stat().st_size
            })

    return chunks