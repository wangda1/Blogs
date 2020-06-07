---
title: Latex 入门
date: 2020-01-02 09:30:31
categories:
- Something
tags:
- Something
---

# Latex

## 线下环境

- TeXlive+TeXstuido

## 线上环境

- [overleaf](https://www.overleaf.com/)

## 基本格式

```latex
\begin{document}
\section{text}
\subsection{text}
\end{document}
```

- 斜体`\textit{text}`
- 加粗`\textbf{text}`
- 角标`\textsuperscript`
- 换行`\newline` 或 `\\`

## 新建列表

```latex
\begin{itemize}
\item
\item
\end{itemize}
```

## 插入表格

```latex
\begin{table}[htbp]
\caption{spacy NER Accuracy Table\textsuperscript{\cite{b3}}}
\begin{center}
\begin{tabular}{|c|c|c|}
\hline
\textbf{F}&\textbf{P}&\textbf{R} \\
\hline
85.55&85.89&85.21  \\
\hline
\end{tabular}
\label{tab1}
\end{center}
\end{table}
```

## 插入图片

```latex
\begin{figure}[htbp]
\includegraphics[scale=0.6]{figure/entity_top5.png}
\caption{Top 5 entities in multiple categories.}
\label{fig}
\end{figure}
```

## Reference

文本中的引用

`text\cite{bn}`

Reference 的列表

```latex
\begin{thebibliography}{00}
\bibitem{b1}
\bibitem{b2}
\bibitem{b3}
\end{thebibliography}
```

## 参考

- [Latex环境配置](https://www.jianshu.com/p/3e842d67ada2)
- [latex插入表格](https://blog.csdn.net/JueChenYi/article/details/77116011)
- [latex插入图片](https://zhuanlan.zhihu.com/p/32925549)
- [常用Latex参考](https://blog.csdn.net/Gentleman_Qin/article/details/79963396)