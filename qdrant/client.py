from qdrant_client import QdrantClient
from qdrant.schema import COLLECTION_NAME, VECTOR_CONFIG
import os

client = QdrantClient(url=os.getenv("QDRANT_URL"))

def init_collection():
    client.recreate_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VECTOR_CONFIG
    )
