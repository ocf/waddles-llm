from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OllamaEmbeddings
from langchain.vectorstores import Chroma
from langchain.retrievers.multi_query import MultiQueryRetriever
import os
from knowledge_db.parsers.document_loader import load_directory
from knowledge_db.parsers.website_parser import crawl_website
from tqdm import tqdm


def load_and_split(retrain=False, **kwargs):
    """
    A method to load the data from documents annd websites and return the chunks
    :param retrain: A boolean indicating whether to retrain on data or use cache (boolean)
    :param kwargs: A dictionary containing the directory and website to load from (dict)
    :return: A list of text splits (list)
    """
    db_dir = os.path.join(os.getcwd(), "knowledge_db/", "database/")
    # check if a directory is empty
    if not os.listdir(db_dir) or retrain:
        # Load the document
        print("[LOAD] Loading documents")
        documents = load_directory(kwargs["directory"])
        print("[LOAD] Loaded " + str(len(documents)) + " documents.")

        # Crawl the website
        print("[LOAD] Crawling websites")
        websites = crawl_website(kwargs["website"])
        print("[LOAD] Crawled " + str(len(websites)) + " websites.")

        # add all the documents and websites together
        sources = documents + websites

        # Split the documents into chunks
        print("[SPLIT] Splitting documents")
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1024, chunk_overlap=64
        )
        child_chunks = text_splitter.split_documents(sources)
        print("[SPLIT] Split documents into " + str(len(child_chunks)) + " chunks.")
    else:
        print("[SPLIT] Not splitting as vectorstore pre-generated.")
        child_chunks = None
    return child_chunks


def store(splits, retrain=False):
    """
    A method to create a vector database from a list of text splits
    :param splits: A list of text splits (list)
    :param retrain: A boolean indicating whether to retrain on data or use cache (boolean)
    :return: A vectorstore (vectorstore)
    """
    # Embed the text splits
    db_dir = os.path.join(os.getcwd(), "knowledge_db/", "database/")
    vectorstore = None
    # check if a directory is empty
    if not os.listdir(db_dir) or retrain:
        if len(splits) < 50:
            vectorstore = Chroma.from_documents(
                documents=splits,
                embedding=OllamaEmbeddings(model="mixtral"),
                persist_directory=db_dir,
            )
            print("[V_DB] Vectorstore of size less than 100 generated.")
            return vectorstore
        else:
            BATCH_SIZE = 20
            # Get the first 50 splits
            first_batch = splits[:BATCH_SIZE]
            vectorstore = Chroma.from_documents(
                documents=first_batch,
                embedding=OllamaEmbeddings(model="mixtral"),
                persist_directory=db_dir,
            )
            # remove the first 50 splits
            splits = splits[BATCH_SIZE:]
            for i in tqdm(range(0, len(splits), BATCH_SIZE)):
                # Get the next 50 splits
                next_batch = splits[i : i + BATCH_SIZE]
                vectorstore.add_documents(
                    documents=next_batch,
                    embedding=OllamaEmbeddings(model="mixtral"),
                )
            print("[V_DB] Vectorstore generated.")
    else:
        vectorstore = Chroma(
            persist_directory=db_dir,
            embedding_function=OllamaEmbeddings(model="mixtral"),
        )
        print("[V_DB] Vectorstore loaded from disc.")
    return vectorstore


def retrieve(llm, vectorstore):
    """
    A method to retrieve the most similar text splits
    :param llm: A language model (llm)
    :param vectorstore: A vectorstore (vectorstore)
    :return: A retriever (retriever)
    """
    # Retrieve the most similar text splits
    retriever_from_llm = MultiQueryRetriever.from_llm(
        retriever=vectorstore.as_retriever(), llm=llm
    )
    return retriever_from_llm
