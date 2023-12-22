from langchain.chat_models import ChatOllama
from langchain.agents import initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain.agents.agent_types import AgentType
from knowledge_db.agents import create_agent
from knowledge_db.llm_config.system_message import message

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
    agent_kwargs={"system_message": message},
    handle_parsing_errors=True,
)


# Initialize the agent as shown in the previous examples
nullInput = agent.invoke({"input": message.content})

while True:
    # Get user input
    user_input = input("User: ")

    # Check if the user wants to exit the conversation
    if user_input.lower() == "exit":
        print("Exiting conversation.")
        break

    # Pass the user input to the agent and get the response
    response = agent.invoke({"input": user_input})

    # Print the response
    print(f"Chatbot: {response['output']}")
