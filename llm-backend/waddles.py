from langchain.chat_models import ChatOllama
from langchain.agents import initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain.agents.agent_types import AgentType
from knowledge_db.agents import create_agent
from knowledge_db.llm_config.prompt import get_prompt_template, message
from fastapi import FastAPI
from langserve import add_routes

# Load the model
model = ChatOllama(model="starling-lm")

# Create the agent
tools = create_agent(
    model, directory="./sources/", website="https://www.ocf.berkeley.edu"
)


agent = initialize_agent(
    tools,
    model,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=ConversationBufferMemory(memory_key="chat_history"),
    handle_parsing_errors=True,
)


print("[MODEL] Model Intialized")

# Initialize the agent as shown in the previous examples
contextInput = agent.invoke({"input": get_prompt_template(message.content)})

app = FastAPI(
    title="Waddles on the Web",
    version="0.1a",
    description="Waddles using AI as an API",
)

add_routes(
    app,
    agent,  # your model
    path="/waddles",  # the path where your model will be served
    enabled_endpoints=["invoke"],  # the endpoints to enable
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
