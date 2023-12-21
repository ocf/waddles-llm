from langchain.chat_models import ChatOllama
from langchain.agents.conversational_chat.base import ConversationalChatAgent
from langchain.agents import AgentExecutor

from knowledge_db.agents import create_agent
from knowledge_db.llm_config.system_message import message

# Load the model
model = ChatOllama(model="starling-lm")

# Create the agent
tools = create_agent(
    model, directory="./sources/", website="https://www.ocf.berkeley.edu"
)


# Create the conversational retrieval agent
prompt = ConversationalChatAgent.create_prompt(
    system_message=message,
    tools=tools,
)

agent = ConversationalChatAgent(llm=model, tools=tools, prompt=prompt)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    return_intermediate_steps=True,
)

# Run the agent
result = agent_executor({"input": "hi, im Aditya, and I wanted to ask how to print at the OCF."})
print(result)



