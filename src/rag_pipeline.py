from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
import ollama


# -------------------------
# Load Vector Database
# -------------------------
def load_vector_db():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return db


# -------------------------
# Ask Question
# -------------------------
def ask_question(question, db):

    docs = db.similarity_search(question, k=3)

    context = ""
    sources = []

    for doc in docs:

        context += doc.page_content + "\n"

        if "page" in doc.metadata:
            sources.append(doc.metadata["page"])


    prompt = f"""
You are an AI assistant answering questions from the Swiggy Annual Report.

Use ONLY the context below to answer the question.

Context:
{context}

Question: {question}

Answer in 2-3 sentences.
"""

    response = ollama.chat(
        model="mistral",
        options={"num_predict": 120},
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response["message"]["content"]

    return {
        "answer": answer,
        "sources": list(set(sources))
    }
