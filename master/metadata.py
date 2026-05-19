"""
Metadata storage for Mini-GFS.
"""

from typing import Dict, List
from datetime import datetime


class MetadataStore:
    def __init__(self):
        self.files: Dict[str, Dict] = {}

    def save_file(self, filename: str, chunk_id: str, replicas: List[str], size: int):
        self.files[filename] = {
            "filename": filename,
            "chunk_id": chunk_id,
            "replicas": replicas,
            "size": size,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

    def get_file(self, filename: str):
        return self.files.get(filename)

    def list_files(self):
        return list(self.files.values())

    def delete_file(self, filename: str):
        if filename in self.files:
            del self.files[filename]
            return True
        return False
