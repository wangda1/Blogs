---
title: Nginx
date: 2021-03-15 17:47:10
categories: Cloud Computing
tags: Nginx
---

# Nginx

## 功能

- 正向代理
- 反向代理
- 负载均衡
- 动静分离

## nginx 配置文件

1. `nginx` 配置文件的位置： `/usr/local/nginx/conf/nginx.conf`
2. `nginx` 配置文件的组成
    
    - 全局块： 从配置文件开始到 events 块之间的内容，主要会设置一些影响 nginx 服务器整体运行的配置指令，比如 `worker_process 1`，`worker_process` 值越大，可以支持的并发处理量越大
    - events块：events 块涉及的指令主要影响 nginx 服务器与用户的网络连接，比如 `worker_connections 1024`；支持的最大连接数
    - http 块： nginx 服务器配置中最频繁的部分，http 块也可以包括 http 全局块，server 块


## `nginx.conf` 相关字段

1. `http`
    -   `server`
        - `location`
            - `root`
            - `index`
            - `autoindex`
    -   `upstream`


## Nginx 配置实例 - 反向代理

## Nginx 配置实例 - 负载均衡

## Nginx 配置实例 - 动静分离

## Nginx 配置实例 - 高可用

高可用是采用主从模式的方式，结合 `keepalived` 虚拟 IP 实现高可用