from langchain.chat_models import ChatOllama
from langchain.agents import initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain.agents.agent_types import AgentType
from knowledge_db.agents import create_agent
from knowledge_db.llm_config.prompt import get_prompt_template, message
from fastapi import FastAPI
from langserve import add_routes

# Load the model
model = ChatOllama(model="mixtral")
retrieverModel = ChatOllama(model="qwen:1.8b")

# Create the agent
tools = create_agent(
    retrieverModel, directory="./sources/", website="https://www.ocf.berkeley.edu"
)

# Initialize the agent with respective memory settings
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

# Create a conversation loop for people to try out:
contextInput = agent.invoke({"input": "What is your name and purpose?"})
print("Waddles: ", contextInput["output"])

# Sample code for a Model loop without server
while True:
    user_input = input("You: ")
    contextInput = agent.invoke({"input": user_input})
    print("Waddles: ", contextInput["output"])
    if user_input == "exit":
        break

# app = FastAPI(
#     title="Waddles on the Web",
#     version="0.1a",
#     description="Waddles using AI as an API",
# )

# # Add the API routes to invoke the LLM
# add_routes(
#     app,
#     agent,  # your model
#     path="/waddles",  # the path where your model will be served
#     enabled_endpoints=["invoke"],  # the endpoints to enable
# )

# # Main module to hose the API
# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="0.0.0.0", port=8000)
