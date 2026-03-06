import streamlit as st
from src.rag_pipeline import ask_question, load_vector_db


st.set_page_config(page_title="Swiggy RAG Chatbot")

st.title("Swiggy Annual Report Chatbot")

st.write("Ask questions about the Swiggy Annual Report.")


# -------------------------
# Cache Vector DB
# -------------------------
@st.cache_resource
def get_db():
    return load_vector_db()


db = get_db()


# -------------------------
# Suggested Questions
# -------------------------
st.markdown("### Suggested Questions")

examples = [
    "What services does Swiggy provide?",
    "How many cities does Swiggy operate in?",
    "How many delivery partners does Swiggy have?",
    "When did Swiggy launch food delivery?"
]

cols = st.columns(len(examples))

for i, q in enumerate(examples):
    if cols[i].button(q):
        st.session_state["selected_question"] = q


# -------------------------
# Chat History
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display chat history
for msg in st.session_state.messages:

    with st.chat_message("user"):
        st.write(msg["question"])

    with st.chat_message("assistant"):
        st.write(msg["answer"])
        st.caption("Sources: " + ", ".join([f"Page {p}" for p in msg["sources"]]))


# -------------------------
# Chat Input
# -------------------------
question = st.chat_input("Ask a question about the Swiggy report")

if "selected_question" in st.session_state:
    question = st.session_state.pop("selected_question")


if question:

    with st.chat_message("user"):
        st.write(question)

    with st.spinner("Searching the Swiggy Annual Report..."):

        result = ask_question(question, db)

    with st.chat_message("assistant"):
        st.write(result["answer"])
        st.caption("Sources: " + ", ".join([f"Page {p}" for p in result["sources"]]))

    st.session_state.messages.append({
        "question": question,
        "answer": result["answer"],
        "sources": result["sources"]
    })
