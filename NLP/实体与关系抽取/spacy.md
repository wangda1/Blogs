---
title: spacy 使用记录
date: 2019-01-16 10:09:00
categories:
- NLP
- 实体与关系抽取
tags:
- NLP
- 实体与关系抽取
---

# spacy 使用记录

## NER的使用


## EL的使用

update on 2020/3/26

`spacy` 并没有提供现成的 EL model，而是要通过spacy提供的 framework 自己训练出一个 model，至于为什么 spacy 不提供一个训练好的 model release 出来，见 [issues#4511](https://github.com/explosion/spaCy/issues/4511) 作者给出了解释。

Model 的训练过程需要耗费较长时间，这里记录一下，步骤参考：https://github.com/explosion/spaCy/tree/master/bin/wiki_entity_linking

Step 1.

`python wikidata_pretrain_kb.py wiki/latest-all.json.bz2 wiki/enwiki-latest-pages-articles-multistream.xml.bz2 output/ en_core_web_md`

这里使用的是 英文的 `en_core_web_md` 模型，使用 `en_core_web_sm` 模型会报错。

然后经历的过程大概是这样的：

- Intel(R) Xeon(R) Gold 6132 CPU @ 2.60GHz 6核
- 60GB 内存

```
2020-03-25 10:57:56,366 - INFO - __main__ - Creating KB with Wikipedia and WikiData
2020-03-25 10:57:56,366 - INFO - __main__ - STEP 1: Loading NLP model en_core_web_md
2020-03-25 10:58:09,601 - INFO - __main__ - STEP 2: Writing prior probabilities to output/prior_prob.csv
2020-03-25 11:02:19,011 - INFO - bin.wiki_entity_linking.wikipedia_processor - processed 25000000 lines of Wikipedia XML dump
2020-03-25 11:06:06,973 - INFO - bin.wiki_entity_linking.wikipedia_processor - processed 50000000 lines of Wikipedia XML dump

...

2020-03-25 13:04:44,104 - INFO - bin.wiki_entity_linking.wikipedia_processor - Finished. processed 1154673507 lines of Wikipedia XML dump
2020-03-25 13:06:49,519 - INFO - __main__ - STEP 3: Calculating and writing entity frequencies to output/entity_freq.csv
2020-03-25 13:07:47,159 - INFO - __main__ - STEP 4: Parsing and writing Wikidata entity definitions to output/entity_defs.csv
2020-03-25 13:11:46,605 - INFO - bin.wiki_entity_linking.wikidata_processor - processed 500000 lines of WikiData JSON dump
2020-03-25 13:14:44,627 - INFO - bin.wiki_entity_linking.wikidata_processor - processed 1000000 lines of WikiData JSON dump

...

2020-03-25 23:17:48,677 - INFO - bin.wiki_entity_linking.wikidata_processor - Finished. Processed 78951019 lines of WikiData JSON dump
2020-03-25 23:17:52,051 - INFO - __main__ - STEP 4b: Writing Wikidata entity aliases to output/entity_alias.csv
2020-03-25 23:17:56,290 - INFO - __main__ - STEP 4c: Writing Wikidata entity descriptions to output/entity_descriptions.csv
2020-03-25 23:17:58,717 - INFO - __main__ - STEP 5: Parsing and writing Wikipedia gold entities to output/gold_entities.jsonl
2020-03-25 23:19:36,808 - INFO - bin.wiki_entity_linking.wikipedia_processor - Processed 10000 articles

...

2020-03-26 02:17:41,098 - INFO - bin.wiki_entity_linking.wikipedia_processor - Finished. Processed 6890313 articles
2020-03-26 02:17:43,364 - INFO - __main__ - STEP 6: Creating the KB at output/kb
2020-03-26 02:17:52,463 - INFO - bin.wiki_entity_linking.kb_creator - Loaded pretrained vectors of size 300
2020-03-26 02:17:52,463 - INFO - bin.wiki_entity_linking.kb_creator - Filtering entities with fewer than 20 mentions
2020-03-26 02:18:17,807 - INFO - bin.wiki_entity_linking.kb_creator - Kept 1148892 entities from the set of 5763431
2020-03-26 02:18:17,808 - INFO - bin.wiki_entity_linking.kb_creator - Training entity encoder
2020-03-26 02:18:27,323 - INFO - bin.wiki_entity_linking.train_descriptions - loss: 1.0226774291992187 
2020-03-26 02:20:38,614 - INFO - bin.wiki_entity_linking.train_descriptions - loss: 0.3986138000488281 
2020-03-26 02:22:47,917 - INFO - bin.wiki_entity_linking.train_descriptions - loss: 0.22751368713378906 
2020-03-26 02:24:58,512 - INFO - bin.wiki_entity_linking.train_descriptions - loss: 0.15389662170410157 
2020-03-26 02:27:09,470 - INFO - bin.wiki_entity_linking.train_descriptions - loss: 0.11821630859375 
2020-03-26 02:29:19,072 - INFO - bin.wiki_entity_linking.train_descriptions - loss: 0.09795716857910156 
2020-03-26 02:31:27,877 - INFO - bin.wiki_entity_linking.train_descriptions - loss: 0.0902191925048828 
2020-03-26 02:33:37,375 - INFO - bin.wiki_entity_linking.train_descriptions - loss: 0.07779336547851562 
2020-03-26 02:35:46,578 - INFO - bin.wiki_entity_linking.train_descriptions - loss: 0.07243069458007813 
2020-03-26 02:37:56,318 - INFO - bin.wiki_entity_linking.train_descriptions - loss: 0.07262858581542969 
2020-03-26 02:40:06,218 - INFO - bin.wiki_entity_linking.train_descriptions - loss: 0.07191573333740234 
2020-03-26 02:42:16,195 - INFO - bin.wiki_entity_linking.train_descriptions - loss: 0.07062159729003906 
2020-03-26 02:44:26,376 - INFO - bin.wiki_entity_linking.train_descriptions - loss: 0.0659771957397461 
2020-03-26 02:46:36,478 - INFO - bin.wiki_entity_linking.train_descriptions - loss: 0.06245959091186523 
2020-03-26 02:48:08,080 - INFO - bin.wiki_entity_linking.train_descriptions - Trained entity descriptions on 343000 (non-unique) descriptions across 5 epochs
2020-03-26 02:48:08,081 - INFO - bin.wiki_entity_linking.train_descriptions - Final loss: 0.06493917846679688
2020-03-26 02:48:08,081 - INFO - bin.wiki_entity_linking.kb_creator - Getting entity embeddings
2020-03-26 02:49:16,621 - INFO - bin.wiki_entity_linking.train_descriptions - Encoded: 200000 entities
2020-03-26 02:50:26,592 - INFO - bin.wiki_entity_linking.train_descriptions - Encoded: 300000 entities
2020-03-26 02:51:30,845 - INFO - bin.wiki_entity_linking.train_descriptions - Encoded: 400000 entities
2020-03-26 02:52:37,864 - INFO - bin.wiki_entity_linking.train_descriptions - Encoded: 500000 entities
2020-03-26 02:53:41,903 - INFO - bin.wiki_entity_linking.train_descriptions - Encoded: 600000 entities
2020-03-26 02:54:48,951 - INFO - bin.wiki_entity_linking.train_descriptions - Encoded: 700000 entities
2020-03-26 02:55:53,231 - INFO - bin.wiki_entity_linking.train_descriptions - Encoded: 800000 entities
2020-03-26 02:57:01,271 - INFO - bin.wiki_entity_linking.train_descriptions - Encoded: 900000 entities
2020-03-26 02:58:04,693 - INFO - bin.wiki_entity_linking.train_descriptions - Encoded: 1000000 entities
2020-03-26 02:59:13,314 - INFO - bin.wiki_entity_linking.train_descriptions - Encoded: 1100000 entities
2020-03-26 03:00:18,196 - INFO - bin.wiki_entity_linking.train_descriptions - Encoded: 1148892 entities
2020-03-26 03:00:49,433 - INFO - bin.wiki_entity_linking.train_descriptions - Encoded: 1148892 entities
2020-03-26 03:00:49,558 - INFO - bin.wiki_entity_linking.kb_creator - Adding 1148892 entities
2020-03-26 03:00:57,009 - INFO - bin.wiki_entity_linking.kb_creator - Adding aliases from Wikipedia and Wikidata
2020-03-26 03:00:57,011 - INFO - bin.wiki_entity_linking.kb_creator - Adding WP aliases
2020-03-26 03:01:58,750 - INFO - __main__ - kb entities: 1148892
2020-03-26 03:01:58,750 - INFO - __main__ - kb aliases: 1665015
2020-03-26 03:02:09,177 - INFO - __main__ - Done!

```