---
title: DNS
date: 2019-11-08 19:09:36
categories:
- CypherSecurity
- 2016
tags:
- CypherSecurity
- 2016
---

# DNS查询  

## DNS域名解析记录  

**记录**  

1.A记录：解析IPv4地址记录  
2.AAAA记录： 解析IPv6地址记录  
3.CNAME记录： 解析别名记录  
4.NS记录： 解析子域名指定DNS服务器记录  
5.MX记录： 解析SMTP服务器记录

## 解析  

1.正向解析: 查询A记录

2.反向解析: 查询PTR记录  
  完成逆向域名解析，系统提供一个特别域，该特别域称为逆向解析域in-addr.arpa。这样欲解析的IP地址就会被表达成一种像域名一样的可显示串形式，后缀以逆向解析域域名"in-addr.arpa"结尾

## 工具  

dnsenum 可用于DNS的多项查询  

