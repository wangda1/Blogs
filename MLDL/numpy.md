---
title: numpy
date: 2020-01-04 11:55:37
categories:
- MLDL
tags:
- MLDL
---

# Numpy 学习

```python
import numpy as np
```

## 1. 函数

### 1.1 生成序列

- `range()` 可生成一定 step 的序列，但只能整数
- `arange()` 可生成一定 step 的序列，可以是浮点数

## Tricks

## 2. `np.eye()` 与 `np.identity()`

`numpy.eye(N, M=None, k=0, dtype=<class 'float'>, order='C')[source]`

可以生成2-D的对角矩阵（不一定对角），零可以被设置放置在任意地方；

### 2.1 Example

```python
>>> np.eye(2, dtype=int)
array([[1, 0],
       [0, 1]])
>>> np.eye(3, k=1)
array([[0.,  1.,  0.],
       [0.,  0.,  1.],
       [0.,  0.,  0.]])
# 常用的可以对数组进行 one-hot 编码
>>> np.eye(3)[[1,0,2,1]]
array([[0., 1., 0.],
       [1., 0., 0.],
       [0., 0., 1.],
       [0., 1., 0.]])
```

`np.identity(n, dtype=None)`

仅能生成对角方阵

```python
>>> np.identity(3)
array([[1., 0., 0.],
       [0., 1., 0.],
       [0., 0., 1.]])
```