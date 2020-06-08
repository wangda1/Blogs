---
title: UNLINK
date: 2018-05-11 11:06:00
categories:
- CTF
- Heap_Stack
tags:
- CTF
- Heap_Stack
---

# UNLINK

**unlink 中的很重要的一点就是合并**

- <font color="#FF0000">常用的两道检查（这里以后向合并为例，一般构造为后向合并）</font>

1. <font color="#7600D8"><span style="font-size: 19px;">判断两个块的 size 是否正常（即：size 未经修改）</span></font>

<font color="#FF0000">（这里的P是指 需要 unlink的 P，也就是 目前在 bins中的 P）</font>

```
    // 由于P已经在双向链表中，所以有两个地方记录其大小，所以检查一下其大小是否一致。
    if (__builtin_expect (chunksize(P) != prev_size (next_chunk(P)), 0))      \
      malloc_printerr ("corrupted size vs. prev_size");               \
```

```
2. 判断指针是否连接正确（即：指针未经修改）
```

```
(这里的P也是要 unlink 也就是在 bins中的 P)
```

```
// fd bkif (__builtin_expect (FD->bk != P || BK->fd != P, 0))                      \
```

```
  malloc_printerr (check_action, "corrupted double-linked list", P, AV);  \
```

- <font color="#7600D8"> 下面图来看</font>
- <font color="#7600D8">当我们时，若进行后向合并</font><font color="#FF0000">（合并低地址）</font><font color="#7600D8">则 进行的操作为：</font>

1. <font color="#FF0000">BK = P -> bk</font>
2. <font color="#FF0000">FD = P ->fd</font>
3. <font color="#FF0000">FD -> bk = BK</font> <font color="#7600D8">（ptr - 0x10(64bits)）</font>
4. <font color="#FF0000">BK -> fd = FD  </font> <font color="#7600D8"> (ptr - 0x18(64bits))</font>

- <font color="#FF0000">unlink之后的ptr 的内容修改为 ptr - 0x18!!!!至此任务完成</font>

<font color="#FF0000"><span style="font-size: 19px;"><br></span></font>

<font color="#FF0000"><span style="font-size: 19px;"><br></span></font>

<font color="#FF0000"><span style="font-size: 19px;">小结：完成unlink需要：先free出两个 chunk ，然后再把 构造 chunk 内容，然后 free 中间指针完成 unlink</span></font>
<font size="4"><br></font>