---
title: word_embedding
date: 2020-01-04 22:53:51
categories:
- NLP
tags:
- NLP
---

# Word Embedding

## 1-of-N Encoding

## 2. Word Embeddding

- `unsupervised learning`
- `dimension reduction` wword embedding 的维度要比 1-of-N encoding 低很多

## 3. Training 的两种方法

### 3.1 Count-based 

通过计算 co-occurence frequency，并计算两个 vector 的 dot product，使其与 frequency 相似

![word_embedding](word_embedding/word_emb_1.png)

### 3.2 Count-based 的代表

#### 3.2.1 LSA(Latent Semantic Analysis)

#### 3.2.2 word2vec

#### 3.2.3 GloVe(Global Vectors for word representation)

*参考：http://www.fanyeong.com/2018/02/19/glove-in-detail/*

> 它是一个基于 `全局词频统计` 的词表征（word representation）工具，它可以把一个单词表达成一个由实数组成的向量，这些向量捕捉到了单词之间的语义特性，比如：相似性（similarity）、类比性（analogy）等。我们通过对向量的运算，比如欧式距离或cosine相似度，可以计算出两个单词之间的语义相似性。
 
### 3.2 Prediction-based 

基于 prediction 的方法，通过学习上下文的信息来预测下一个输出，来保证下一个输出相同的输入具有相似的 input vector

![word_embedding](word_embedding/word_emb_2.png)

![word_embedding](word_embedding/word_emb_3.png)

上述只是考虑到了前一个词汇的 vector 输入，当输入扩展到 n 的时候，采取的方法是将 weight metrix 强制相等

![word_embedding](word_embedding/word_emb_4.png)

- 如何保证 weight metrix 是相等的呢？

保证每次 weight update 的时候减去相同的分量

![word_embedding](word_embedding/word_emb_5.png)

### 3.3 Prediction-based -- Various Architecture

- CBOW(Continuous bag of word)
- Skip-gram

![word_embedding](word_embedding/word_emb_6.png)


### 3.4 Word Embedding 的 hidden layer 为什么不是 deep 的

Tomas Mikolov

> word embeeding是个很早的概念，以前也是 deep 的做法，但是效果并不太好，Tomas 使用很多 trick ，并采用单个 hidden layer 的做法将效果训练的很好

### 3.5 word vector的一些有趣的东西

![word_embedding](word_embedding/word_emb_7.png)

![word_embedding](word_embedding/word_emb_8.png)

![word_embedding](word_embedding/word_emb_9.png)

### 3. Document embedding

![document-embedding](word_embedding/word_emb_11.png)

一种直观的想法是使用 Bag-of-word 的思路，将 word ebedding 组成 document 的 semantic，word 的位置信息也很重要

![word_embedding](word_embedding/word_emb_12.png)

![word_embedding](word_embedding/word_emb_13.png)

![word_embedding](word_embedding/word_emb_14.png)
