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


## BERT

**Encoder of Transformer**

![bert](..\NLP\IMG\word2com_7.png)

*在中文中，也许使用 character 更为有效*

### Training of Bert

- Approach 1: Masked LM

![bert_2](..\NLP\IMG\bert2.png)

- Approach 2: Next Sentence Prediction

![bert_3](..\NLP\IMG\bert_3.png)

### How to use Bert

- 把 bert 的训练和下游的任务放在一起进行 train

#### case1: Sequence -> class

在开头的地方给一个分类的符号，再通过 linear classifier 进行分类

![bert4](..\NLP\IMG\bert_4.png)

#### case2: sentences' word slot

句子的词分类问题，将句子中的每个词填入一个class slot

![bert_case_2](..\NLP\IMG\bert_5.png)
#### case3: premise -> 判断 hypothesis

输入两个句子，一个作为 premise，一个作为 hypothesis，判断是否正确：T/F/unknown

![bert_case_3](..\NLP\IMG\bert_6.png)


#### case4: Extraction-based QA

![bert_case_4](..\NLP\IMG\bert_7.png)

![bert_case_4](..\NLP\IMG\bert_8.png)

### 中文版本的 bert -- Erine

![erine](..\NLP\IMG\erine.png)

### What bert learns??

研究者通过将 bert 24层的 embedding 输出对比发现， bert 的24层从低到高学习到了 NLP 的大部分过程：`文法->句法->语义`

![bert_9](..\NLP\IMG\bert_9.png)

### Multilingual Bert

多语言的 bert，google 的研究者爬取104种语言的 wiki进行训练 多语言版本的 bert

![bert_10](..\NLP\IMG\bert_10.png)


## GPT

**Generative Pre-Training**
特别大特别大的一个预训练模型

GPT 是 transformer 的 decoder，由 openAI 制作

![GPT](..\NLP\IMG\gpt_1.png)

GPT-2 model 特别巨大，能够在**没有训练资料**的情况下，做：
- Reading Comprehension
- Summarization
- Translation

![gpt_2](..\NLP\IMG\gtp_2.png)

GPT-2 OpenAI 最大的model 拥有的参数有 1542M，但考虑到到多种问题并没有被 release，release 的 model 的版本与 bert 差不多.

### 例子

- https://talktotransformer.com/