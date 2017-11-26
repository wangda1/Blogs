# Github常用命令

今日又重新启用了    github  来管理软件课设，渣渣以前还没用过呢

主要阐述一下关于    远程库与本地库的关联  
至于多人协作开发部分，学了再记


## 远程库与本地库

首先来一波本地库的操作  
`git init`来创建一个本地库 

`git remote add [name] git@github.com:username/xxxx.git`

来关联一个远程库

然后，你可能在本地库里经过了一番骚操作:        
```
git add .
git commit -m [message]
```

然后 push `git push -u origin master`  嘻嘻，报错，报错信息类似这样：       ```
To https://github.com/USERNAME/REPOSITORY.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to 'https://github.com/USERNAME/REPOSITORY.git'
To prevent you from losing history, non-fast-forward updates were rejected
Merge the remote changes (e.g. 'git pull') before pushing again.  See the
'Note about fast-forwards' section of 'git push --help' for details.
```      

为啥呢？因为远程库里有东西啊，想想也是，肯定不能随随便便    push    上去，那还版本管理啥啊，

于是乎，三条建议：       

1.
- git pull origin master

把远程库先   pull    下来然后再   push

2.
- git fetch origin 
- git merge origin master

这种方法与   1   原理相同

前面两种都属于 正规做法，还有下面的非主流做法：        

3.
- git push origin master -f
强推！！！当然了这一推远程库就被更改地与你一致了。:)不建议