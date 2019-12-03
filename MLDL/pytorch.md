<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

# PyTorch

*参考：《深度学习入门之PyTorch》*

## 0. 基本数据类型

### 0.1 数据类型

`torch.Tensor` 默认是 `torch.FloatTensor`

| Data tyoe	            | CPU tensor | GPU tensor |
|-----------------------|------------|------------|
| 32-bit floating point |torch.FloatTensor  |torch.cuda.FloatTensor
| 64-bit floating point |torch.DoubleTensor	|torch.cuda.DoubleTensor
|16-bit floating point  |N/A               |torch.cuda.HalfTensor
|8-bit integer (unsigned)|	torch.ByteTensor|	torch.cuda.ByteTensor
|8-bit integer (signed)	|torch.CharTensor	  |torch.cuda.CharTensor
|16-bit integer (signed) |torch.ShortTensor	|torch.cuda.ShortTensor
|32-bit integer (signed) |torch.IntTensor	  |torch.cuda.IntTensor
|64-bit integer (signed) |torch.LongTensor	|torch.cuda.LongTensor

### 0.2 对 `torch.Tensor` 的操作方法

- `tensor`可以由python中的 `list` 或序列创建
- 也可以用python中的切片与索引来修改 `tensor` 中的内容
- 会改变 `tensor` 的函数操作会带有下划线表示，例如：`abs_()`等

`torch.max()` 函数用于选出 tensor 中的最大值，用法如下：

### 0.3 变换数据维度

这里涉及到的总共有 3 种方法：

*参考：https://zhuanlan.zhihu.com/p/76583143*

- `Tensor.permute(a, b, c...)` 可以直接对高纬度矩阵进行转置操作
- `torch.transpose()` 与 `permute()`作用相同，但只能操作两个维度
- `Tensor.view()`; `view()` 仅能作用在连续的内存中，如果在调用了 `transpose()` 或 `permute()` 则可导致内存不连续，需要使用 `contiguous()`返回一个连续的内存拷贝；
- `torch.reshape()` *version >=0.4*, `== tensor.contiguous().view()`

```python
import torch
import numpy as np

a=np.array([[[1,2,3],[4,5,6]]])
unpermuted=torch.tensor(a)
print(unpermuted.size())              #  ——>  torch.Size([1, 2, 3])

permuted=unpermuted.permute(2,0,1)
print(permuted.size())                #  ——>  torch.Size([3, 1, 2])
print(permuted.is_contiguous())       # False

view_test = unpermuted.view(1,3,2)
print(view_test.size())               #  ——>  torch.Size([1, 3, 2])
```

### 0.4 数据拼接 

- `torch.cat(tensors, dim=0, out=None) → Tensor`，在指定维度上进行数据的拼接，如当`dim=0`时，在第0维度进行扩展

```python
>>> x = torch.randn(2, 3)
>>> x
tensor([[ 0.6580, -1.0969, -0.4614],
        [-0.1034, -0.5790,  0.1497]])
>>> torch.cat((x, x, x), 0)
tensor([[ 0.6580, -1.0969, -0.4614],
        [-0.1034, -0.5790,  0.1497],
        [ 0.6580, -1.0969, -0.4614],
        [-0.1034, -0.5790,  0.1497],
        [ 0.6580, -1.0969, -0.4614],
        [-0.1034, -0.5790,  0.1497]])
>>> torch.cat((x, x, x), 1)
tensor([[ 0.6580, -1.0969, -0.4614,  0.6580, -1.0969, -0.4614,  0.6580,
         -1.0969, -0.4614],
        [-0.1034, -0.5790,  0.1497, -0.1034, -0.5790,  0.1497, -0.1034,
         -0.5790,  0.1497]])
```

### 0.5 数据压栈

- `torch.stack(tensors, dim=0, out=None) → Tensor`

`torch.stack()` 要求不同的 `tensor` 之间是相同的维度，它的作用与转置的作用类似，不同的是 `torch.stack()` 作用于不同的 `tensor`，通过指定 `dim` 去除相应维度的数据进行组合成新的维度，也就是 `stack`。

```python
a = torch.IntTensor([[1, 2, 3]])
b = torch.IntTensor([[4, 5, 6]])

d0 = torch.stack([a, b], dim=0)
d1 = torch.stack([a, b], dim=1)
d2 = torch.stack([a, b], dim=2)
```

### 0.6 数据压缩

- `tensor.squeeze()`
- `tensor.unsqueeze()`

压缩的维度为元素个数为 1 的维度，如：

```python
a = torch.randn(2,1)
a.size()                # [2, 1]
a.squeeze().size()      # [2]
```

## 1. Variable(变量)

> Variable 是神经网络计算图里的概念，提供了自动求导的功能。Variable 和 Tensor 本质上没有区别，不过 Variable 会被放入一个计算图中，然后进行前向传播、反向传播、自动求导。

位置： `torch.autograd.Variable`

```python
x = Variable(torch.Tensor([1]))
w = Variable(torch.Tensor([2]))
b = Variable(torch.Tensor([3]))

y = w * x + b

y.backward()

pritn(x.grad)
```

### 1.1 Parameters

`class torch.nn.Parameter()`

`Variable` 的一种，常被用于模块参数 `module parameter`

`Variable` 与 `Parameter`  的不同：

- `Parameters` 是 `Variable` 的子类。 当把 `Parameters` 赋值给 `Modules`的时候，会被自动加到 `Module` 的参数列表中（会出现在 `parameters()` 迭代器中）。将 `Variable` 赋值给 `Module` 属性则不会有这样的影响。
- `Parameter` 不能被 `volatile`，且默认 `requires_grad=True`，`Variable`默认`requires_grad=False`

## 2. Dataset(数据集)

## 3. 激励函数

```python
import torch
import torch.nn.functional as F

x = torch.linspace(-5, 5, 200)
y_relu = torch.relu(x)
print(y_relu)
y_sigmoid = torch.sigmoid(x)
print(y_sigmoid)
y_tanh = torch.tanh(x)
print(y_tanh)
y_softplus = F.softplus(x)
print(y_softplus)
```

## 4. Commonly used function

- `torch.view()` 类似于 `numpy.reshape()` 但不同的是，`view()` 函数并不进行变量内存的复制，而只是在原来的内存区域进行操作。
- `torch.Tensor()`
- `torch.LongTensor()`
- `torch.optim.SGD()`

## 5. Containers（容器） `torch.nn` Module

### 5.1 `nn.Linear(in_features, out_features, bias=True)`

- `in_features` 每个输入样本的大小
- `out_features` 每个输出样本的大小
  
$$y=Ax+b$$

### 5.2 `nn.Dropout(p=0.5, inplace=False)`

- `p` 将元素置0的概率
- `inplace` 若设置为 True，会在原地进行操作

### 5.3 `nn.ReLU(inplace=False)`

$$
y=\begin{cases}
0, \quad x\leq0 \\\\
x, \quad x>0
\end{cases}
$$

### 5.4 `nn.Embedding(num_embeddings, embedding_dim, padding_idx=None, max_norm=None, norm_type=2, scale_grad_by_freq=False, sparse=False)`

保存了固定字典和大小的简单查找表，该模块保存，这里只是初始化的一些向量，后续还需要进行学习和修改

- `num_embeddings` 嵌入字典的大小
- `embeddings_dim` 每个嵌入向量的大小

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable

word_to_idx = {'hello': 0 ,'world': 1}
embeds = nn.Embedding(2, 5)
hello_idx = torch.LongTensor([word_to_idx['hello']])
hello_variable = Variable(hello_idx)
hello_embed = embeds(hello_variable)
print(hello_embed)

embeds.weight.data = torch.ones(2, 5)   # embeddings 的 weight 可以设置 
print(embeds.weight)
```

### 5.5 `nn.Sequential(*args)`

一个时序容器。 `Modules` 会以他们传入的顺序被添加到容器中。

```python
# Example of using Sequential

model = nn.Sequential(
          nn.Conv2d(1,20,5),
          nn.ReLU(),
          nn.Conv2d(20,64,5),
          nn.ReLU()
        )
# Example of using Sequential with OrderedDict
model = nn.Sequential(OrderedDict([
          ('conv1', nn.Conv2d(1,20,5)),
          ('relu1', nn.ReLU()),
          ('conv2', nn.Conv2d(20,64,5)),
          ('relu2', nn.ReLU())
        ]))
```

### 5.6 `nn.CrossEntropyLoss(weight=None, size_average=True)`

$$loss(x,class) = -log{\frac{exp(x[class])}{\sum_{j}exp(x[j])}}$$

### 5.7 `nn.RNN()` 与 `nn.LSTM()` 中已经讲过参考 [RNN](./RNN.md)

## 6. `torch.optim`

`torch.optim` 是一个实现了各种优化算法的库。

### 6.1 如何使用 `optimizer`

为了使用 `torch.optim`，你需要构建一个 optimizer 对象，这个对象能够保持当前参数状态并基于计算得到的梯度进行参数更新。

- 构建

为了构建一个 `optimizer`，需要传入一个包含优化参数（必须都是 `Variable` 对象）的 iterable，并设置 optimizer 的参数选项，如：学习率、权重衰减等。

```python
optimizer = optim.SGD(model.parameters(), lr=0.01, )
```

- 进行单次优化

采用的方法：

`optimizer.step()` 这个方法会更新所有的参数，所有的 optimizer 都实现了这个方法，一旦梯度被 `backward()` 之类的函数计算好后，就可以调用这个函数。

```python
# 单次优化的常用做法
for input, target in dataset:
    optimizer.zero_grad()
    output = model(input)
    loss = loss_fn(output, target)
    loss.backward()
    optimizer.step()
```

### 6.2 常用函数

- `step(closure)` 进行单次优化
- `zero_grad()` 清空所有被优化过的 Variable 的梯度

## 7. 参考

- [PyTorch-官方教程](https://pytorch-cn.readthedocs.io/zh/latest/package_references/torch-optim/)
- [pytorch-文档](https://pytorch.org/docs/stable/torch.html)