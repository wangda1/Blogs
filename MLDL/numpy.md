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

### 2.2 `numpy.ndarray.flatten`

`ndarray.flatten(order='C')` 返回一个变换为1-D的副本

- paramenter: 'C'- 行；'F' - 列；'C'是默认的；

Example:

```python
>>> a = np.array([[1,2], [3,4]])
>>> a.flatten()
array([1, 2, 3, 4])
>>> a.flatten('F')
array([1, 3, 2, 4])
```

### 2.3 `numpy.argmax`

`numpy.argmax(a, axis=None, out=None)` 找出 ndarray 中最大值对应的索引

Parameters:

- axis: 默认是将 array flatten，取其最大值对应的索引，当指定 axis = 0时，每一列的最大值 index；当 axis = 1时，每一行的最大值 index

Examples：

```python
>>> a = np.arange(6).reshape(2,3) + 10
>>> a
array([[10, 11, 12],
       [13, 14, 15]])
>>> np.argmax(a)
5
>>> np.argmax(a, axis=0)
array([1, 1, 1])
>>> np.argmax(a, axis=1)
array([2, 2])
```