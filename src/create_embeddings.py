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
def ask_question(question):

    db = load_vector_db()

    docs = db.similarity_search(question, k=3)

    print("\nRetrieved Context:\n")

    context = ""

    for i, doc in enumerate(docs):

        print(f"\n--- Source {i+1} ---\n")
        print(doc.page_content[:300])

        context += doc.page_content + "\n"


    prompt = f"""
You are answering questions based on the Swiggy Annual Report.

Use ONLY the context below.

If the answer is not present in the context, say:
"I cannot find this information in the Swiggy Annual Report."

Context:
{context}

Question: {question}

Answer in 2-3 sentences.
"""


    response = ollama.chat(
        model="phi3",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response["message"]["content"]

    print("\nAnswer:\n")
    print(answer)


# -------------------------
# Run Chatbot
# -------------------------
if __name__ == "__main__":

    while True:

        q = input("\nAsk a question about the Swiggy Annual Report: ")

        if q.lower() in ["exit", "quit"]:
            break

        ask_question(q)
