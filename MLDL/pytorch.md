

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