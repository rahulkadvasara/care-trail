from qdrant.client import client
from qdrant.schema import COLLECTION_NAME
from embeddings.embedder import embed

def retrieve_memory(query, top_k=5):
    vector = embed(query)

    results = client.query_points(
        collection_name=COLLECTION_NAME,
        query=vector,
        limit=top_k
    )

    memories = []
    for r in results.points:
        memories.append({
            "text": r.payload["text"],
            "type": r.payload["type"],
            "date": r.payload["date"]
        })

    return memories
