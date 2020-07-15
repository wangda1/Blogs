---
title: list（链表） 相关问题
date: 2020-06-24 11:21:00
categories:
- Algorithm
tags:
- Algorithm
---

# list

## list的构造与增删改查

## leetcode题目

1. 141 Linked List Cycle
2. 142

#get all .c files
SrcFiles=$(wildcard *.c)
#all .c files --> .o files
ObjFiles=$(patsubst %.c,%.o,$(SrcFiles))

all:app

app:$(ObjFiles)
    gcc -o $@ -I./include $(ObjFiles)
#模式匹配规则，$@，$< 这样的变量，只能在规则中推导
%.o:%.c
    gcc -c $< -I ./include

test:
    @echo $(SrcFiles)
    @echo $(ObjFiles)

#定义伪目标，防止有歧义
.PHONY:clean all
clean:
    -@rm -f *.o
    -@rm -f app
