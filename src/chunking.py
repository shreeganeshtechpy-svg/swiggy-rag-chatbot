from langchain_text_splitters import RecursiveCharacterTextSplitter
from load_pdf import load_pdf


def chunk_documents():

    documents = load_pdf()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=300,
        separators=["\n\n", "\n", " ", ""]
    )

    chunks = splitter.split_documents(documents)

    print("\nTotal Chunks Created:", len(chunks))

    print("\nSample Chunk Metadata:")
    print(chunks[0].metadata)

    print("\nSample Chunk Content:")
    print(chunks[0].page_content[:300])

    return chunks


if __name__ == "__main__":
    chunk_documents()
