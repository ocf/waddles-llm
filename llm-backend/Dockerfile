FROM nvidia/cuda:12.3.1-devel-ubuntu22.04

WORKDIR /app

COPY . /app/

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    git \
    curl \
    wget \
    software-properties-common

# Add python3.9 repository
RUN apt-add-repository -y ppa:deadsnakes/ppa

# Add python
RUN apt-get update && apt-get install -y \
    python3.9 \
    python3.9-distutils

# Install poetry
RUN cd .. && curl -sSL https://install.python-poetry.org | python3.9 - && curl https://ollama.ai/install.sh | sh && cd app

ENV PATH="/root/.local/bin:$PATH"


# Install dependencies
RUN poetry install --no-root

# Run the app
CMD ["poetry", "run", "python3.9", "waddles.py"]