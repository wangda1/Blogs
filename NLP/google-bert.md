---
title: Google Bert
date: 2020-01-15 9:11:00
categories:
- NLP
tags:
- NLP
---

# Google Bert

[google-bert-github](https://github.com/google-research/bert) 部分代码解读

## `run_classifier.py` 分类 demo

其中包含的主要的类有：

```
class InputExample(object):

class PaddingInputExample(object):

class InputFeatures(object):

class DataProcessor(object):

class XnliProcessor(DataProcessor):

class MnliProcessor(DataProcessor):

class MrpcProcessor(DataProcessor):

class ColaProcessor(DataProcessor):

```

```python
# create_model function
def create_model(bert_config, is_training, input_ids, input_mask, segment_ids,
                 labels, num_labels, use_one_hot_embeddings):
  """Creates a classification model."""
  # 首先调用 modeling.BertModel 得到 bert 模型
  # Bert Model 需要的输入为：1. input_ids, 2. input_mask 3. segment_ids
  # bert_config 直接加载下载得到的配置文件
  model = modeling.BertModel(
      config=bert_config,
      is_training=is_training,
      input_ids=input_ids,
      input_mask=input_mask,
      token_type_ids=segment_ids,
      use_one_hot_embeddings=use_one_hot_embeddings)

  # In the demo, we are doing a simple classification task on the entire
  # segment.
  #
  # If you want to use the token-level output, use model.get_sequence_output()
  # instead.
  # bert 的输出有两种：
  # toekns level: model.get_sequence_output(): [batch_size, seq_len, embeddings_size]
  # sentences level: model.get_pooled_output(): [batch_size, embeddings_size]
  output_layer = model.get_pooled_output()

  hidden_size = output_layer.shape[-1].value

  output_weights = tf.get_variable(
      "output_weights", [num_labels, hidden_size],
      initializer=tf.truncated_normal_initializer(stddev=0.02))

  output_bias = tf.get_variable(
      "output_bias", [num_labels], initializer=tf.zeros_initializer())

  with tf.variable_scope("loss"):
    if is_training:
      # I.e., 0.1 dropout
      output_layer = tf.nn.dropout(output_layer, keep_prob=0.9)

    logits = tf.matmul(output_layer, output_weights, transpose_b=True)
    logits = tf.nn.bias_add(logits, output_bias)
    probabilities = tf.nn.softmax(logits, axis=-1)
    log_probs = tf.nn.log_softmax(logits, axis=-1)

    one_hot_labels = tf.one_hot(labels, depth=num_labels, dtype=tf.float32)

    per_example_loss = -tf.reduce_sum(one_hot_labels * log_probs, axis=-1)
    loss = tf.reduce_mean(per_example_loss)

    return (loss, per_example_loss, logits, probabilities)

```

`main` 部分

```python
```

## `run_squad.py` SQuAD（The Stanford Question and Answer Datasets） demo

## `modelling.py` bert 上游模型

## `optimization.py` 优化器部分

## `run_pretraining.py` 预训练部分

## 参考

- [实体关系抽取-github:yuanxiaosc](https://github.com/yuanxiaosc/Entity-Relation-Extraction)