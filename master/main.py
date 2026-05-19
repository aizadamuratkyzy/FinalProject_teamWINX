"""
Master Server entry point.
Responsible for metadata and coordination.
"""

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import Response
import uuid

from master.metadata import MetadataStore
from master.replication import replicate_chunk, read_from_replicas, get_alive_servers

app = FastAPI(title="Mini-GFS Master Server")

metadata = MetadataStore()


@app.get("/")
def root():
    return {
        "service": "Mini-GFS Master Server",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "ONLINE",
        "service": "master"
    }


@app.get("/nodes")
def nodes():
    return {
        "alive_chunkservers": get_alive_servers()
    }


@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    data = await file.read()
    chunk_id = str(uuid.uuid4())

    try:
        replicas = replicate_chunk(chunk_id, data)

        metadata.save_file(
            filename=file.filename,
            chunk_id=chunk_id,
            replicas=replicas,
            size=len(data),
        )

        return {
            "message": "File uploaded successfully",
            "filename": file.filename,
            "chunk_id": chunk_id,
            "replicas": replicas,
            "size": len(data),
        }

    except RuntimeError as error:
        raise HTTPException(status_code=500, detail=str(error))


@app.get("/download/{filename}")
def download_file(filename: str):
    file_info = metadata.get_file(filename)

    if not file_info:
        raise HTTPException(status_code=404, detail="File not found")

    try:
        data = read_from_replicas(
            chunk_id=file_info["chunk_id"],
            replicas=file_info["replicas"],
        )

        return Response(
            content=data,
            media_type="application/octet-stream",
            headers={
                "Content-Disposition": f"attachment; filename={filename}"
            },
        )

    except RuntimeError as error:
        raise HTTPException(status_code=503, detail=str(error))


@app.get("/files")
def list_files():
    return {
        "files": metadata.list_files()
    }


@app.delete("/files/{filename}")
def delete_file(filename: str):
    deleted = metadata.delete_file(filename)

    if not deleted:
        raise HTTPException(status_code=404, detail="File not found")

    return {
        "message": f"{filename} deleted from metadata"
    }
