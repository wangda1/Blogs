---
title: jieba
date: 2019-11-21 21:49:28
categories:
- NLP
tags:
- NLP
---

## Jieba简介

jieba是一款中文分词工具


## 常用API

`jieba.cut(self, sentence, cut_all=False, HMM=True)`

- sentence：输入文本
- cut_all：是否全模式分词
- HMM：是否开启 HMM，默认模式开启HMM，对中文歧义有较好的分词效果

`jieba.cut_for_search(self, sentence, cut_all=False, HMM=True)`

- 搜索引擎模式？？

```
import jieba.posseg as pseg

result = pseg.cut(test_sent)
```
- 使用 `pseg.cut` 分词，并显示词性

## 中文歧义与去除停用词

中文歧义，中文由于对词语缺乏明显的区分标识，因此在分词方面往往存在一定的歧义，Jieba 使用 HMM（隐马尔科夫模型）仍取得了不错的效果；

去除停用词，即通过中文停用词表，来对分词后的词语比对，去除常用的停用词。


## 分词更准确的 trick

- 在 jieba 中加入一些不常见的中文词语： `jieba.add_word('xxx')`
- 添加自定义词库： `jieba.loca_userdict("xxx.txt")`
-  

