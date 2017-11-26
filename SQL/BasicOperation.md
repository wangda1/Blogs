# MySQL的基本操作

MySQL数据库:  
**系统数据库:**  
> - information_schema: 数据库对象信息  
> - performance_schema: 性能参数  
> - mysql:  用户权限信息  
> - test：  用作测试的数据库 

**用户数据库(可创建多个)**

## MySQL数据库的操作  
> - 新建数据库:  create database 数据库名;  
> - 查看数据库:  show databases;(查看所有）  
> - 选择数据库:  use 数据库名;  
> - 删除数据库:  drop database 数据库名;
> - 查看支持的引擎:  show variables like 'have%';  
> - 查看引擎:    show engines;

## MySQL数据表的操作  

***表中数据库对象:  列，索引，触发器***  
> - 新建表:  create table 数据表名 (             );  
> - 查看表:  describe/desc 数据表名; show columns from  
> - 删除表:  drop table 数据表名;  
> - 修改表:  alter 













## MySQL语句操作  











## 操作表的约束  
对于字段的完整性约束

> - NOT NULL 非空  
> - DEFAULT  默认  
> - UNIQUE KEY(UK)  唯一  
> - PRIMARY KEY(PK) 主键  
> - AUTO_INCREMENT  自动增加  
> - FOREIGN KEY     外键

***表名，主键具有唯一性***   
***外键提前需要有父表的主键***







