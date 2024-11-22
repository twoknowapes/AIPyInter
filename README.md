###### Miniconda
* [Download Now](https://www.anaconda.com/download/success)
  conda update conda
  conda list
  conda env list
* 创建虚拟环境并安装软件包
conda create -n deepseek python=3.11 openai
conda remove -n env_name
conda remove -n env_name pkg_name
* 激活虚拟环境
conda activate deepseek
conda install pkg_name
conda uninstall pkg_name
conda deactivate
* 环境变量修改
export PATH=/path/to/python:$PATH
* 重要文档
[Python 3.13.0 documentation](https://docs.python.org/3.13/index.html)
