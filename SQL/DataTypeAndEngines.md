# DataType and Engines  数据类型与存储引擎

## DataType 数据类型  

### 字符串类型  
1.CHAR:  CHAR(M),VARCHAR(M)

2.TEXT:  TINYTEXT,TEXT,MEDIUMTEXT,LONGTEXT 

3.BINARY: BINARY(M),VARBINARY(M)  

4.BLOB:  TINYBLOB,BLOB,MEDIUMBLOB,LONGBLOB 

1,3仅能存储字符数据，2,4可用来存储二进制数据，如：图片，音频，视频等


### 日期与时间类型

> - DATE  DATETIME  TIMESTAMP TIME  YEAR

### 浮点数，定点数与位类型

1.FLOAT   DOUBLE

2.DEC(M,D)  DECIMAL(M,D)

3.BIT(M)

### 整数类型

> - TINYINT   SMALLINT    MEDIUMINT   INT && INTEGER    BIGINT


## 存储引擎

存储引擎就是存储数据，建立索引，更新与查询数据的方法

> - 查询引擎命令: SHOW ENGINES; 
> - 查询支持的存储引擎:  SHOW VARIABLES LIKE 'have%'

***补:SHOW ENGINES \G;是一种较为理想的查看方式，而 SHOW ENGINGES;SHOW ENGINES \g;查看起来则不方便***

MySQL有多个可用的存储引擎，主要有:  InnoDB  MyISAM  MEMORY

InnoDB:  
> - 

MyISAM:  
> - 

MEMORY:  
> - 















