---
title: hadoop
date: 2019-12-10 10:25:16
categories:
- BigDataSystem
- Batch
tags:
- BigDataSystem
- Batch
---

# Hadoop

## 1. 安装与配置

## 2. 常用命令

### 2.1 对 `HDFS` 文件的增删改查命令

```python
# 基本格式
hadoop fs -cmd <args>
# ls
hadoop fs -ls /
# 删除
hadoop fs -r <file>
hadoop fs -rm -r <dir>
# 新建文件夹
hadoop fs -mkdir <path>
hadoop fs -mkdir -p <recursive path>
# put
hadoop fs -put <local file> <hdfs file>
# get
hadoop fs -get <hdfs file> <local file>
# moveFromLocal
hadoop fs -moveFromLocal <local file> <hdfs dst>
# copyFromLocal
hadoop fs -copyFromLocal <local src> <hdfs dst>
# mv,cp ...
```

### 2.2 运行 hadoop jar 包

`hadoop jar NaiveBayesDriver.jar naiveBayesDistribute`

## 3. Q&A

### 3.1 `hadoop fs -put` 当在文件路径中包含空格出现 `unexpected URISyntaxException`

解决方法：　把空格使用　`%20`　替代

### 3.1 如何查看hadoop的库文件路径

`./bin/hadoop classpath`，当不在 `maven` 工程下进行编译java文件的时候，需要将这个路径引入 `classpath`：

```shell
export CLASSPATH=$($HADOOP_HOME/bin/hadoop classpath):$CLASSPATH
```