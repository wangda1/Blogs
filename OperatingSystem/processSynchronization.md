#  进程同步的一些算法  
这些算法主要用于解决**临界区问题**  
所谓临界区，即对共享数据访问与操作的代码，主要要求是最多只有一个进程在临界区内  

临界区问题的解答需要满足以下三点需求：  
> - 互斥(mutual exclusion)
> - 前进“空闲可进”(progress)  
> - 有限等待(bounded waiting)

下面是软件实现的几种算法： 

## Peterson算法（仅限于2个进程） 
**采用共享数据 turn,flag 来实现 预约与轮转 的算法**
```
do {
    flag[i] = TRUE;           //flag[i]=TRUE 表示i想进入临界区
    turn = j;                 //turn 表示哪一个 可以进入临界区
    while(flag[j]&&turn == j);
    
    临界区  
    
    flag[i] = FALSE;
     
    剩余区  
    
    }while(TRUE);
```
注解：
> - 当若只包含turn则只能满足条件1，互斥进入，存在问题2，有空闲不让进情况  
> - flag 主要用于解决条件2，让想进入临界区的有限次等待可以进入
    
## 面包店算法 （可用于n个进程）
**类似面包店取号**
> - choosing = TRUE 表示开始取号
> - number[i]  表示取得的号码  
> - number最小的进入临界区
> - (number[j],j)<(number[i],i) 若number[j]<number[i]则返回1；若number[j]==number[i]&&j<i则返回1
```
do {
    choosing[i] = TRUE;                                           //开始取号码
    number[i] = MAX{number[0],number[1]...number[i-1]} + 1；      //取号码
    choosing[i] = FALSE;                                          //取号结束
     
    for(j=0;j<i;j++) {
      while(choosing[j]);                                         //碰到有正在取号的则等待，若无choosing，还是会出现一些问题
      while((number[j] != 0)&&((number[j],j)<(number[i],i)));     //碰到比自己号码小的想要进入的则等待
      }
     
     临界区  
     
     number[i] = 0;                                               //重新置号
     
     剩余区  
     
}while(TRUE);
```

下面是一些总结： **预约+互斥**   
两者相同点：
> - 存在一个预约机制(flag & number)，即保证条件3能够满足
> - 在对共享数据进行操作时都特别小心(flag,number[n])因为临界区问题的源头在这里 
> - 在进入临界区检查时，都用while()检查其它进程有没有满足条件，若有，空操作；若无，进入；（进程之间应该谦让）
> - 出了临界区之后，立即对自己的预约进行消除(flag[i] = FALSE,number[i] = 0)

两者不同点：
> - 互斥的实现：前者通过turn，后者通过number的大小比较来实现
  
    
    
    
    
 
