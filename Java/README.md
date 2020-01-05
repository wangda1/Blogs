---
title: README
date: 2019-12-02 16:44:37
categories:
- Java
tags:
- Java
---

# Java

## Java环境的配置

Java 环境变量的配置：

- `JAVA_HOME` 指向 JDK 的路径
- `CLASS_PATH` 的路径常用： `.;%JAVA_HOME%\lib\;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar;`
- `PATH` 的路径常用： `%JAVA_HOME%\bin\;%JAVA_HOME%\jre\bin\;`

## IDEA 的环境配置（必要配置部分）

JDK、Java Language Level的配置：

`File` - `Project Structure` - `Project` 可以配置：

- `Project SDK` 
- `Project language level`
- `Project compiler output`

导入 jar 包：

`File` - `Project Structure` - `Modules` - `Dependencies` 点击 + 添加 jar 包的路径
