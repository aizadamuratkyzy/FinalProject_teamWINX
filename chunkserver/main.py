from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import Response
import os

from chunkserver.storage import save_chunk, read_chunk, delete_chunk, list_chunks

NODE_NAME = os.getenv("NODE_NAME", "chunkserver")

app = FastAPI(title=f"Mini-GFS {NODE_NAME}")


@app.get("/")
def root():
    return {
        "service": NODE_NAME,
        "message": "Chunkserver is running"
    }


@app.get("/health")
def health():
    return {
        "status": "ONLINE",
        "node": NODE_NAME
    }


@app.post("/store/{chunk_id}")
async def store_chunk(chunk_id: str, file: UploadFile = File(...)):
    data = await file.read()
    save_chunk(chunk_id, data)

    return {
        "message": "Chunk stored successfully",
        "node": NODE_NAME,
        "chunk_id": chunk_id,
        "size": len(data)
    }


@app.get("/read/{chunk_id}")
def get_chunk(chunk_id: str):
    try:
        data = read_chunk(chunk_id)
    except FileNotFoundError:
        raise HTTPException(
            status_code=404,
            detail="Chunk not found"
        )

    return Response(
        content=data,
        media_type="application/octet-stream"
    )


@app.delete("/delete/{chunk_id}")
def remove_chunk(chunk_id: str):
    deleted = delete_chunk(chunk_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Chunk not found"
        )

    return {
        "message": "Chunk deleted successfully",
        "node": NODE_NAME,
        "chunk_id": chunk_id
    }


@app.get("/chunks")
def chunks():
    return {
        "node": NODE_NAME,
        "chunks": list_chunks()
    }