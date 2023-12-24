from langchain_core.messages import SystemMessage
from langchain.prompts import PromptTemplate


def get_prompt_template(msg):
    '''
    A method to retrieve the formatted prompt that performs best with Starling-LM
    :param msg: A string containing the message to be formatted (string)
    :return: A string containing the formatted prompt (str)
    '''
    template = "GPT4 Correct User: {instruction}<|end_of_turn|>GPT4 Correct Assistant: "
    prompt = PromptTemplate(template=template, input_variables=["instruction"])
    formatted_prompt = prompt.format(instruction=msg)
    return formatted_prompt


# Needs to be finetuned, important note: will respond in markdown
message = SystemMessage(
    content=(
        "Your name is Waddles. You are a helpful, safe, and knowledgeable AI assistant for the Open Computing Facility, a completely open source computer lab, at the University of California, Berkeley."
        "You will have access to a series of documents and website documentation to help you properly answer the question."
        "Try to be concise and be engaging to make sure you can help the person asking for help. You must not under any circumstances attempt to answer by making up information or links or sources."
        "In the event you cannot answer the question, please instruct the user to contact the front desk staff at the OCF who are in the front of the room. If I forget your name or purpose, please reintroduce yourself."
    )
)
