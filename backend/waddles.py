from langchain.chat_models import ChatOllama
from langchain.agents.agent_toolkits import create_conversational_retrieval_agent

from knowledge_db.agents import create_agent

gguf_file = "./model/dolphin-2.2.1-mistral-7b.Q8_0.gguf"
model_file = "./model/Modelfile.dolphin.mistral"

# Load the model
model = ChatOllama(gguf_file=gguf_file, model_file=model_file)

# Create the agent
tools = create_agent(model, directory="./sources/", website="https://www.ocf.berkeley.edu")
# Create the conversational retrieval agent
agent = create_conversational_retrieval_agent(model, tools)


