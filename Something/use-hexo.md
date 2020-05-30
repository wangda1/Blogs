---
title: use-hexo
date: 2020-01-05 12:20:12
categories:
- Something
tags:
- Something
---

# USE-HEXO

本篇记录将 Blogs 使用 hexo + Next 主题的过程。

## 1. HEXO

> Hexo 是高效的静态站点生成框架，基于 Node.js.

### 1.1 安装

`npm i hexo-cli -g`

配置 github，文件：`_config.yml`
```
deploy:
  type: git
  repository: https://github.com/godweiyang/godweiyang.github.io
  branch: master
```

### 1.2 常用命令

```python
# 初始化文件夹
hexo init
# 生成静态网页
hexo g
# 打开本地服务器
hexo s
hexo s --debug
# 新建文章
hexo new post "article title"
# 新建页面
hexo new page "page title"
# 新建草稿
hexo new draft "draft title"
# 部署到github
hexo d

```

### 1.3 集成主题 `next`

- 关于 Next 主题的配置可以参考官方文档 [NexT](http://theme-next.iissnan.com/getting-started.html)

本站的配置内容（`blog-hexo\themes\next\themes\next`）：

- menu
- scheme
- social
- tencent_analytics
- Reward
- since

### 1.4 文章模板

```
---
# 文章标题中的空格替换为-
title: {{ title }}
# hexo 支持多个并列 tag
tags:
- A
- B
# hexo 不支持多个并列 category，以下为顺序父子关系
categories:
- A
- B
description:
date: {{ date }}
---
```

### 1.5 写文章注意事项

`next` 能自动识别不同级别的标题

## 2. 本站文章的更新

本站文章的更新采取了 Blog 源文件目录与 hexo 生成的目录分别放置的方式，每次站点的更新需要：

1. 将所有的 blog 文件复制到 `blog-hexo/source/_posts` 目录下；
2. `hexo s -g` 提前预览更新，或直接 `hexo g` 生成静态文件目录；
3. 将 `blog-hexo/public` 目录中的所有内容粘贴至 git 目录中，`add->commit->push` 即可；（这里`git push -f`）
4. 将 github 中的 `Custom domain` 设置为自身的域名 `laoxiangchun.cn`
