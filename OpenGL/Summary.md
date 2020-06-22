---
title: OpenGL 综述
date: 2020-06-18 22:15:00
categories:
- OpenGL
tags:
- OpenGL
---

# OpenGL

## 前言

### 状态机

OpenGL 本质上是个大状态机

### 对象

在 OpenGL 中一个对象是指一些选项的集合，它代表OpenGL状态的子集。

### GLFW

> GLFW is an Open Source, multi-platform library for OpenGL, OpenGL ES and Vulkan development on the desktop. It provides a simple API for creating windows, contexts and surfaces, receiving input and events.
> 
> 主要 生成窗口，支持OpenGL上下文，是API库函数

### GLAD

> 基于官方规格的多语言GL / GLES / EGL / GLX / WGL装载机 - 生成器。
一般结合GLFW使用。主要用于不同的硬件环境。是与硬件相关的驱动函数。

```c++
// 两者头文件的顺序
#include <glad/glad.h>
#include <GLFW/glfw3.h>
```

### GLEW

>因为OpenGL只是一个标准/规范，具体的实现是由驱动开发商针对特定显卡实现的。由于OpenGL驱动版本众多，它大多数函数的位置都无法在编译时确定下来，需要在运行时查询。任务就落在了开发者身上，开发者需要在运行时获取函数地址并将其保存在一个函数指针中供以后使用。取得地址的方法因平台而异。

GLEW是OpenGL Extension Wrangler Library的缩写。

### SOIL

存在的背景：
>纹理图像可能被储存为各种各样的格式，每种都有自己的数据结构和排列，所以我们如何才能把这些图像加载到应用中呢？一个解决方案是选一个需要的文件格式，比如.PNG，然后自己写一个图像加载器，把图像转化为字节序列。写自己的图像加载器虽然不难，但仍然挺麻烦的，而且如果要支持更多文件格式呢？你就不得不为每种你希望支持的格式写加载器了。

SOIL是简易OpenGL图像库(Simple OpenGL Image Library)的缩写，它支持大多数流行的图像格式，使用起来也很简单。

## 参考

- [opengl库区分](https://www.cnblogs.com/MakeView660/p/10488306.html)