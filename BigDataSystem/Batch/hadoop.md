# Hadoop

## 1. 安装与配置

## 2. 常用命令

## 3. Q&A

### 3.1 如何查看hadoop的库文件路径

`./bin/hadoop classpath`，当不在 `maven` 工程下进行编译java文件的时候，需要将这个路径引入 `classpath`：

```shell
export CLASSPATH=$($HADOOP_HOME/bin/hadoop classpath):$CLASSPATH
```