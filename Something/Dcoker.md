# Docker

## 常用操作

```python
# 查看帮助
docker xxx --help
# 拉取镜像
sudo docker pull image
# 创建容器
docker run image
# 列出当前运行的容器
docker ps
# 列出所有的容器，包括运行的和不运行的
docker ps -a
# 删除容器
docker rm container-id
# 容器的启动、进入、退出
docker start [-i] container-id
# 容器的停止、重启
docker stop container-id
docker restart container-id
```

## 参考

- [Docker,深度学习的环境配置](https://zhuanlan.zhihu.com/p/64493662)