# Waddles AI Backend

This section contains the backend of the 🐧 Waddles AI assistant. It is very much a work in progress with little to no input validation than what ever `langchain` (an absolutely amazing Python package btw) does natively. It is powered by Starling-LM, a model released by BAIR, and uses a RAG (retrieval-generated-augmentaion) structure to train off data.

## Development
The things below are meant for developers and people who are interested/want to contribute to the backend specifically.

### Dependencies

* 🐍 Python 3.9.X (<https://www.python.org/downloads/>)
* 🎤 Python Poetry (<https://python-poetry.org/>)
* 🐳 Docker (<https://www.docker.com/>)

### Getting Started

```bash
# Clone the repository
git clone https://github.com/ocf/ocf-llm.git

# cd into the backend part of the project
cd ocf-llm/llm-backend

# Build the docker image and run it
docker run -p 8000:8000 -it --rm $(docker build -q .)

# Success, hopefully 🤞🏼
```

## Contributing

Feel free to open a PR on anything you think can be fixed or improved.

## Important Citations

We use the Starling-LM model created by BAIR in November of 2023 as the core LLM in this project.

```LaTex
@misc{starling2023,
    title = {Starling-7B: Improving LLM Helpfulness & Harmlessness with RLAIF},
    author = {Zhu, Banghua and Frick, Evan and Wu, Tianhao and Zhu, Hanlin and Jiao, Jiantao},
    website = {https://starling.cs.berkeley.edu/}
    month = {November},
    year = {2023}
}
```

# Joe's (superior) note
1. Make sure to get Conda/miniconda
2. Setup through conda: create an environment with conda create --name [name]
3. "conda activiate [name]" in the llm directory
4. "conda install poetry"
5. ./start_service.sh, your server is on!
6. Open a separate terminal, cd into the llm backend directory, and run python3 server_test.py
7. Ask a question!