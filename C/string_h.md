---
title: string_h
date: 2019-11-08 19:09:35
categories:
- C
tags:
- C
---

# string.h vs string


string.h C的头文件，无string类，有strcpy()函数  
cstring 这个完全是string.h的C++版本只不过多了std的命名空间，也就是必须用 std::strcpy()
string C++新生头文件，与string.h无半毛钱关系，亲儿子  

## string.h  
C 的头文件  
- **无string类型的定义**  
  想定义个字符串，char string[] = "string";  char *string = "string";
  
- **常用的字符串操作函数**  
  `int strcmp(char * str1,char * str2);`  
  这个返回值比较有意思，按照字符ASCII码，若str1 < str2,返回负数；同理  
  
  
  `unsigned int strlen(char * str);` 注意：统计字符个数不包括\0  
  
  
  `void *memset(void *s, int c, size_t n);`   
  
  
  
## string 
C++ 亲生儿子，属于STL  
- **string类出现**


- **重载了操作符**



## Note  
1.其实iostream.h也是C的头文件，C++里面使用iostream就必须使用命名空间了，与此类似，当用一些C里面的函数时：  
  eg:   
  - math.h 可以直接使用里面的函数，不用管命名空间  
  - cmath  必须申明命名空间来使用头文件里的一些函数  



  
