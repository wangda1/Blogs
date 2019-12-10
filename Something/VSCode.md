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

## References

- https://nshen.net/article/2015-11-20/vscode/