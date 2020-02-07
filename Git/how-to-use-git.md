--- 
title: How To Use Git
date: 2020/1/5 18:22
categories:
- Git
tags:
- Git
---


这里记录一下`git`常用的命令：

作为一个版本控制的软件，对于

- 版本管理

git 的版本管理主要靠`HEAD`指向的`commitId`来改变，是针对于一个`branch`而言，每个版本的内容除文件外还有日志`git log`

```git
git reset --hard  commitId      // 版本的切换
git reflog                      // 可以查看向后的commitId 
```

- 分支的管理

```git
git branch YourBranch      //  创建分支MyBranch
git branch -d YourBranch   //　删除分支MyBranch
git checkout YourBranch    //  切换分支
//  git checkout -b YourBranch    
git merge  Branch          // 合并分支，需要解决冲突
git diff branch1 branch2 --stat // 显示出所有有差异的文件列表
git diff branch1 branch2    // 显示出差异文件的详细差异
```

**注：**　合并分支时可以 master->dev，也可以　dev->master　只需要解决冲突一次即可

- remote, local的管理

查看远程库信息

```git
git remote -v
```

远程仓库的名字一般为：`origin`

```git
git clone https:url        //  将远程仓库克隆到本地，此时自动构建master分支与远程master分支关联
git remote add origin git@github.com:xxxx/xxxx.git        //  关联远程仓库
git push origin master        //  将本地master分支提交到远程仓库master分支
```

创建远程分支 dev 到本地

```git
git checkout -b dev origin/dev
```

将本地分支与远程分支建立链接，以便 `git pull`

```git
git branch --set-upstream-to=origin/dev dev
```

ref: [廖雪峰的git教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)