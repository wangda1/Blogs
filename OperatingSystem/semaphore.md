---
title: semaphore
date: 2019-11-08 19:09:36
categories:
- OperatingSystem
tags:
- OperatingSystem
---

# 进程同步之信号量实现  semaphore

信号量的提出---Dijkstra大神   
信号量分为  二进制信号量 与 计数信号量  
操作分为  P操作(waiting) 与 V操作(signal)


## 二进制信号量 mutex   

二进制信号量主要用于解决 互斥问题  
```
do {
    waiting(mutex);
    
    //critical section
    
    signal(mutex);
    
    //remainder section
    
}while(TRUE);
```

## 计数信号量 
结构  
```
typedef struct {
  int value;
  struct process *list;
} semaphore;
```
P,V操作的定义:
```
wait(semaphore *S) {
  S->value--;
  if(S->value < 0) {
  
    //add this process to S->list
    
    block();   
    }
}

signal(semaphore *S) {
  S->value ++ ;
  if(S->value <= 0) {
    
    //remove a P process from S->list
    
    wakeup(P);
    }
}
```
信号量的初值
> - 对于一般计数信号量初值一般设置为1
> - 对于同步问题处置一般设置为0 

说一下我的理解：  
wait(S)操作是用在访问与操作临界区之前，用于申请，或者说测试释放可用，执行-操作；  
signal(S)操作用于访问与操作临界区之后，对临界区访问权限的释放，或者说发送一个可用信号，执行+操作；

## Note 
**1.wait()signal()位置**   

为了防止出现死锁，一般将wait()与signal()放置在**紧贴**临界区的位置上  

**2.S->list的访问**  

**一般使用FIFO**以保证条件3即有限等待次数的实现，当使用其它的访问算法时，可能会违背条件3，**出现饥饿** 

**3.wait()signal()都属于原子操作**

当单cpu情况下可以用“关中”即**关闭中断**的方式来实现  
当多cpu情况下可以...emmm...反正记住PV都属于Atomic Operations :-) !!!



    
   
