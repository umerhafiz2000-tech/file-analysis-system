from chromadb.utils import embedding_functions
import chromadb

client = chromadb.Client(chromadb.config.Settings(persist_directory="./chroma_db"))
collection = client.get_collection("file_chunks")

# Retrieve all documents and metadata
all_docs = collection.get(include=["documents", "metadatas"])
documents = all_docs['documents']
metadatas = all_docs['metadatas']

for doc, meta in zip(documents, metadatas):
    print(f"File: {meta['file']} | Chunk ID: {meta['chunk_id']}")
    print(doc)
    print("-----")
