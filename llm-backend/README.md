# Waddles AI Backend

This section contains the backend of the 🐧 Waddles AI assistant. It is very much a work in progress with little to no input validation than what ever `langchain` (an absolutely amazing Python package btw) does natively. It is powered by Llama3 -7b, a model released by Alibaba Cloud, and uses a RAG (retrieval-generated-augmentaion) structure to train off data.

## Development
The things below are meant for developers and people who are interested/want to contribute to the backend specifically.

### Dependencies

* 🐍 Python 3.9.X (<https://www.python.org/downloads/>)
* 🎤 Python Poetry (<https://python-poetry.org/>)
* 🐳 Docker (<https://www.docker.com/>)

### Getting Started Locally

```bash
# Clone the repository
git clone https://github.com/ocf/ocf-llm.git

# cd into the backend part of the project
cd ocf-llm/llm-backend

# Build the docker image and run it
docker run -p 8000:8000 -it --rm $(docker build -q .)

# Success, hopefully 🤞🏼
```

### Getting Started on HPC

```bash
# Clone the repository
git clone https://github.com/ocf/ocf-llm.git

# cd into the backend part of the project
cd ocf-llm/llm-backend

# Build the docker image
sudo build ./

# Run the docker image
sudo docker run -p 8000:8000 -it --rm --runtime=nvidia --gpus all [image container ID]

# Success, hopefully 🤞🏼
```


## Contributing

Feel free to open a PR on anything you think can be fixed or improved.

## Important Citations

We use the Qwen 1.8 and Mixtral8x7b created by Alibaba Cloud in August of 2023 and Mistral in December of 2023, respectively as the core LLMs in this project.

```LaTex
@article{qwen,
  title={Qwen Technical Report},
  author={Jinze Bai and Shuai Bai and Yunfei Chu and Zeyu Cui and Kai Dang and Xiaodong Deng and Yang Fan and Wenbin Ge and Yu Han and Fei Huang and Binyuan Hui and Luo Ji and Mei Li and Junyang Lin and Runji Lin and Dayiheng Liu and Gao Liu and Chengqiang Lu and Keming Lu and Jianxin Ma and Rui Men and Xingzhang Ren and Xuancheng Ren and Chuanqi Tan and Sinan Tan and Jianhong Tu and Peng Wang and Shijie Wang and Wei Wang and Shengguang Wu and Benfeng Xu and Jin Xu and An Yang and Hao Yang and Jian Yang and Shusheng Yang and Yang Yao and Bowen Yu and Hongyi Yuan and Zheng Yuan and Jianwei Zhang and Xingxuan Zhang and Yichang Zhang and Zhenru Zhang and Chang Zhou and Jingren Zhou and Xiaohuan Zhou and Tianhang Zhu},
  journal={arXiv preprint arXiv:2309.16609},
  year={2023}
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