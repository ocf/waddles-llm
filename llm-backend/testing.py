from langchain.document_loaders import WebBaseLoader
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings

import os

links = ["https://www.ocf.berkeley.edu"]
webpage = WebBaseLoader(web_paths=links).load()

fileList = []
for root, dirs, files in os.walk("./sources/"):
    for file in files:
        if file.lower().endswith(".pdf"):
            filename = os.path.join(root, file)
            pdf_loader = UnstructuredPDFLoader(filename)
            documents = pdf_loader.load()
            fileList.append(documents[0])


documents = fileList + webpage
print(documents)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=0)
child_chunks = text_splitter.split_documents(documents)
print(len(child_chunks))


# Load the model

vectorstore = Chroma.from_documents(
    documents=child_chunks, embedding=OllamaEmbeddings(model="starling-lm")
)
print(vectorstore)
