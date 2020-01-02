# tqdm

tqdm 是快速，可扩展的 python 进度条，用户只需要封装任意的迭代器 `tqdm(iterator)`

## 1. 基本用法

```python
import time
from tqdm import tqdm

for i in tqdm(range(100)):
    time.sleep(0.01)
```

## 参考

- [csdn](https://blog.csdn.net/qq_33472765/article/details/82940843)