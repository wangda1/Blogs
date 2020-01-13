---
title: Bert Tutorial
date: 2020-01-11 20:44:00
categories:
- NLP
tags:
- NLP
---

# 1. Bert Tutorial

## 1.1 

BERT requires specifically formatted inputs. For each tokenized input sentence, we need to create:

- input ids: a sequence of integers identifying each input token to its index number in the BERT tokenizer vocabulary
- segment mask: (optional) a sequence of 1s and 0s used to identify whether the input is one sentence or two sentences long. For one sentence inputs, this is simply a sequence of 0s. For two sentence inputs, there is a 0 for each token of the first sentence, followed by a 1 for each token of the second sentence
- attention mask: (optional) a sequence of 1s and 0s, with 1s for all input tokens and 0s for all padding tokens (we'll detail this in the next paragraph)
- labels: a single value of 1 or 0. In our task 1 means "grammatical" and 0 means "ungrammatical"