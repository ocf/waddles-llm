from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma
from langchain.retrievers.multi_query import MultiQueryRetriever
import os
import pickle
from knowledge_db.parsers.document_loader import load_document
from knowledge_db.parsers.website_parser import crawl_website


def load_and_split(**kwargs):
    # Load the document
    documents = load_document(kwargs["directory"])

    # Crawl the website
    websites = crawl_website(kwargs["website"])

    # add all the documents and websites together
    sources = documents + websites

    # Split the documents into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=50)
    child_chunks = text_splitter.split_documents(sources)
    print("Split documents into chunks.")
    return child_chunks


def store(splits):
    # Embed the text splits
    print(len(splits))
    vectorstore = Chroma.from_documents(
        documents=splits, embedding=OllamaEmbeddings(model="starling-lm")
    )
    print('Vectorstore generated.')
    return vectorstore


def retrieve(llm, vectorstore):
    # Retrieve the most similar text splits
    retriever_from_llm = MultiQueryRetriever.from_llm(
        retriever=vectorstore.as_retriever(), llm=llm
    )
    return retriever_from_llm
