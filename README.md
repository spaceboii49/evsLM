# evsLM: Local RAG for Environmental Studies 🌿📚

**evsLM** is a privacy-focused, local Retrieval-Augmented Generation (RAG) system designed to assist students with Environmental Studies (EVS) coursework. By leveraging **Llama 3** running locally via **Ollama**, it provides accurate, context-aware answers derived specifically from course materials, eliminating hallucinations common in general-purpose LLMs.

## 🚀 Key Features

* **Local Inference:** Powered by **Llama 3** via Ollama, ensuring data privacy and offline capability.
* **Robust ETL Pipeline:** Integrates **PyTesseract** (OCR) and `pdf2image` to extract text from scanned PDFs and unstructured course notes.
* **Semantic Search:** Uses **ChromaDB** as the vector store with `mxbai-embed-large` embeddings for high-precision context retrieval.
* **Hallucination Control:** Engineered strict system prompts to constrain the model's answers solely to the provided context.

## 🛠️ Tech Stack

* **LLM Engine:** Ollama (Llama 3)
* **Orchestration:** LangChain
* **Vector Database:** ChromaDB
* **Embeddings:** `mxbai-embed-large`
* **Data Processing:** PyTesseract, PDF2Image, RecursiveCharacterTextSplitter
* **Language:** Python 3.10+

## ⚙️ Installation

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/yourusername/evsLM.git](https://github.com/yourusername/evsLM.git)
    cd evsLM
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
    *Note: Ensure you have Tesseract-OCR installed on your system (e.g., `sudo apt install tesseract-ocr` or `brew install tesseract`).*

3.  **Setup Ollama**
    * Download and install [Ollama](https://ollama.com/).
    * Pull the required models:
        ```bash
        ollama pull llama3
        ollama pull mxbai-embed-large
        ```

## 🏃‍♂️ Usage

1.  **Ingest Data**
    Place your PDF course materials in the `data/` directory and run the ingestion script to populate the vector database:
    ```bash
    python ingest.py
    ```

2.  **Run the Query Interface**
    Start the interactive CLI or web interface (if configured):
    ```bash
    python main.py
    ```

## 🧠 Architecture

1.  **Document Loading:** PDFs are converted to images and processed via OCR.
2.  **Chunking:** Text is split into 1000-character chunks with 200-character overlap.
3.  **Embedding:** Chunks are embedded and stored in a persistent ChromaDB instance.
4.  **Retrieval:** User queries fetch top-k relevant chunks.
5.  **Generation:** Llama 3 synthesizes an answer using *only* the retrieved context.