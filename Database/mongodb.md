# mongo DB

## 1. 插入

## 2. 删除

## 3. 修改

## 4. 查询

mongodb的查询分为两种：

- 普通查询：类似于 sql 中的 `select where`
- 聚合查询：类似于 sql 中的 `group by`

### 4.1 普通查询

mongo的普通查询是通过在 {} 中指定过滤参数来进行查询

- `db.collection.find()` 查询所有
- `db.collection.find( { status: "D" } )` 查询 status 为D的记录
- `db.collection.find( { status: { $in: ["A", "D"] } } )` 查询 status 为 数组中的记录

AND 与 OR 运算符的使用

- `db.collection.find( { status: "A", qty: { $lt: 30 } } )` 查询 status 为 A， qty 小于 30 的记录，类似于 AND 的记录查询
- `db.collection.find( { $or: [ {status: "A" }, { qty: { $lt: 30 } } ] } )` OR 的记录查询

指定字段

- `db.collection.find( {}, { user_id: 1, status: 1, _id: 0}` 不显示 ID

## 5. 函数

- 指定数据的数量：`limit(NUM)`
- 跳过指定的数量：`skip(NUM)`

## 6. 使用 PyMongo

在 Pymongo 中使用命令与 mongo 命令相同，少许对应关系：

- `null` <--> `None`
- `false` <--> `False`

### 6.1 查询

使用 Pymongo 进行查询的时候返回 `cursor` 对象，这是一个可迭代的对象

- 查询字段是否为设置
`db.find({'news_abstract_ne_with_nltk': {'$exists': False}})`

- 查询字段是否为空或不存在
`db.find({'news_abstract_ne_with_nltk': None)`

- 查询字段存在且为空
`db.find({'news_abstract_ne_with_nltk': {'$exists': True, '$in': [None]}})`

### 6.2 计数

- `count_documents({})`

### 6.3 修改文档

- `update_one()` 更新一条记录 
- `update_many()` 批量更新记录

```python
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["runoobdb"]
mycol = mydb["sites"]
 
myquery = { "alexa": "10000" }
newvalues = { "$set": { "alexa": "12346" } }
 
mycol.update_one(myquery, newvalues)
```

- https://www.yangyanxing.com/article/specialUse-in-pymongo.html

## 学习参考

- https://www.jianshu.com/p/dbf966f8d314
- https://docs.mongodb.com/manual/tutorial/query-documents/
- https://api.mongodb.com/python/current/tutorial.html#querying-for-more-than-one-document