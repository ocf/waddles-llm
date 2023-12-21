from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOllama
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma
from langchain.retrievers.multi_query import MultiQueryRetriever

from .parsers.document_loader import load_document
from .parsers.website_parser import crawl_website


def load(**kwargs):
    # Load the document
    documents = load_document(kwargs['directory'])

    # Crawl the website
    websites = crawl_website(kwargs['website'])
    
    #add all the documents and websites together
    return documents + websites

def splitter(document, chunk_size=1024, overlap_size=0):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size, overlap_size)
    print(document)
    child_chunks = text_splitter.split_documents(document)
    return splits

def store(splits):
    # Embed the text splits
    vectorstore = Chroma.from_documents(documents=splits, embeddings=OllamaEmbeddings())
    return vectorstore

def retrieve(llm, vectorstore):
    # Retrieve the most similar text splits
    retriever_from_llm = MultiQueryRetriever.from_llm(
        retriever=vectorstore.as_retriever(), llm=llm
    )
    return retriever_from_llm