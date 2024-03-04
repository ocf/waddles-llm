from flask import Flask, jsonify, request
import requests
from knowledge_db.llm_config.prompt import get_prompt_template

app = Flask(__name__)
# Im just testing (Joe)
@app.route('/api/data', methods=['POST'])
def handle_data():
    # Extract data from request
    data = request.json
    # Assuming you have a function `process_data` to handle the request data
    response_data = process_data(data)
    return jsonify(response_data)

def process_data(data):
    # Process your data here and return a response
    while True:
        userInput = data
        response = requests.post(
            "http://0.0.0.0:8000/waddles/invoke",
            json={"input": {"input": get_prompt_template(userInput)}},
        )
        print("Chat: " + response.json()["output"]["output"])

if __name__ == '__main__':
    app.run(debug=True, port=5000)