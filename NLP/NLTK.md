## 背景介绍

NLTK 是最为知名的Python自然语言处理工具之一，全程：Natural Language ToolKit， 诞生于宾夕法尼亚大学，主要面向英文。但其很多模型或者模块都与语种无关，因此当实现了Tokenization 和分词之后，NLTK的很多工具包是可以复用的。

在NLTK中使用Stanford文本分析工具包也是一个常用的手段，如何在NLTK中调用Stanford中文工具包：
- http://www.zmonster.me/2016/06/08/use-stanford-nlp-package-in-nltk.html
- http://www.cnblogs.com/baiboy/p/nltk1.html

## 官方资料学习 https://www.nltk.org/book/

### 5. Categorizing and Tagging words

#### 5.1 tag sets 词性标注集

- `nltk.help.upenn('NN')` 可查询词性标注集的具体含义，如：

1. `NN` noun, common, singular or mass
2. `VB` verb, base form
3. `JJ` adjective or numeral, ordinal
4. `IN` preposition or conjunction, subordinating
5. `DT` determiner
6. `PRP` pronoun, personal

### 7. Extracting Information from Text

参考：https://www.nltk.org/book/ch07.html

#### 7.2 Chunking 分块 --- 命名实体识别技术之一

NLTK主要采用 chunk 技术来识别命名实体，这是一种基于规则的方法，如：

- Tag Patterns 标记模式
- Regular Expressions 正则表达式
- Classifier-Based Chunkers 基于分类器的分块器，主要加入不仅仅考虑 POS，还考虑 words 的内容

人工标记的 tag patterns 用来对 POS 进行匹配和识别，因此 Part-of-Speech 词性标注是其前提；

识别出的 chunk 的表示方法：  

- IOB标记（如 B-NP、I-NP等）
- 树状图标记 （将 词性标注后的 token 表示成树的叶子节点

#### 7.5 Named Entity Recognition

对命名实体识别中的一些词语进行解释：

- `Facility` : human-made artifacts in the domains of architecture and civil engineering
- `GPE` : geo-political entities such as city, state/province, and country

## 学习资料

- NLTK 官方在线书籍：https://www.nltk.org/book/
- 基于 NLTK 官方书籍的翻译版：《Python自然语言处理》 陈涛译
- 52nlp: http://textminingonline.com/dive-into-nltk-part-i-getting-started-with-nltk
