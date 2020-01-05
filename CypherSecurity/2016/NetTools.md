---
title: NetTools
date: 2019-11-08 19:09:36
categories:
- CypherSecurity
- 2016
tags:
- CypherSecurity
- 2016
---

# 一些网络工具的使用

## dnsenum  
多线程perl脚本枚举域的DNS信息并发现非连续的IP段工具  

主要功能:  
> - 获取主机的地址（A记录）
> - 获取名称服务器（线程）
> - 获取MX记录（线程化）
> - 对名称服务器执行axfr查询并获取BIND VERSION（线程化）
> - 通过Google抓取获取额外的名称和子域(google query = “allinurl: -www site:domain”)
> - 读取文件爆破子域，也可以对具有NS记录的子域执行递归查询（开启所有线程）
> - 计算C类域网络范围并对其执行whois查询（线程化）
> - 对网络（C类或/和whois网络）执行反向查找（线程化）
> - 将ip段写入domain_ips.txt文件
