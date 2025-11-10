import chromadb
from embeddings.embedder import model
import uuid

# Use persistent directory so your database survives restarts
persist_dir = "./chroma_db"

client = chromadb.Client(chromadb.config.Settings(
    persist_directory=persist_dir
))

collection_name = "file_chunks"

# Check if collection exists; create if it doesn't
collections = [c.name for c in client.list_collections()]
if collection_name in collections:
    collection = client.get_collection(collection_name)
else:
    collection = client.create_collection(collection_name)

def store_chunks(chunks, embeddings, filename):
    for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
        unique_id = f"{filename}_chunk_{i}_{uuid.uuid4()}"  # unique ID for each chunk
        collection.add(
            ids=[unique_id],
            documents=[chunk],
            metadatas=[{"file": filename, "chunk_id": i}],
            embeddings=[emb]
        )

def search(query, top_k=5):
    emb = model.encode([query])
    results = collection.query(
        query_embeddings=emb,
        n_results=top_k
    )
    return results
