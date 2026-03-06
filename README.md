# Swiggy Annual Report RAG Chatbot

This project implements a **Retrieval-Augmented Generation (RAG)** chatbot that answers questions based on the Swiggy Annual Report.

The chatbot retrieves relevant sections from the report using a **vector database (FAISS)** and generates grounded answers using a **local Large Language Model (Mistral via Ollama)**.

---

## Features

* Retrieval-Augmented Generation (RAG)
* Semantic search using FAISS
* SentenceTransformer embeddings
* Local LLM using Ollama
* Source citations from the document
* Streamlit chat interface
* Suggested questions for quick testing

---

## Tech Stack

* Python
* LangChain
* FAISS
* SentenceTransformers
* Ollama (Mistral LLM)
* Streamlit

---

## Project Architecture

<img width="1024" height="1536" alt="image" src="https://github.com/user-attachments/assets/3253e012-c814-44ae-ac11-4e229d109dac" />

---

## Installation

### 1. Clone the repository

git clone https://github.com/shreeganeshtechpy-svg/swiggy-rag-chatbot.git
cd swiggy-rag-chatbot

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Ollama

Download from: [https://ollama.com/download](https://ollama.com/download)

Then pull the model:

```bash
ollama pull mistral
```

### 4. Run the application

```bash
streamlit run app.py
```

The chatbot will open in your browser at:

[http://localhost:8501](http://localhost:8501)

---

## Example Questions

* What services does Swiggy provide?
* How many cities does Swiggy operate in?
* How many delivery partners does Swiggy have?
* When did Swiggy launch food delivery?

---

## Author

Shreeganesh Vishwakarma
