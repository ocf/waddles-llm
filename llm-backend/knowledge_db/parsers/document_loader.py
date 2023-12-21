from langchain.document_loaders import UnstructuredPDFLoader
import os


def load_document(directory):
    """
    Load a document from a file.
    """
    fileList = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".pdf"):
                filename = os.path.join(root, file)
                pdf_loader = UnstructuredPDFLoader(filename)
                documents = pdf_loader.load()
                fileList.append(documents[0])
    return fileList
