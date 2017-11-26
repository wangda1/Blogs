# typedef及一些复杂的声明   

今天在做微机原理实验时，看了一些API的声明，被里面的一些函数的声明搞得有点头晕了，哎呀！我个C语言的渣。慌得我赶紧补了一发！


## typedef 与 #define  

> - 与 #define 不同，typedef给出的符号名称仅限于对类型，而不是对值；   
> - typedef的解释由编译器，而不是由预处理器；  
> - 但在有限的范围内,typedef 比 #define 灵活。

经典用法：  
typedef unsigned char byte;  
# define byte unsigned char;  同  

但是，  
typedef char * STRING；
# define STRING char *     

前者,STRING name,sign 表示 char * name, * sign;  
后者,STRING name,sign 表示 char * name,sign;    


**另一个不可告人的原因是：**     
typedef 常用于 复杂类型      

来来来，这个告诉我是啥？  ** typedef char (* FRPTC()) [5] **    

表示函数返回一个指向5个元素的char数组的指针；   
** typedef char * FRPTC() [5] **     
表示函数返回一个含有5个指向char的指针的数组；   

## C的奇特的声明


char * fump ();       //返回指向 char 的指针的函数；    
char (* fump) ();     //指向返回类型为char 的函数的指针；   
char (* flump[3])();  //由3个指针组成的数组，每个指针指向返回类型为char的函数；   

注：(),[]的优先级相同，高于 * 的优先级

**鄙人认为这些奇特的声明的辨认就严格按照优先级顺序进行结合**
