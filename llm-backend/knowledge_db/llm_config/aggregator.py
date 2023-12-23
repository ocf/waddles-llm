from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma
from langchain.retrievers.multi_query import MultiQueryRetriever
import os
from knowledge_db.parsers.document_loader import load_document
from knowledge_db.parsers.website_parser import crawl_website


def load_and_split(retrain=False, **kwargs):
    db_dir = os.path.join(os.getcwd(), "knowledge_db/", "database/")
    # check if a directory is empty
    if not os.listdir(db_dir) or retrain:
        # Load the document
        documents = load_document(kwargs["directory"])

        # Crawl the website
        websites = crawl_website(kwargs["website"])

        # add all the documents and websites together
        sources = documents + websites

        # Split the documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1024, chunk_overlap=50)
        child_chunks = text_splitter.split_documents(sources)
        print("[SPLIT] Split documents into " + str(len(child_chunks)) + " chunks.")
    else:
        print("[SPLIT] Not splitting as vectorstore pre-generated.")
        child_chunks = None
    return child_chunks


def store(splits, retrain=False):
    # Embed the text splits
    db_dir = os.path.join(os.getcwd(), "knowledge_db/", "database/")
    vectorstore = None
    # check if a directory is empty
    if not os.listdir(db_dir) or retrain:
        vectorstore = Chroma.from_documents(
            documents=splits,
            embedding=OllamaEmbeddings(model="starling-lm"),
            persist_directory=db_dir,
        )
        print("[V_DB] Vectorstore generated.")
    else:
        vectorstore = Chroma(
            persist_directory=db_dir,
            embedding_function=OllamaEmbeddings(model="starling-lm"),
        )
        print("[V_DB] Vectorstore loaded from disc.")
    return vectorstore


def retrieve(llm, vectorstore):
    # Retrieve the most similar text splits
    retriever_from_llm = MultiQueryRetriever.from_llm(
        retriever=vectorstore.as_retriever(), llm=llm
    )
    return retriever_from_llm
