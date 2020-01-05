---
title: Question_in_stackoverflow
date: 2019-08-26 11:28:11
categories:
- Python
- gc
tags:
- Python
- gc
---

**Background truths(?):** When python program exits, `gc`(`garbage collection`) works to collect memory in a common way `reference counting`.

**Question:** but what's the order of objects' destructing or similar with `java`?

Pls see code below. The reference relationship is:(`-->` means reference)  

- ABC `-->` A 
- ABC `-->` B 
- A `-->` C      

And I could understand **the construct order is abc, a, c, b**, but why the destruct order is c, a, b, abc. **c** has the most reference, why firstly deleted.

python version 3.7.1

```python
class A():
    def __init__(self):
        self.name = 'little a'
        print(self.name)
        self._c = C() 
    def __del__(self):
        print('little a was deleted')

class B():
    def __init__(self):
        self.name = 'little b'
        print(self.name)
    def __del__(self):
        print('little b was deleted')

class C():
    def __init__(self):
        self.name = 'little c'
        print(self.name)
    def __del__(self):
        print('little c was deleted')

class ABC():
    def __init__(self):
        self.name = 'little abc'
        print(self.name)
    def get_ABC(self):
        self._a = A()
        self._b = B()
    def __del__(self):
        print('little abc was deleted')

if __name__ == '__main__':
    abc = ABC()
    abc.get_ABC()
    print(sys.getrefcount(abc._a))
    print(sys.getrefcount(abc._b))
```