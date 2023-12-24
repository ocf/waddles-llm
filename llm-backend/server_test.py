import requests
from knowledge_db.llm_config.prompt import get_prompt_template


# Quirk: Input needs to be given as {"input": {"input": whatever the fuck}}
# I don't know why it needs to be nested but my guess is first is for the API, second is for model

while True:
    userInput = input("User: ")
    if userInput == "exit":
        break
    response = requests.post(
        "http://0.0.0.0:8000/waddles/invoke",
        json={"input": {"input": get_prompt_template(userInput)}},
    )
    print("Chat: " + response.json()["output"]["output"])
