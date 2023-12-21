from langchain.document_loaders import WebBaseLoader
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings

import os

links = ['https://www.google.com']
webpage = WebBaseLoader(web_paths=links).load()

fileList = []
for root, dirs, files in os.walk('./sources/'):
    for file in files:
        if file.lower().endswith(".pdf"):
            filename = os.path.join(root, file)
            pdf_loader = UnstructuredPDFLoader(filename)
            documents = pdf_loader.load()
            fileList.append(documents[0])


documents = fileList + webpage

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=0)
child_chunks = text_splitter.split_documents(documents)
print(len(child_chunks))


gguf_file = "./model/dolphin-2.2.1-mistral-7b.Q8_0.gguf"
model_file = "./model/Modelfile.dolphin.mistral"

# Load the model
# model = ChatOllama(gguf_file=gguf_file, model_file=model_file)
embeddings = OllamaEmbeddings(gguf_file=gguf_file, model_file=model_file)

vectorstore = Chroma.from_documents(documents=child_chunks, embedding=embeddings)