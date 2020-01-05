---
title: pyplot
date: 2020-01-04 12:10:06
categories:
- MLDL
tags:
- MLDL
---

# pyplot

```python
import matplotlib.pyplot as plt
```

使用该库绘制图形

## 2. 矩阵/数组的可视化

`matshow()`

```python
import matplotlib.pyplot as plt
import numpy as np


def samplemat(dims):
    """Make a matrix with all zeros and increasing elements on the diagonal"""
    aa = np.zeros(dims)
    for i in range(min(dims)):
        aa[i, i] = i
    return aa


# Display matrix
plt.matshow(samplemat((15, 15)))

plt.show()
```