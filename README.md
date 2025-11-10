<img width="562" height="297" alt="s4" src="https://github.com/user-attachments/assets/3e2f24e6-2ba9-4544-91fa-bd3f759239b9" /># 🧠 File Analysis & Embedding System

An end-to-end **document analysis and embedding system** that ingests files in multiple formats (`.docx`, `.txt`, `.pdf`), converts them into structured HTML and plain text, generates **embeddings** via a **local DeepSeek service**, stores them in **ChromaDB**, and retrieves the most relevant information through **high-performance similarity search**.

---

## 🚀 Features
- 📄 Multi-format document ingestion (.docx, .txt, .pdf)
- 🧩 Conversion to structured HTML and plain text
- ✂️ Custom text segmentation (splitter)
- 🧠 Embedding generation via **DeepSeek**
- 🗂️ Local vector storage in **ChromaDB**
- 🔍 Fast semantic retrieval
- 💻 Streamlit-based interactive UI (via `app.py`)

---

## 🏗️ Project Structure
DOC-EMBEDDINGS/
│
├── data/uploaded_files/ # Input files (not uploaded to GitHub)
├── embeddings/embedder.py # Embedding generation logic
├── ingest/ # Ingestion and text extraction
├── storage/ # Vector storage and retrieval
├── app.py # Streamlit app
├── chroma.py # ChromaDB integration
├── requirements.txt
└── .gitignore

## ⚙️ Installation
1. Clone the repository:
https://github.com/umerhafiz2000-tech/file-analysis-system.git

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Run the application:
streamlit run app.py

🧭 Workflow

Upload documents via the UI.

System converts to HTML → plain text.

Custom splitter breaks text into segments.

DeepSeek generates embeddings locally.

ChromaDB stores and retrieves relevant chunks for any query.


📸 Screenshots
<img width="553" height="380" alt="s1" src="https://github.com/user-attachments/assets/ab5ba9fd-13e6-4553-89e3-50202119bb0f" />
<img width="534" height="326" alt="s2" src="https://github.com/user-attachments/assets/6ca06360-0f58-400c-82c0-41355e9dc084" />
<img width="517" height="376" alt="s3" src="https://github.com/user-attachments/assets/3b4652f0-a630-4bb7-9628-25d3f8e5306f" />
<img width="562" height="297" alt="s4" src="https://github.com/user-attachments/assets/800504cd-94ec-4598-9b61-8b676489c010" />

🧰 Tech Stack

Python

Streamlit

For embedding (all-MiniLM-L6-v2 Model from SentenceTranformer)

ChromaDB

Langchain (optional)

PyMuPDF / docx2txt / BeautifulSoup



🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

Built with ❤️ by Hafiz Umer Mehmood (A python Developer)














































