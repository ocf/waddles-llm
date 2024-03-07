from langchain.chat_models import ChatOllama
from langchain.agents import initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain.agents.agent_types import AgentType
from knowledge_db.agents import create_agent
from knowledge_db.llm_config.prompt import get_prompt_template, message, LLM
from fastapi import FastAPI
from langserve import add_routes
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Load the model
print("[MODEL] Loading Models")
model = ChatOllama(model=LLM)
retrieverModel = ChatOllama(model=LLM)
print("[MODEL] Models Loaded")

# Create the agent
tools = create_agent(
    retrieverModel, directory="./sources/docs", website="https://www.ocf.berkeley.edu"
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

# Sample code for a Model loop without server
# while True:
#     user_input = input("You: ")
#     contextInput = agent.invoke({"input": user_input})
#     print("Waddles: ", contextInput["output"])
#     if user_input == "exit":
#         break

# Initialize the agent as shown in the previous examples
# contextInput = agent.invoke({"input": get_prompt_template(message.content)})

# # Create a conversation loop for people to try out:
# contextInput = agent.invoke({"input": "What is your name and purpose?"})
# print("Waddles: ", contextInput["output"])

app = FastAPI(
    title="Waddles on the Web",
    version="0.1a",
    description="Waddles using AI as an API",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],  # Adjust the port if your React app runs on a different one
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Add the API routes to invoke the LLM
add_routes(
    app,
    agent,  # your model
    path="/waddles",  # the path where your model will be served
    enabled_endpoints=["invoke"],  # the endpoints to enable
)

# Main module to hose the API
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
