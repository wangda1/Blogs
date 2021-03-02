---
title: Few-Shot Learning
date: 2021-03-02 15:32:00
categories:
- MLDL
tags:
- MLDL
---

# Few Shot Learning

Few Shot learning 是 meta-learning 的一种，"Learn to learn"

## Few Shot learning v.s. Supervised learning

Supervised Learning

- Test 集 model 没见过，但类别已知

    ![Supervised Learning](./few-shot-learning/supervised-learning.png)

Few Shot Learning

- Training Set 用于Pre-train Model
- Support Set 用于Low Resource Class
- Query Set 用于Test

    ![Few Shot Learning](./few-shot-learning/few-shot-learning.png)

    ![Few Shot Learning](./few-shot-learning/few-shot-learning2.png)

Support Set

- k-way: the support set has k classes
- n-shot: every class has n samples

## Few-Shot Learning 的基本思想

1. 基于 **High-Resources Classes** 部分的数据集训练 Pre-train Model
2. 基于 1 中的 model，得到 **Support Set** 中的 class embedding
3. 基于 1 中的 model，得到 **Query Set** 中的 class embedding
4. 计算 3 与 2 中每个 class 之间的 Similarity

    ![few-shot-learning-basic-idea](./few-shot-learning/few-shot-basic-idea.png)

## 常用的 CV Few-Shot Learning 数据集

- Omniglot 多种语言手写字母 few-shot 数据集

    ![Omniglot](./few-shot-learning/Dataset1.png)

    ![Omniglot](./few-shot-learning/Dataset1-1.png)

## Few-Shot 的常用 Model-- Siamese Network

计算两两直接的相似度
    ![siamese-network](./few-shot-learning/siamese-network1.png)

### 改进：Triplet Loss

计算 Positive Sample，Negative Sample 和 Anchor 之间的 相似度
    ![siamese-network](./few-shot-learning/siamese-network2.png)

## Pretrain + Fine-tuning 提升性能

![fine-tune-summary](./few-shot-learning/fine-tune-summary.png)

![fine-tune](./few-shot-learning/fine-tune.png)

### Trick1

使用 support set mean vector/centric vector 初始化 W，b设置为 0

![trick1](./few-shot-learning/fine-tune-trick1.png)

### Trick2

![trick2](./few-shot-learning/fine-tune-trick2.png)

### Trick3

![trcik3](./few-shot-learning/fine-tune-trick3.png)

参考：

- https://github.com/wangshusen/DeepLearning