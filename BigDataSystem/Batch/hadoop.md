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

### 3.2 如何查看hadoop的库文件路径

`./bin/hadoop classpath`，当不在 `maven` 工程下进行编译java文件的时候，需要将这个路径引入 `classpath`：

```shell
export CLASSPATH=$($HADOOP_HOME/bin/hadoop classpath):$CLASSPATH
```

### 3.3 `单机、伪分布、分布`模式的切换

*参考： http://dblab.xmu.edu.cn/blog/install-hadoop/*

总共涉及四个文件的修改：

- core-site.xml
- hdfs-site.xml
- mapred-site.xml
- yarn-site.xml

#### 3.3.1 单机模式

安装完成后，默认模式为单机模式

- core-site.xml

```xml
<configuration>
</configuration>
```

#### 3.3.2 伪分布模式

- core-site.xml

```xml
<configuration>
	<property>
		<name>hadoop.tmp.dir</name>
		<value>file:/usr/local/hadoop/tmp</value>
		<description>Abase for other temporary directories. </description>
	</property>
	<property>
		<name>fs.defaultFS</name>
		<value>hdfs://Master:9000</value>
	</property>
</configuration>
```

- hdfs-site.xml

```xml
<configuration>
	<property>
		<name>dfs.namenode.secondary.http-address</name>
		<value>Master:50090</value>
	</property>
	<property>
		<name>dfs.replication</name>
		<value>1</value>
	</property>
	<property>
		<name>dfs.namenode.name.dir</name>
		<value>file:/usr/local/hadoop/tmp/dfs/name</value>
	</property>
	<property>
		<name>dfs.datanode.data.dir</name>
		<value>file:/usr/local/hadoop/tmp/dfs/data</value>
	</property>
</configuration>
```

与　`yarn` 有关的两个配置文件：

- mapred-site.xml

```xml
<configuration>
	<property>
		<name>mapreduce.framework.name</name>
		<value>yarn</value>
	</property>
	<property>
		<name>mapreduce.jobhistory.address</name>	
		<value>Master:10020</value>
	</property>
	<property>
		<name>mapreduce.jobhistory.webapp.address</name>
		<value>Master:19888</value>
	</property>
</configuration>
```

- yarn-site.xml

```xml
<configuration>

<!-- Site specific YARN configuration properties -->
		<property>
			<name>yarn.resourcemanager.hostname</name>
			<value>Master</value>
		</property>

		<property>
			<name>yarn.nodemanager.aux-services</name>
			<value>mapreduce_shuffle</value>
		</property>
</configuration>
```

```
./bin/hdfs namenode -format   # 重新格式化 NameNode
./sbin/start-dfs.sh  # 重启
./sbin/start-yarn.sh      # 启动YARN
./sbin/mr-jobhistory-daemon.sh start historyserver  # 开启历史服务器，才能在Web中查看任务运行情况
```

注意事项：

> **不启动 YARN 需重命名 mapred-site.xml** 如果不想启动 YARN，务必把配置文件 mapred-site.xml 重命名，改成 mapred-site.xml.template，需要用时改回来就行。否则在该配置文件存在，而未开启 YARN 的情况下，运行程序会提示 “Retrying connect to server: 0.0.0.0/0.0.0.0:8032” 的错误，这也是为何该配置文件初始文件名为 mapred-site.xml.template。

#### 3.3.3 分布模式

配置文件相比于伪分布式模式多了一个 `slaves` 文件，里面包含由所有 slave 节点的 hostname，注意：　hosts　文件中应该加入对于 slave hostname 的解析
注意事项：

> **伪分布式、分布式配置切换时的注意事项**

> 1, 从分布式切换到伪分布式时，不要忘记修改 slaves 配置文件；

> 2, 在两者之间切换时，若遇到无法正常启动的情况，可以删除所涉及节点的临时文件夹，这样虽然之前的数据会被删掉，但能保证集群正确启动。所以如果集群以前能启动，但后来启动不了，特别是 DataNode 无法启动，不妨试着删除所有节点（包括 Slave 节点）上的 /usr/local/hadoop/tmp 文件夹，再重新执行一次 hdfs namenode -format，再次启动试试。
## 4. `hadoop`分布式程序开发的一般步骤

- 使用文件系统的接口，使用`FileSystem`类的一系列方法进行操作文件，这样具有一般性，既可以添加本地文件系统的路径`file://xxxx`，也可以使用HDFS文件系统的路径`hdfs://xxxxx`
- 可在打包成`jar`之前，先将数据集存放在本地文件系统，使用本地文件系统进行测试，没问题后将路径替换为HDFS文件系统的路径；
*虽然也可以直接在IDE中直接进行运行，操作HDFS*