# Metasploit

这个在 Kali中是自带的，无需安装

我的 kali 4.6.0 amd64

## 启动

metasploit 默认使用 postgresql 数据库，进行一些信息的存储与检索

1.  启动  postgresql
- service postgresql start

2.  初始化 msfdb
- msfdb init    
初始化  数据库为  msfdb    用户名为  msf   默认密码为  空

3.  启动
- msfconsole    
控制台启动 metsploit
