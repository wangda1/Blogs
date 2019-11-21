# Introduction of Bert, ELMO, GPT

## 传统的 encoding 方式

- 1-of-N encoding

    one hot 的方式，但缺乏词汇之间的语义相似度

- word embedding

    refer: https://www.youtube.com/watch?v=X7PH3NuYW0Q

![word2com](..\NLP\IMG\word2com_1.png)

*In the typical embedding, the same type hase the same embedding.*

**下图中的 word， 属于相同的 type，但是不同的 token**

![word2com](..\NLP\IMG\word2com_2.png)

![word2com](..\NLP\IMG\word2com_3.png)

## BERT

**Encoder of Transformer**

![bert](..\NLP\IMG\word2com_7.png)

*在中文中，也许使用 character 更为有效*

### Training of Bert

- Approach 1: Masked LM

![bert_2](..\NLP\IMG\bert2.png)

- Approach 2: Next Sentence Prediction

![bert_3](..\NLP\IMG\bert_3.png)


## ELMO

Embeddings from Language Model (ELMO)

### RNN-based ELMO
- RNN-based language model
- 不需要标注数据，直接 trainning

![elmo](..\NLP\IMG\word2com_4.png)

### LSTM-based ELMO
- 考虑进正向及反向的 contex 信息

![elmo](..\NLP\IMG\word2com_5.png)

当深度的 LSTM 进行训练的时候，如何选取不同的 hidden layer作为 output 呢？？

进行 weight sum:

![elmo](..\NLP\IMG\word2com_6.png)
## GPT


