# Conda

```python
# 查看conda下的所有基本配置
conda config --show
# 删除conda的channel
conda config --remove channels 'default'
# 添加conda的channel
conda config --add channels https://xxx
# 配置清华PyPI镜像（如无法运行，将pip版本升级到>=10.0.0）
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
# 创建环境
conda create --name envname python=3.6
# 激活环境
conda activate envname
# 获取当前环境中已经安装的包
conda list
# 获取某个环境中安装的包
conda list -n envname
# 退出环境
conda deactivate
# 删除环境
conda remove -n envname --all
# 导出环境
conda env export > environment.yml
# 根据 .yml 文件创建环境
conda env create -f environment.yml 
```

## pip 源

```python
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt # pip 清华源
pip install -i http://pypi.douban.com/simple/ -r requirements.txt           # pip 豆瓣源
```

## 参考
- https://zhuanlan.zhihu.com/p/57287956
- 