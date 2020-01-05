---
title: Ch6_classify
date: 2020-01-05 16:12:09
categories:
- MLDL
- AndrewNG机器学习
tags:
- MLDL
- AndrewNG机器学习
---

# Classifier 分类器

- Linear Regression
- Logistic Regression ！！！

## 1. 分类问题

**以下考虑的均为二分类问题：`y=0/y=1`**

分类问题的引入，由最初的线性函数（`linear function`），得到的值往往存在于 0 与 1 之外，并且线性函数得出的值往往会受到样本的扰动比较大，因此考虑将线性函数的值再经过映射到0-1的空间内。

![classifier](Ch6_classify/Andrew_ch06_1.png)

## 2. 假设（Hypothesis）

![hypothesis](Ch6_classify/Andrew_ch06_2.png)

![hypothesis](Ch6_classify/Andrew_Ch06_3.png)

## 3. 决策界限（Decision Boundary）

![decision_boundary](Ch6_classify/Andrew_Ch06_4.png)

![decision_boundary](Ch6_classify/Andrew_Ch06_5.png)

## 4. 代价函数（Cost Function）

![cost_function](Ch6_classify/Andrew_Ch06_6.png)

在线性回归（`Linear Regression`）里，使用平方差函数作为损失函数是可以的，但是在逻辑回归（`Logistic Regression`）里，使用平方差函数作为损失函数，该函数并不是凸函数（`non-convex function`），就不能使用梯度下降 `gradient descent` 找到全局最小值（`global minimum`）

![cost_funciton](Ch6_classify/Andrew_Ch06_7.png)

## 5. 简化代价函数与梯度下降

对代价函数进行简化，写成一个整体，则成为下面的函数：

![gradient_descent](Ch6_classify/Andrew_Ch06_8.png)

对代价函数进行求导：

![gradient_descent](Ch6_classify/Andrew_Ch06_9.png)

## 6. 高级优化

梯度下降是一个比较常用算法，但由于其在实际的比较大的问题中，速度较慢，因此往往使用比较快速的方法：

- Conjugate Descent （共轭梯度）
- BFGS
- L-BFGS

这些算法的优点是不用手工设置学习率`α`，它们算法的内部往往包含一个内循环来自动设置这些学习率，并且每一步的学习率也比较不同，收敛速度较快。

![gradient_descent](Ch6_classify/Andrew_Ch06_10.png)

Andrew NG 使用 Octave 演示的梯度下降的例子:

![gradient_descent](Ch6_classify/Andrew_Ch06_11.png)

## 7. 多元分类（Multi-Class Classification）

`one-vs-all` 的方法：思想很简单，即把多元分类的问题看成多个二元分类问题，来选取置信度最高的那一个；

![one-vs-all](Ch6_classify/Andrew_Ch06_12.png)

![one-vs-all](Ch6_classify/Andrew_Ch06_13.png)

