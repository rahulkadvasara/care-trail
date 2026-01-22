from qdrant.client import client
from qdrant.schema import COLLECTION_NAME
from embeddings.embedder import embed
from utils.chunker import chunk_text
import uuid
import datetime

def ingest_text(text, record_type="note"):
    chunks = chunk_text(text)

    points = []
    for chunk in chunks:
        points.append({
            "id": str(uuid.uuid4()),
            "vector": embed(chunk),
            "payload": {
                "text": chunk,
                "type": record_type,
                "date": str(datetime.date.today())
            }
        })

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points
    )
