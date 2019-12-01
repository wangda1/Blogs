# Cassandra

> *wikipedia:* Cassandra 是一套开源式分布式 NoSQL 数据库系统。 最初由 Facebook 开发，用于储存收件箱等简单格式数据，集 Google BigTable 的数据模型与 Amazon Dynamo的完全分布式架构于一身。

## 1. 数据模型

Cassandra使用了 Google 设计的 BigTable 的数据模型，与面向行（row）的传统关系型数据库或键值存储（key-value）数据库不同，Cassandra使用的是宽列存储模型（wide column stores。

## 2. 存储模型

与 BigTable、HBase不同，Cassandra的数据并不存储在分布式文件系统如 GFS 或 HDFS 中，而是直接存储于本地。与 BigTable 一样，Cassandra 也是日志型数据库，采用 `LSM-Tree` 存储算法，特点是适合于写入较多的场景。

旧版的Cassandra与客户端交互的方法是通过thrift，而当前新版本的Cassandra采用与SQL语言类似的 `CQL` 语言来实现数据模型的定义和数据的读写。其中BigTable中的 `列族(Column Family)` 在Cassandra中被称作类似关系型数据库中的称呼——`表(table)`，而Cassandra/BigTable中的 `row key` 和 `column key` 并称为主键 `(primary key)`。

Cassandra的row key决定了该行数据存储在哪些节点中，因此row key需要按哈希来存储，不能顺序的扫描或读取，而一个row内的column key是顺序存储的，可以进行有序的扫描或范围查找

## 3. 分布式架构

Cassandra 的系统架构与 Dynamo 类似，属于一致性哈希的完全 P2P 架构，每行数据通过哈希来决定应该存在哪个节点或哪些节点。集群没有 master 节点，所有节点都是同样的角色，避免了系统的单点瓶颈，集群间的状态同步通过 Gossip 协议来进行 P2P 通信。

在 CAP（Consistency、Available、Partition）问题的 trade-off 上，Cassandra 和 Dynamo一样比较灵活。Cassandra的每个 keyspace 可配置一行数据会写入多少个节点才算写入成功(设这个数为N)，来保证数据不因为机器宕机或磁盘损坏而丢失数据，即保证了CAP中的P。用户在读写数据时可以指定要求成功写到多少个节点才算写入成功(设为W)，以及成功从多少个节点读取到了数据才算成功(设为R)。可推理得出，当 `W+R>N` 时，读到的数据一定是上一次写入的，即维护了 `强一致性`，确保了 `CAP` 中的 `C`。当 `W+R<=N` 时，数据是 `最终一致性` 因为存在一段时间可能读到的并不是最新版的数据。当 `W=N` 或 `R=N` 时，意味着系统只要有一个节点无响应或宕机，就有一部分数据无法成功写或者读，即失去了CAP中的可用性A。 *from wikipedia*

## 参考

1. https://zh.wikipedia.org/wiki/Cassandra
2. 