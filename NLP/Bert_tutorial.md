---
title: Bert Tutorial
date: 2020-01-11 20:44:00
categories:
- NLP
tags:
- NLP
---

# 1. Bert Tutorial

## 1.1 Bert 的输入格式

BERT requires specifically formatted inputs. For each tokenized input sentence, we need to create:

- input ids: a sequence of integers identifying each input token to its index number in the BERT tokenizer vocabulary
- segment mask: (optional) a sequence of 1s and 0s used to identify whether the input is one sentence or two sentences long. For one sentence inputs, this is simply a sequence of 0s. For two sentence inputs, there is a 0 for each token of the first sentence, followed by a 1 for each token of the second sentence
- attention mask: (optional) a sequence of 1s and 0s, with 1s for all input tokens and 0s for all padding tokens (we'll detail this in the next paragraph)
- labels: a single value of 1 or 0. In our task 1 means "grammatical" and 0 means "ungrammatical"

## 1.2 Bert 的参数设置

> For the purposes of fine-tuning, the authors recommend the following hyperparameter ranges:

- Batch size: 16, 32
- Learning rate (Adam): 5e-5, 3e-5, 2e-5
- Number of epochs: 2, 3, 4

# 2. BertTokenizer 之 `WordPiece` Model

```python
# Load pre-trained model tokenizer (vocabulary)
>>> tokenizer = BertTokenizer.from_pretrained('bert-base-uncased'
>>> text = "Here is the sentence I want embeddings for."
>>> marked_text = "[CLS] " + text + " [SEP]"

# Tokenize our sentence with the BERT tokenizer
>>> tokenized_text = tokenizer.tokenize(marked_text)

# Print out the tokens.
>>> print (tokenized_text
['[CLS]', 'here', 'is', 'the', 'sentence', 'i', 'want', 'em', '##bed', '##ding', '##s', 'for', '.', '[SEP]']
```

使用 `BertTokenizer` 进行分词后的序列包含 `##`，这主要的原因是 bert 使用 vocabulary 词典的大小为 3000，为了在训练时能够将所有的英文文章中的单词都能得到编码，就是用了 `WordPiece`。具体：

> Why does it look this way? This is because the BERT tokenizer was created with a WordPiece model. This model greedily creates a fixed-size vocabulary of individual characters, subwords, and words that best fits our language data. Since the vocabulary limit size of our BERT tokenizer model is 30,000, the WordPiece model generated a vocabulary that contains all English characters plus the ~30,000 most common words and subwords found in the English language corpus the model is trained on. This vocabulary contains four things:
>
> - Whole words
> - Subwords occuring at the front of a word or in isolation ("em" as in "embeddings" is assigned the same vector as the standalone sequence of characters "em" as in "go get em" )
> - Subwords not at the front of a word, which are preceded by '##' to denote this case
> - Individual characters
>
> To tokenize a word under this model, the tokenizer first checks if the whole word is in the vocabulary. If not, it tries to break the word into the largest possible subwords contained in the vocabulary, and as a last resort will decompose the word into individual characters. Note that because of this, we can always represent a word as, at the very least, the collection of its individual characters.
>
> As a result, rather than assigning out of vocabulary words to a catch-all token like 'OOV' or 'UNK,' words that are not in the vocabulary are decomposed into subword and character tokens that we can then generate embeddings for.
>
> So, rather than assigning "embeddings" and every other out of vocabulary word to an overloaded unknown vocabulary token, we split it into subword tokens ['em', '##bed', '##ding', '##s'] that will retain some of the contextual meaning of the original word. We can even average these subword embedding vectors to generate an approximate vector for the original word. [详见](https://mccormickml.com/2019/05/14/BERT-word-embeddings-tutorial/)

## 参考

- [google-bert-github](https://github.com/google-research/bert)
- [一起读bert文本分类代码](https://zhuanlan.zhihu.com/p/56103665)
- [BERT for dummies — Step by Step Tutorial](https://towardsdatascience.com/bert-for-dummies-step-by-step-tutorial-fb90890ffe03)，对应的 [Jupyter notebook](https://colab.research.google.com/drive/1ywsvwO6thOVOrfagjjfuxEf6xVRxbUNO)