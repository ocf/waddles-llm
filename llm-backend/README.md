# Waddles AI Backend

This section contains the backend of the 🐧 Waddles AI assistant. It is very much a work in progress with little to no input validation than what ever `langchain` (an absolutely amazing Python package btw) does natively. It is powered by Qwen:14B and Qwen:1.8N, a model released by Alibaba Cloud, and uses a RAG (retrieval-generated-augmentaion) structure to train off data.

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

We use the Qwen 1.8 and 14 Billion flavors created by Alibaba Cloud in August of 2023 as the core LLM in this project.

```LaTex
@article{qwen,
  title={Qwen Technical Report},
  author={Jinze Bai and Shuai Bai and Yunfei Chu and Zeyu Cui and Kai Dang and Xiaodong Deng and Yang Fan and Wenbin Ge and Yu Han and Fei Huang and Binyuan Hui and Luo Ji and Mei Li and Junyang Lin and Runji Lin and Dayiheng Liu and Gao Liu and Chengqiang Lu and Keming Lu and Jianxin Ma and Rui Men and Xingzhang Ren and Xuancheng Ren and Chuanqi Tan and Sinan Tan and Jianhong Tu and Peng Wang and Shijie Wang and Wei Wang and Shengguang Wu and Benfeng Xu and Jin Xu and An Yang and Hao Yang and Jian Yang and Shusheng Yang and Yang Yao and Bowen Yu and Hongyi Yuan and Zheng Yuan and Jianwei Zhang and Xingxuan Zhang and Yichang Zhang and Zhenru Zhang and Chang Zhou and Jingren Zhou and Xiaohuan Zhou and Tianhang Zhu},
  journal={arXiv preprint arXiv:2309.16609},
  year={2023}
}
```
