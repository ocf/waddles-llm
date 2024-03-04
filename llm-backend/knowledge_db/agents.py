from langchain.agents.agent_toolkits import create_retriever_tool
from .llm_config.aggregator import load_and_split, store, retrieve


def create_agent(llm, **kwargs):
    """
    A method to create an agent
    :param llm: A language model (llm)
    :param kwargs: A dictionary containing the agent configuration (dict)
    :return: tool for LLM
    """
    # Load the document
    print("[AGENT] Loading and Splitting Data")
    data_splits = load_and_split(
        directory=kwargs["directory"], website=kwargs["website"]
    )
    print("[AGENT] Data Loaded and Split")

    # Embed the text splits
    print("[AGENT] Creating Vectorstore")
    vectorstore = store(data_splits)
    print("[AGENT] Vectorstore Created")

    # Retrieve the most similar text splits
    retriever = retrieve(llm, vectorstore)

    # Create the tool
    tool = create_retriever_tool(
        retriever,
        "search OCF and Open Computing Facility account and printing issues",
        "OCF related matters",
    )
    return [tool]
