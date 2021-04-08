---
title: VPS 选用指南
date: 2021-04-07 09:30:31
categories:
- Something
tags:
- Something
---

# VPS 选用指南

## 购买

可以去 VPSGO(https://www.vpsgo.com/) 参考比较优惠的 VPS 方案

## 测试

### 测试速度[1]

1. 使用 `ping` 或 `tracert` 等工具进行测试延时和hop
2. 使用 站长工具等进行 ip ping 测试
3. 使用 BestTrace(https://www.vpser.net/manage/vps-test-tool.html) 进行可视化线路测试，可以通过查看出口IP查看出口线路

> 关于出口线路[2]：
> 据了解，目前中国电信共有两条线路接入全球互联网，分别是163骨干网(也就是CN1)线路以及现在新建设的CN2线路，出海的时候这两条线路是相互独立的，163骨干网(CN1)线路和CN2线路的简单区别如下：
>
> 1、163骨干网接入的是as4134带宽、CN2线路接入的是as4809带宽;
>
> 2、163骨干网是以202.97 IP地址开头的路由，而CN2线路是以59.43 IP地址开头的路由;
>
> 3、163骨干网海外出口带宽容量大，价格便宜，而CN2线路整体带宽容量较小，费用高。
>
> CN2 GT 和 CN2 GIA的区别：CN2 GT线路在没有出国之前一般是走的是202.97(163骨干网)，出国之后才会走59.43，CN2 GIA线路从国内省级网络开始就已经走59.43了，出国还是走59.43。
> 
> 笔者进行测试的时候发现教育网的出口不同于上述这些描写的出口，是从 101.4 直接出海，关于教育网的出口线路可以参考[3]


## reference

1. [常用VPS测试工具，线路测试工具详解](https://www.vpser.net/manage/vps-test-tool.html)
2. [带你了解CN2 GT和CN2 GIA线路的区别](https://developer.aliyun.com/article/762091)
3. [主流VPS线路介绍及简单评测（以北京教育网为例）](https://sbeam.dev/2019/06/22/lineintro/)