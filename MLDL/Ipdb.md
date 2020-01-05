---
title: Ipdb
date: 2020-01-02 12:05:05
categories:
- MLDL
tags:
- MLDL
---

# IPDB (Ipython Debugger)

IPDB和GDB类似，是一款集成了`Ipython`的Python代码命令行调试工具。

## 1. 集成到源代码中使用

```python
import ipdb

x = 10
ipdb.set_trace() # 执行到此，程序停止，展开Ipython环境
y = 20
```

## 2. 交互式使用

`python -m ipdb code.py`