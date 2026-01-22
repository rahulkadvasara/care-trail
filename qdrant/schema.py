from qdrant_client.models import VectorParams, Distance

COLLECTION_NAME = "patient_memory"
VECTOR_SIZE = 384  # all-MiniLM-L6-v2

VECTOR_CONFIG = VectorParams(
    size=VECTOR_SIZE,
    distance=Distance.COSINE
)
