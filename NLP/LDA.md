LDA 

## 输入与训练

`The interface follows conventions found in scikit-learn` LDA的接口遵循 `scikit-learn` 的规范，因此可使用 `scikit-learn` 提供的数据预处理方法如 `CountVectorizer` 或 `TfidfVectorizer` 将文本数据转化为向量，并作为 LDA 的输入进行训练。

```python
>>> model = lda.LDA(n_topics=20, n_iter=1000, random_state=1)
>>> model.fit(vectorizer.fit_transform(corpus).toarray())   # Input the weight
```

## 输出

- Topic-Word Distribution

```python
>>> topic_word = model.topic_word_  # model.components_ also works
>>> n_top_words = 8
>>> for i, topic_dist in enumerate(topic_word):
...     topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
...     print('Topic {}: {}'.format(i, ' '.join(topic_words)))
```

- Document-Topic Distribution

```python
>>> doc_topic = model.doc_topic_
>>> for i in range(10):
...     print("{} (top topic: {})".format(titles[i], doc_topic[i].argmax()))
...     print("{} (top topic: {})".format(titles[i], np.argsort(doc_topic[i])[:-4:-1]))
```

## 总结

由此，我们观察到 `lda` 全程对 TF-Matrix 进行计算，并没有考虑词语的上下文关系，是 Bow 模型。

## 参考

- https://pypi.org/project/lda/
- https://juejin.im/post/5ab365f25188252c32199636
- https://github.com/scarlettgin/novel_analysis