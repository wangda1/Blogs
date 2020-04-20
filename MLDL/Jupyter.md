---
title: Jupyter
date: 2019-11-30 18:47:58
categories:
- MLDL
tags:
- MLDL
---

# Jupyter 的使用

Jupyter 通篇内容有两种格式：Markdown 与 code，Markdown 模式下可以进行 Markdown 的编辑，code 模式下则可以进行代码的运行，这样有机地将代码和注释结合起来。

## Markdown 模式

`shift`+`enter` 快捷键是个很重要的快捷键，在 Markdown 模式下使用则可以进行预览和编辑的切换

## Code 模式

`shift`+`enter` 快捷键在 `code/md` 模式下可以进行代码/字体的创建和运行

## 快捷键

- `H`：查看所有快捷键。
- `S`：保存当前 Notebook 内容。
- `P`：调出 Notebook 命令栏。

### 对单元格（Cell）的操作

- `A/a`: 在当前单元格上方新建单元格 cell
- `B/b`：在当前单元格下方新建空白单元格。
- `M`：将单元格格式转换为 Markdown。
- `Y`：将单元格格式转换为 Code。
- `连续按 D+D/ d+d`：删除当前单元格。（慎用，推荐使用 X 剪切单元格代替，因为其可以起到删除效果，且删错了还可以粘贴回来）
- `Shift + Enter`：运行当前单元格内容。（当 Markdown 单元格处于编辑状态时，运行即可复原)
- `ESC` 在编辑模式（绿色）与非编辑模式（蓝色）下切换

## 服务器 Jupyter 搭建

1. 安装 jupyter notebook：`pip install jupyter`

2. 生成配置文件：`jupyter notebook --generate-config`

3. 设置 jupyter notebook 的密码：

```python
In [1]: from IPython.lib import passwd
In [2]: passwd()
Enter password: 
Verify password: 
```

4. 设置配置文件：`vim ~/.jupyter/jupyter_notebook_config.py`

```python
# 常见配置选项
c.NotebookApp.ip = '*' #所有绑定服务器的IP都能访问，若想只在特定ip访问，输入ip地址即可
c.NotebookApp.port = 6666 #将端口设置为自己喜欢的吧，默认是8888
c.NotebookApp.open_browser = False #我们并不想在服务器上直接打开Jupyter Notebook，所以设置成False
c.NotebookApp.notebook_dir = '/root/jupyter_projects' #这里是设置Jupyter的根目录，若不设置将默认root的根目录，不安全
c.NotebookApp.allow_root = True # 为了安全，Jupyter默认不允许以root权限启动jupyter 
```

5. 启动远程服务器：`jupyter notebook`

6. 打开浏览器访问对应的url，输入 token 即可。

当对应的 notebook token 忘记时，可以使用 `jupyter notebook list` 访问不同 notebook 的 token