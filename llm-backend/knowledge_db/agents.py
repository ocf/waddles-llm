from langchain.agents.agent_toolkits import create_retriever_tool
from .llm_config.aggregator import load_and_split, store, retrieve


def create_agent(llm, **kwargs):
    # Load the document
    data_splits = load_and_split(
        directory=kwargs["directory"], website=kwargs["website"]
    )

    # Embed the text splits
    vectorstore = store(data_splits)

    # Retrieve the most similar text splits
    retriever = retrieve(llm, vectorstore)

    tool = create_retriever_tool(
        retriever,
        "search OCF and Open Computing Facility account and printing issues",
        "OCF related matters",
    )
    return [tool]
