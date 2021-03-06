---
title: MarkDown
date: 2020-01-02 09:30:31
categories:
- Something
tags:
- Something
---

# Markdown语法  

## 学习链接

[简书](http://www.jianshu.com/p/q81RER)
[Wow!Ubuntu](http://wowubuntu.com/markdown/#p)  感谢!

## Markdown优点:
- 纯文本，兼容性强
- 格式转换方便，可以轻松地转换为html,电子书等
- Markdown语法有极好的可读性

## 标题  

> \# 一级标题  
\## 二级标题  
\### 三级标题  

#可以有六级，表示六级标题

## 列表与引用

> \- 文本1  
\- 文本2  
\- 文本3

或者显示1,2,3的情况，使用:

> 1.文本1  
2.文本2  
3.文本3  

注意：**这些符号需在与后续文本之间加上一空格字符才能正确地显示**

## 换行

> - 当在一个文本块需要强制换行时，可以使用两个空格+换行符来强制换行，否则仅用一个换行符并不能起到换行的作用；
> - 恰当的使用空白行也能起到换行的作用；

## 粗体与斜体

> - 粗体：用2个*包含的内容，例如\*\*文本\*\*
> - 斜体：用1个*包含的内容，例如\*文本\*

## 反斜杠\

> 为什么我上面在引用里使用了一些符号但是却以文本的形式显示出来的呢？这得靠\的帮助，当你在文本中需要\#,\>,\-
等这些普通意义的符号时就只用在前面加上\就OK了

## 链接与图片

> - 插入链接：\[显示文本\](链接地址)  
> - 插入图片：\!\[\](图片链接地址)

## 表格

> - 用\|表示竖列对齐  
> - 用\-\-\-区分名称与数值  
> - 用\:表示左，右，中间对齐

*例如:*  

> \| Tables                     \| Are           \| Cool        \|  
> \| \-\-\-\-\-\-\-\-\-\-\-\-\- \|\:\-\-\-\-\-\: \| \-\-\-\-\-\:\|  
> \| col 3 is                   \| right-aligned \| $1600       \|  
> \| col 2 is                   \| centered      \|   $12       \|  
> \| zebra stripes              \| are neat      \|    $1       \|  

*显示效果：*  

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

## 代码引用

> - 单段代码引用：用  \'  包括整个代码段显示为一个代码段  
> - 多段代码引用：用  \'\'\'  置于代码段的首行与末行

## 编写数学公式

*参考：https://juejin.im/post/5a6721bd518825733201c4a2#heading-1*

数学公式的编写类似于 Latex 中的用法，这里介绍一些常用的：

- `$$\left(\sum_{k=\frac{1}{2}}^{N^2}\frac{1}{k}\right)$$`

$$\left(\sum_{k=\frac{1}{2}}^{N^2}\frac{1}{k}\right)$$

- `$$\left(\int_a^b\sqrt{2x}dx\right)$$`

$$\left[\int_a^b\sqrt{2x}dx\right]$$

```
$$\begin{bmatrix}
    1 & 2 \\\\
    3 & 4
\end{bmatrix}$$
```

$$\begin{bmatrix}
    1 & 2 \\\\
    3 & 4
\end{bmatrix}$$

- 数学公式中的空格

markdown 中数学公式中的空格

```markdown
没有空格 $ab$
小空格 a\,b
中等空格 a\;b
大空格 a\ b
quad空格 $a\quad b$
qquad空格 $a\qquad b$
```

没有空格 $ab$  
小空格 $a\,b$  
中等空格 $a\;b$  
大空格 $a\ b$  
quad空格 $a\quad b$  
qquad空格 $a\qquad b$

- 数学公式的换行

使用 `\\` 或 `\\` 进行数学公式的换行，使用在 `\begin \end` 块中，见以下示例。

- 数学公式的对齐

使用 `aligned` + `&`

```markdown
$$
\begin{aligned}
r_{t} =& \sigma(W_{ir}x_{t} + b_{ir} + W_{hr}h_{(t-1)} + b_{hr}) \\
z_{t} =& \sigma(W_{iz}x_{t} + b_{iz} + W_{hz}h_{(t-1)} + b_{hz}) \\
n_{t} =& tanh(W_{in}x_{t} + b_{in} + r_{t}*(W_{hn}h_{(t-1)} + b_{hn})) \\
h_{t} =& (1-z_{t}) * n_{t} + z_{t} * h_{(t-1)}        
\end{aligned}
$$
```

$$
\begin{aligned}
r_{t} =& \sigma(W_{ir}x_{t} + b_{ir} + W_{hr}h_{(t-1)} + b_{hr}) \\
z_{t} =& \sigma(W_{iz}x_{t} + b_{iz} + W_{hz}h_{(t-1)} + b_{hz}) \\
n_{t} =& tanh(W_{in}x_{t} + b_{in} + r_{t}*(W_{hn}h_{(t-1)} + b_{hn})) \\
h_{t} =& (1-z_{t}) * n_{t} + z_{t} * h_{(t-1)}        
\end{aligned}
$$

