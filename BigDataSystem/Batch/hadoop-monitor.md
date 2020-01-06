---
title: Hadoop 监控
date: 2020-1-06 10:51
categories:
- BigDataSystem
- Batch
tags:
- BigDataSystem
- Batch
---

# Hadoop 监控

## 1. 网页查看集群的状态

### 1.1 `hdfs`的集群状态

- 配置： `hdfs-site.xml--dfs.namenode.http-address`
- 访问地址： `http://namenode-ip:50070`

### 1.2 `secondary namenode`　的集群状态

- 配置： `hdfs-site.xml--dfs.namenode.secondary.http-address`
- 访问地址： `http://namenode-ip:50090`

### 1.3 `yarn`的集群状态

- 配置： `yarn-site.xml--yarn.resourcemanager.webapp.address`
- 访问地址： `http://resource-manager-ip:8088`