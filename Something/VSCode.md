---
title: VSCode
date: 2019-12-10 10:25:16
categories:
- Something
tags:
- Something
---

# VSCode

神器驾驭指南

## 1. 简介

## 2. 插件安装

## 3. 快捷键

- `F1` / `Ctrl+shift+P` 打开命令面板，可以执行VSCode的任何命令

## Q&A

### 3.1 在`Java`中不能导入第三方的库，出现　`xxx unresolve`　的问题

*ref: https://stackoverflow.com/a/57249227*

这种情况下有两种解决方法：

- 使用　`maven`　或　`gradle`　引入 `Jar`
- 按照以下步骤进行： a. 在工程目录下创建　`lib`　文件夹，放入`.jar` 文件 　b. 新建 `.classpath` 在其中　`<classpathentry kind="lib" path="lib/xxxx.jar"/>`
- 以上均不能解决问题，则　`F1` - input `Clean` - `clean workspace`

### 3.2 如何在 VSCode 中调试 python 程序

- 先选择Python interpreter:`F1` -> `Python: Select Interpreter` -> 选择 Conda 虚拟环境/主机上已存在的环境
- 在VScode的左侧边栏 -> Run 图标 -> 打开调试选项
- VScode 的上边栏 -> `Run` -> `Start Debugging` 打开调试的按钮选项，进行调试即可

## References

- https://nshen.net/article/2015-11-20/vscode/