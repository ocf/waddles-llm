from langchain.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import DirectoryLoader
import os


def load_document(directory):
    """
    Load a document from a file.
    :param directory: A string containing the directory to load from (string)
    :return: A list of documents (list)
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


def load_directory(directory):
    loader = DirectoryLoader(directory, glob="*.*", use_multithreading=True)
    docs = loader.load()
    return docs