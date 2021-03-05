---
title: pytorch(2)
date: 2020-01-04 11:55:23
categories:
- MLDL
tags:
- MLDL
---

# pytorch (二)

## 1. `Variable` `Tensor` `numpy` 之间的转换

**Variable 已经被 depreciate 了！！！**
```python
>>> from torch.autograd import Variable
>>> import torch

# numpy --> tensor
>>> tensor_variable = torch.from_numpy(numpy_variable)

# tensor --> numpy
>>> numpy_variable = tensor_variable.numpy()

# numpy -- > Tensor --> Variavle
>>> v = Variable(torch.from_numpy(numpy_variable))

# Variable --> numpy
>>> numpy_variable = v.data.numpy()
```

## 2. `tensor.new()`

*[source](https://pytorch.org/docs/0.3.1/tensors.html?highlight=new#torch.Tensor.new)*

`new(*args, **kwargs)`

Constructs a new tensor of the same data type as self tensor.

> For CUDA tensors, this method will create new tensor on the same device as this tensor.

```python
>>> input = (input.data.new([word2ix[w]])).view(1, 1)
>>> h_0 = input.data.new(2, batch_size, self.hidden_dim).fill_(0).float()
>>> c_0 = input.data.new(2, batch_size, self.hidden_dim).fill_(0).float()
```

## 3. `cuda` 上 `tensor` 的定义

```python
>>> a = torch.one(1000, 1000, 3).cuda()     # 在 cpu 上定义，将数据转移到 cuda 上
>>> torch.zeros().cuda()

# 在某一GPU设备上定义
>>> cuda1 = torch.deivce('cuda:1')
>>> b = torch.randn((1000, 1000, 1000), device=cuda1)

# 直接在 GPU上定义数据，减少cpu的损耗
>>> torch.cuda.FloatTensor(batch_size, self.hidden_dim, self.height, self.width).fill_(0)
```