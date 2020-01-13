---
title: tmux tutorial
date: 2019-01-13 18:11:00
categories:
- Something
tags:
- Something
---

# tmux Tutorial

项目地址 [tmux](https://github.com/tmux/tmux)，终端复用工具. 
命令参考：https://www.cnblogs.com/kaiye/p/6275207.html

tmux 中有几个比较重要的概念：

- session: 建立一个工作区会话
- window: 容纳多个窗格
- pane: 可以在窗格中分成多个窗格
- `ctrl + B` 基本指令，使用该指令之后，输入的下一个指令解释为 `tmux` 命令

1. session 的操作

    - 新建 session：`tmux new -s name_xxx` name_xxx 为 session name
    - 断开当前 session：`tmux detach` 或者快捷键：`ctrl+b` + `d`
    - 进入之前的 session：`tmux attach-session -t session_name_xxx` = `tmux a -t session_name_xxx`； `tmux a` 默认进入第一个 session
    - session 的删除： `tmux kill-session -t session_name_xxx`：关闭对应的 session；`tmux kill-server`：关闭服务器，所有会话都将关闭
    - `tmux list-session` 查看所有 session = `tmux l`

2. 一个 session 中新建 window

    `ctrl+B` -> `c`

    sesssion 中 window 之间的切换：  
     `ctrl+B` -> `n` 切换 next wiindow；  
     `ctrl+B` -> `p` 切换 previous window

3. 一个 window 里新建 pane

    左右切分 pane: `ctrl+B` -> `%`；  
    上下切分 pane: `ctrl+B` -> `"`；  
    pane 之间的切换使用 `ctrl+B` -> 上下左右；  
    关闭 pane: `ctrl+B` -> `x`
