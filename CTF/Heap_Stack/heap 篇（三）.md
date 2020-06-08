---
title: Heap 篇（三 ）
date: 2018-05-07 16:59:00
categories:
- CTF
- Heap_Stack
tags:
- CTF
- Heap_Stack
---

# heap 篇（三）

- malloc申请内存与pymalloc实际分配内存的计算公式：

```
/* pad request bytes into a usable size -- internal version */
//MALLOC_ALIGN_MASK = 2 * SIZE_SZ -1
#define request2size(req)                                                      \
    (((req) + SIZE_SZ + MALLOC_ALIGN_MASK < MINSIZE)                           \
         ? MINSIZE                                                             \
         : ((req) + SIZE_SZ + MALLOC_ALIGN_MASK) & ~MALLOC_ALIGN_MASK)
```

- 最小Chunk大小为 2 \* 字长
- Chunk大小以 2 \* 字长对齐