from langchain_community.document_loaders import PyPDFLoader

def load_pdf():

    file_path = "data/swiggy_report.pdf"

    loader = PyPDFLoader(file_path)

    documents = loader.load()

    print("Total Pages Loaded:", len(documents))

    print("\nFirst Page Preview:\n")
    print(documents[0].page_content[:500])

    return documents


if __name__ == "__main__":
    load_pdf()