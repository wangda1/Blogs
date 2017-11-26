# Makefile

Makefile 文件是  make  的规则文件，是一种 build 脚本，里面阐明了编译链接的顺序及所需要的相关文件

## 概述

命令规则：  
```
target:prerequisites
  command
```
target 为目标文件，prerequisites为依赖文件，commmand为要执行的shell命令**前面要以TAB键开头**      
并默认第一个目标文件为最终要生成的目标文件，然后后续的过程就是以这个文件为根，进行依赖文件展开，检查时间戳，执行规则  

时间戳：这里指的是 make  可以在编译过程中依据文件的更新程度来决定哪些文件需要重新编译，哪些文件需要重新链接生成

```
   edit : main.o kbd.o command.o display.o \
          insert.o search.o files.o utils.o
           cc -o edit main.o kbd.o command.o display.o \
                      insert.o search.o files.o utils.o
 
   main.o : main.c defs.h
           cc -c main.c
   kbd.o : kbd.c defs.h command.h
           cc -c kbd.c
   command.o : command.c defs.h command.h
           cc -c command.c
   display.o : display.c defs.h buffer.h
           cc -c display.c
   insert.o : insert.c defs.h buffer.h
           cc -c insert.c
   search.o : search.c defs.h buffer.h
           cc -c search.c
   files.o : files.c defs.h buffer.h command.h
           cc -c files.c
   utils.o : utils.c defs.h
           cc -c utils.c
   clean :
           rm edit main.o kbd.o command.o display.o \
              insert.o search.o files.o utils.o   
```
以此makefile文件为例，若command.c发生改变，只需重新编译生成新的中间代码文件command.o，再重新进行链接     
但如果 defs.h  文件发生改变，则全部.o文件都需要重新编译，重新链接

## 变量

当然了上述.o文件一大堆，可以用一个变量名来代替，引用变量用  $(object) 或者  ${object}

上面可以修改成
```
   objects = main.o kbd.o command.o display.o \
             insert.osearch.o files.o utils.o 
   edit : $(objects)
           cc -o edit $(objects)
   main.o : main.c defs.h
           cc -c main.c
   kbd.o : kbd.c defs.h command.h
           cc -c kbd.c
   command.o : command.c defs.h command.h
           cc -c command.c
   display.o : display.c defs.h buffer.h
           cc -c display.c
   insert.o : insert.c defs.h buffer.h
           cc -c insert.c
   search.o : search.c defs.h buffer.h
           cc -c search.c
   files.o : files.c defs.h buffer.h command.h
           cc -c files.c
   utils.o : utils.c defs.h
           cc -c utils.c
   clean :
           rm edit $(objects)
```



## 自动推导

```
只要make看到一个[.o]文件，它就会自动的把[.c]文件加在依赖关系中，如果make找到一个whatever.o，那么whatever.c，就会是whatever.o的依赖文件。
并且 cc -c whatever.c 也会被推导出来
```
画风就变成了酱紫  
```
   objects = main.o kbd.o command.o display.o \
             insert.o search.o files.o utils.o
 
   edit : $(objects)
           cc -o edit $(objects)
 
   main.o : defs.h
   kbd.o : defs.h command.h
   command.o : defs.h command.h
   display.o : defs.h buffer.h
   insert.o : defs.h buffer.h
   search.o : defs.h buffer.h
   files.o : defs.h buffer.h command.h
   utils.o : defs.h
 
   .PHONY : clean
   clean :
           rm edit $(objects)       
 ```




















