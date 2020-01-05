---
title: IO
date: 2019-12-13 14:46:17
categories:
- Python
tags:
- Python
---

# python中的IO

## 文件读取

```python
with open('file.txt', 'r') as f:
    content = f.read()  # 一次性读取所有内容
    f.readline()        # 逐行读取内容
    f.readlines()       # 一次进行逐行读取,返回 list
```

## 文件操作 `os.path`

```python
def list_files():
    news_file_list = []
    for d in os.listdir(data_dir_path):
        if os.path.isdir(os.path.join(data_dir_path, d)):
            news_file_list.append(os.path.join(data_dir_path, d, 'news.txt'))
    return news_file_list

os.path.dirname()   # 返回所在的文件夹名称
os.path.exists()    # 判断路径是否存在
os.path.abspath()   # 返回绝对路径
os.path.isdir()     # 判断是否为目录，注：要输入绝对路径
os.path.isfile()    # 判断是否为文件
```