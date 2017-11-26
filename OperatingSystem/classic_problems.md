# 经典同步问题  

抄一下代码，想一下idea

## Producer-Consumer problem（生产者-消费者问题）  
又名有界缓冲区问题  

原则：  
- 缓冲区有界  
- 同步，互斥读写  

解决方式：  
- semaphore mutex 初值为1，互斥信号量  
- semaphore full,empty full初值为0，empty初值为n，计数信号量  

**备注：**解决互斥问题并不是Dijkstra大神的初心，毕竟这用“关中”也可以实现，这带来的还有避免了空操作；  

实现：  
```
Producer:
do {

  //produce product
  
  wait(empty);
  wait(mutex);
  
  //add product into buffer
  
  signal(mutex);
  signal(full);
  
}while(TRUE);

Consumer:
do {
  wait(full);
  wait(mutex);
  
  //remove product from buffer
  
  signal(mutex);
  signal(empty);
  
  //consume product
  
}
```

## Readers-Writers Problem（读者-写者问题）

原则：  
- 多进程可同时读，单进程可写  
- 读写进程互斥  
- 避免出现读/写进程饥饿  

解决方式：  
- semaphore mutex,wrt 初值为1，mutex保护readercount，wrt保护共享数据  
- int readercount 初值为0，表示读进程个数  

实现：   
```
Writer:
do { 
  wait(wrt);
  
  //writing is performed  
  
  signal(wrt);
}while(TRUE);

Reader:
do {
  wait(mutex);
  readercount ++;
  if(readercount == 1)          //当是第一个要读的进程时申请wrt；若非第一个读的，直接进入
    wait(wrt);
  signal(mutex);
  
  //reading is performed
  
  wait(mutex);
  readercount --;
  if(readercount == 0)          //当是最后一个要离开的进程时释放wrt；若非最后一个，直接离开
    signal(wrt);
  signal(mutex);
}while(TRUE);
```
**当然了，这并没有解决饥饿问题(starvation)，很明显会造成Writer进程饥饿**  




  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
