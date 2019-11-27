# Tensorflow

## 1. Tensorflow 模型文件

```
|--checkpoint_dir
|    |--checkpoint                  # 文本文件，记录最新的checkpoint文件及其它checkpoint文件的列表
|    |--MyModel.meta                # 保存图结构，meta文件是pb文件，包含变量、op、集合等
|    |--MyModel.data-00000-of-00001 # 二进制文件，保存了所有的 weights、biases、gradients等变量
|    |--MyModel.index               # 二进制文件和上述文件的作用相同
```


