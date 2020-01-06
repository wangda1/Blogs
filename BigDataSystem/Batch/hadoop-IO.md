---
title: Hadoop IO 操作
date: 2020-1-06 18:55
categories:
- BigDataSystem
- Batch
tags:
- BigDataSystem
- Batch
---

# Hadoop IO 的常见操作

## 1. 一种比较common的文件打开方式

注：这里并不使用 `java.io.File`　打开文件，因为这种方式只能打开本地文件，对于HDFS文件不支持打开；

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URI;
 
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileSystem;

StringBuffer buffer = new StringBuffer();
FSDataInputStream fsr = null;
BufferedReader bufferedReader = null;


FileSystem fs = FileSystem.get(URI.create(txtFilePath),conf);
fsr = fs.open(new Path(txtFilePath));
bufferedReader = new BufferedReader(new InputStreamReader(fsr));
while ((lineTxt = bufferedReader.readLine()) != null) ...
```

## 2. 列出HDFS文件目录下的所有文件

```java
private static FileSystem fs;
fs = FileSystem.get(URI.create(args[0]), conf);
private static ArrayList<Path> GetPaths(String path) throws IOException, FileNotFoundException {
	// 获取path路径下所有子文件夹路径
	ArrayList<Path> paths = new ArrayList<Path>();
//	File file = new File(path);
	FileStatus file = fs.getFileStatus(new Path(path));
	// 如果这个路径是文件夹
	if (file.isDirectory()) {
		// 获取路径下的所有文件
//		File[] files = file.listFiles();
		FileStatus[] files = fs.listStatus(file.getPath());
		for (int i=0; i<files.length; i++) {
			// 如果还是文件夹
			if (files[i].isDirectory()) {
				// 将其加入路径列表
				paths.add(files[i].getPath());
			}
			else {continue;}
		}
	}
	return paths;
}
```