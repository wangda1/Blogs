---
title: GoogleExplore
date: 2019-11-08 19:09:36
categories:
- Something
tags:
- Something
---

# Google精确搜索，提高查询效率  

[xuanhun](http://www.cnblogs.com/xuanhun/p/3910134.html)  感谢!

这些搜索引擎的搜索技术来源于传统数据库的检索技术  

## 精确搜索

> - Google默认模糊搜索  
> - "xxxxx"可进行精确搜索    
> - 通配符*可用于代替关键词  
> - 点号 . 可用于匹配任意字符  

## 约束条件

> - " + "用于强制搜索，即 + 前后的内容都必须包含;常和精确搜索 " " 一起来用  

## Bool逻辑

> - Google默认多个词间关系为逻辑与  
> - 当使用逻辑算符时，词语逻辑算符用空格分开  
> - 复杂的逻辑关系可以用\(\)来分组 
> - 当运用非逻辑时，"搜索 -内容"格式

## 数字范围  

> - " .. "表示一个数字范围

## 标题中搜索

> - 语法: intitle 或 allintitle  
> - 示例: intitle:"WSO 2.4" [ Sec. Info ], [ Files ], 
[ Console ], [ Sql ], [ Php ], [ Safe mode ], [ String tools ], [ Bruteforce ], [ Network ], [ Self remove ]

##  正文中搜索

> - 语法: intext 或 allintext  
> - 示例: intitle:"index" intext:"Login to the Administrative Interface"

## 网址中搜索

> - 语法: inurl  
> - 示例: inurl:phpmyadmin/index.php & (intext:username & password & "Welcome to")  

## 锚点链接搜索

> - 语法: inanchor 或 allinanchor  
> - 示例: inanchor:修改密码   

















