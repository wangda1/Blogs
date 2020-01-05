---
title: Jupyter
date: 2019-11-30 18:47:58
categories:
- MLDL
tags:
- MLDL
---

# Jupyter 的使用

Jupyter 通篇内容有两种格式：Markdown 与 code，Markdown 模式下可以进行 Markdown 的编辑，code 模式下则可以进行代码的运行，这样有机地将代码和注释结合起来。

## Markdown 模式

`shift`+`enter` 快捷键是个很重要的快捷键，在 Markdown 模式下使用则可以进行预览和编辑的切换

## Code 模式

`shift`+`enter` 快捷键在 `code/md` 模式下可以进行代码/字体的创建和运行

## 快捷键

- `H`：查看所有快捷键。
- `S`：保存当前 Notebook 内容。
- `P`：调出 Notebook 命令栏。

### 对单元格（Cell）的操作

- `A/a`: 在当前单元格上方新建单元格 cell
- `B/b`：在当前单元格下方新建空白单元格。
- `M`：将单元格格式转换为 Markdown。
- `Y`：将单元格格式转换为 Code。
- `连续按 D+D/ d+d`：删除当前单元格。（慎用，推荐使用 X 剪切单元格代替，因为其可以起到删除效果，且删错了还可以粘贴回来）
- `Shift + Enter`：运行当前单元格内容。（当 Markdown 单元格处于编辑状态时，运行即可复原)
- `ESC` 在编辑模式（绿色）与非编辑模式（蓝色）下切换