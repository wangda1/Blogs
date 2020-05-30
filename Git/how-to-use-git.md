--- 
title: How To Use Git
date: 2020/1/5 18:22
categories:
- Git
tags:
- Git
---

- 版本管理

git 的版本管理主要靠`HEAD`指向的`commitId`来改变，是针对于一个`branch`而言，每个版本的内容除文件外还有日志`git log`

```git
git reset --hard  commitId      // 版本的切换
git reflog                      // 可以查看向后的commitId 
```

## 远程库与本地库

首先来一波本地库的操作  
`git init`来创建一个本地库 

`git remote add [name] git@github.com:username/xxxx.git`

来关联一个远程库

然后，你可能在本地库里经过了一番骚操作:

```git
git add .
git commit -m [message]
```

然后 push `git push -u origin master`  嘻嘻，报错，报错信息类似这样

```git
To https://github.com/USERNAME/REPOSITORY.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/USERNAME/REPOSITORY.git'
To prevent you from losing history, non-fast-forward updates were rejected
Merge the remote changes (e.g. 'git pull') before pushing again.  See the
'Note about fast-forwards' section of 'git push --help' for details.
```

为啥呢？因为远程库里有东西啊，想想也是，肯定不能随随便便    push    上去，那还版本管理啥啊，

于是乎，三条建议：

1. `git pull origin master`

把远程库先`pull`下来然后再`push`

2. `git fetch origin`  `git merge origin master`

这种方法与 1 原理相同

前面两种都属于 正规做法，还有下面的非主流做法：

1. `git push origin master -f`

强推！！！当然了这一推远程库就被更改地与你一致了。:)不建议

## Misc

1. `github.com` 的链接可以使用锚链接了！！ `https://github.com/python/cpython/blob/2.7/Python/bltinmodule.c#L1580` 指示在该 `.c` 文件的 1580 行

2. 当出现 `Failed to connect to github.com port 443: Timed out` 的错误，是 http.proxy 的问题

- `git config --global http.proxy (127.0.0.1:1080)`
- `git config --get http.proxy`
- `git config --list`
  
3. `git status` 显示的中文为八进制字符，而不是中文

- `git config --global core.quotepath false` 设置 `core.quotepath` 为 `false`

4. `git clone`之后拉取远程分支：

    1. `git branch -a` 显示远程所有分支；`git checkout origin/branch` 切换至某一远程分支（此时并没有建立本地与之对应的分支）；`git checkout xxx_branch` 建立与远程分支对应的分支；
    2. `git pull -all` 拉取所有分支到本地；
    3. `git clone -b xxx_branch https://xxx` 克隆某一分支到本地；

## 分支的管理

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

- `git stash`命令的使用

`git stash`会把当前暂存区与工作区的改动保存起来。

```git

git stash
git stash save 'message' ...        // 保存当前进度并添加一些注释

git stash list      // 显示保存进度的列表

git stash pop       // 恢复进度至工作区
git stash pop stash@{1}

git stash drop [stash_id]   // 删除存储的进度

git stash clear             // 删除所有存储的进度
```

ref: [廖雪峰的git教程](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000)