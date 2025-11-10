import streamlit as st
from ingest.doc_loader import load_docx, load_pdf, load_txt
from ingest.text_splitter import split_text
from embeddings.embedder import embed_chunks, model
from storage.chroma_db import store_chunks, search

st.title("File Analysis System")

uploaded_file = st.file_uploader("Upload a document", type=["docx", "pdf", "txt"])
if uploaded_file:
    if uploaded_file.name.endswith(".docx"):
        text = load_docx(uploaded_file)
    elif uploaded_file.name.endswith(".pdf"):
        text = load_pdf(uploaded_file)
    else:
        text = load_txt(uploaded_file)

    chunks = split_text(text)
    st.subheader("Document Chunks")
    for i, chunk in enumerate(chunks):
        st.write(f"Chunk {i+1}:\n{chunk}\n")

    embeddings = embed_chunks(chunks)
    store_chunks(chunks, embeddings, uploaded_file.name)
    st.success("Chunks stored in ChromaDB!")

query = st.text_input("Search in documents")
if query:
    results = search(query)
    st.subheader("Search Results")
    for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
        st.write(f"File: {meta['file']} | Chunk ID: {meta['chunk_id']}")
        st.write(doc)
        st.write("---")
