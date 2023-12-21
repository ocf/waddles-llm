from langchain.agents.agent_toolkits import create_retriever_tool
from .aggregator import load, splitter, store, retrieve


def create_agent(llm, **kwargs):
    # Load the document
    data = load(directory=kwargs['directory'], website=kwargs['website'])
    
    # Split the document
    splits = splitter(data)

    # Embed the text splits
    vectorstore = store(splits)

    # Retrieve the most similar text splits
    retriever = retrieve(llm, vectorstore)

    tool = create_retriever_tool(
        retriever,
        "search OCF account and printing issues",
        "Searches and returns documents regarding technical issues with the computers in the OCF lab",
    )
    return [tool]