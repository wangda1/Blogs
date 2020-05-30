---
title: numpy 之 维度变换
date: 2020-01-04 11:55:37
categories:
- MLDL
tags:
- MLDL
---

# numpy 之维度变换

## 维度变换

`numpy` 中关于维度变换函数有很多：`reshape`、`resize`、`swapaxes`、`flatten`、`transpose`等，下面有关于他们一一讲解。

## `resize()` 与 `reshape()` 函数

`resize()` 与 `reshape()` 功能相同，主要区别在于：

- `resize()` 会修改原数组
- `reshape()` 不会修改原数组

## `swapaxes()` 与 `transpose()` 函数

- `swapaxes()` 将原数组中的两个维度进行替换，并不改变原数组
- `transpose()` 可以进行多个维度的变换，类比于矩阵的转置功能，将原来`(i,j,k)`上的数据变换到`(i,k,j)`上来

## `flatten()` 函数

- `flatten()` 主要对数组进行降维，返回一维数组

## 参考

- https://blog.csdn.net/qq1483661204/article/details/70543952