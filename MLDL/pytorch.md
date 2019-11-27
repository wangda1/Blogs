<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>

# PyTorch

*参考：《深度学习入门之PyTorch》*

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

### 1.1 `torch.max()`

`torch.max()` 函数用于选出 tensor 中的最大值，用法如下：

```python

```

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

## 5. `torch.nn` Module

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

保存了固定字典和大小的简单查找表，该模块保存

- `num_embeddings` 嵌入字典的大小
- `embeddings_dim` 每个嵌入向量的大小

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