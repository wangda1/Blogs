---
title: wiki data 简介
date: 2019-01-16 10:09:00
categories:
- NLP
- 实体与关系抽取
tags:
- NLP
- 实体与关系抽取
---

# Wikidata 简介

这里为什么简要介绍 wiki data，因为实体链接（Entity link）常用到的数据集是 wiki data，

## wiki data 与 wiki pedia 的关系

> wikidata is a free and open knowledge base that can be read and edited by both humans and machines. Wikidata acts as central storage for the structured data of its Wikimedia sister projects including Wikipedia, Wikivoyage, Wikisource, and others.

## wiki data 的说明 [url](https://en.wikipedia.org/wiki/Wikidata)

- Items: Wikidata is a document-oriented database, focused on items, which represent topics, concepts, or objects.Each item is identified by a unique number, prefixed with the letter Q, known as a "QID".
- Property: A property describes the data value of a statement and can be thought of as a category of data, for example color (P462) for the data value blue (Q1088).
- Statements: Statements are how any information known about an item is recorded in Wikidata. 
- Lexemes: In linguistics, a lexeme is a unit of lexical meaning. Similarly, Wikidata's lexemes are items with a structure that makes them more suitable to store lexicographical data.

## Wikidata api 的使用

- [api document](https://www.wikidata.org/w/api.php)
- [document2](https://www.mediawiki.org/wiki/API:Presenting_Wikidata_knowledge)

```python
# coding=utf-8

import requests
params = dict (
        action='wbsearchentities',
        format='json',
        language='en',
        uselang='en',
        # type='property',
        search='Hubei Province'
        )
http_proxies = {
    "http": "http://127.0.0.1:1080",
    "https": "https://127.0.0.1:1080"
}
response = requests.get('https://www.wikidata.org/w/api.php?', params, proxies=http_proxies).json()
print(response.get('search')[0]['id'])
```

## Wikipedia api 的使用

- [api document](https://en.wikipedia.org/w/api.php?action=help&modules=query)
- [document2](https://www.mediawiki.org/wiki/API:Main_page)

```python
# coding=utf-8

import requests
params_wikipedia = dict (
        action='query',
        prop='pageprops',
        ppprop='wikibase_item',
        redirects=1,
        titles='trump'
)
http_proxies = {
    "http": "http://127.0.0.1:1080",
    "https": "https://127.0.0.1:1080"
}
response = requests.get('https://en.www.wikipedia.org/w/api.php?', params, proxies=http_proxies).json()

```

- `pip install wikipedia` 上述方法的 python 库版本

> Wikipedia is a Python library that makes it easy to access and parse data from Wikipedia.
> Search Wikipedia, get article summaries, get data like links and images from a page, and more. Wikipedia wraps the MediaWiki API so you can focus on using Wikipedia data, not getting it.

注： wikidata api 与 wikipedia api 所返回的的 QID 都是吧wikidata 中的 QID，但 pageId 不同，它分别代表在 Wikidata 与 Wikipedia 中的 page number.

## Wikidata 数据源的下载

https://www.wikidata.org/wiki/Wikidata:Database_download 可下载 Wikidata 的数据（数据规模较大），进行关系抽取等任务。

`spacy` 的 EL（Entity Link）任务就是利用从 Wikidata 下载的数据进行模型的训练。

> This takes as input the locations of a Wikipedia and a Wikidata dump, and produces a KB directory + training file
>- WikiData: get latest-all.json.bz2 from https://dumps.wikimedia.org/wikidatawiki/entities/
> - Wikipedia: get enwiki-latest-pages-articles-multistream.xml.bz2 from https://dumps.wikimedia.org/enwiki/latest/ (or for any other language)

## 总结

两种方式进行 entity 的查询会返回一系列 candidate 进行候选，这种方法往往在 NLP 的 `实体对齐、实体消歧` 中存在一定的局限性，常作为 EL 的前序步骤。