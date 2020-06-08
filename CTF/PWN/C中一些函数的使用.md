---
title: C中一些函数的使用
date: 2018-04-18 18:29:00
categories:
- CTF
- PWN
tags:
- CTF
- PWN
---

# C中一些函数的使用

- <font color="#A600C4"><span style="font-size: 19px;">setvbuf()</span></font> 函数原型： int setvbuf(FILE \* stream, char \* buf, int type, unsigned size); 

1. - <font color="#333333" face="微软雅黑, Microsoft Yahei, Arial, Helvetica, sans-serif">_IOFBF (满缓冲)：当缓冲区为空时，从流读入数据。或当缓冲区满时，向流写入数据。</font>
    - <font color="#333333" face="微软雅黑, Microsoft Yahei, Arial, Helvetica, sans-serif">_IOLBF (行缓冲)：每次从流中读入一行数据或向流中写入—行数据。</font>
    - <font color="#333333" face="微软雅黑, Microsoft Yahei, Arial, Helvetica, sans-serif">_IONBF (无缓冲）</font>

- <font face="微软雅黑, Microsoft Yahei, Arial, Helvetica, sans-serif"><span style="color: rgb(51, 51, 51); font-size: 14px;">与</span> <span style="font-size: 19px;"><font color="#A600C4">setbuf</font></span><span style="color: rgb(51, 51, 51); font-size: 14px;">的区别：setbuf()只能对缓冲区进行简单操作；两者都可以通过用户设置缓冲区，而不用再使用 fopen()打开的默认缓冲区</span></font>

<font color="#333333" face="微软雅黑, Microsoft Yahei, Arial, Helvetica, sans-serif"><span style="font-size: 14px;"><b>printf(),scanf(),gets(),puts()等函数的区别</b></span></font>
<font color="#333333" face="微软雅黑, Microsoft Yahei, Arial, Helvetica, sans-serif"><span style="font-size: 14px;"><b>     </b>都是从输入，输出缓冲区取内容输入或输出</span></font>

<font color="#333333" face="微软雅黑, Microsoft Yahei, Arial, Helvetica, sans-serif"><span style="font-size: 14px;"><br></span></font>

<font color="#FF0000" face="微软雅黑, Microsoft Yahei, Arial, Helvetica, sans-serif">#include <stdio.h></font>

- <font face="微软雅黑, Microsoft Yahei, Arial, Helvetica, sans-serif"><font color="#A600C4" style="font-size: 19px;">scanf(),gets()</font><font color="#333333" style="font-size: 14px;">：scanf() 会在</font><b style="font-size: 14px; color: rgb(51, 51, 51);">回车，空格，tab键结束</b><font color="#333333" style="font-size: 14px;">，并且这些键会</font><b style="font-size: 14px; color: rgb(51, 51, 51);">保留</b><font color="#333333" style="font-size: 14px;">在缓冲区中，scanf()会在字符串结尾自动补\0;    gets()会收入前面的这些键，以空格键结束，结尾自动补\0，并且不会保留在缓冲区中</font></font>
- <font face="微软雅黑, Microsoft Yahei, Arial, Helvetica, sans-serif"><font color="#A600C4" style="font-size: 19px;">printf(),puts()</font><font color="#333333" style="font-size: 14px;">会直接输出，但</font><b style="font-size: 14px; color: rgb(51, 51, 51);">puts()会将字符串结尾的\0转换成回车</b></font>
- <font face="微软雅黑, Microsoft Yahei, Arial, Helvetica, sans-serif"><span style="font-size: 18px;"><font color="#7600D8">size_t fread(void *ptr,size_t size,size_t nmemb,FILE *stream)：</font>从stream中读取数据到 ptr，size (size 大小）* nmemb（块大小）</span></font>
- <font face="微软雅黑, Microsoft Yahei, Arial, Helvetica, sans-serif"><span style="font-size: 18px;"><font color="#7600D8">size_t fwrite</font> 与之类似<font color="#FF0000">（两者都是对二进制文件进行读写）</font></span></font>

<font color="#FF0000" face="微软雅黑, Microsoft Yahei, Arial, Helvetica, sans-serif">#include <unistd.h></font>

- <font color="#A600C4" face="微软雅黑, Microsoft Yahei, Arial, Helvetica, sans-serif" size="4"><b>ssize_t read(int fd, void * buf, size_t count) </b></font>
- <font face="微软雅黑, Microsoft Yahei, Arial, Helvetica, sans-serif" size="4"><b>fd为文件描述符，buf缓冲区指针，count为字节数</b></font>

<font face="微软雅黑, Microsoft Yahei, Arial, Helvetica, sans-serif" size="4"><b><br></b></font>

- <font color="#A600C4" face="微软雅黑, Microsoft Yahei, Arial, Helvetica, sans-serif" size="4"><b>ssize_t write (int fd, const void * buf, size_t count)</b></font>

<font color="#FF0000">#include <stdlib.h></font>

- <font color="#A600C4" face="微软雅黑, Microsoft Yahei, Arial, Helvetica, sans-serif">strtoul  将 string to unsigned long int</font>
- <font color="#A600C4" face="微软雅黑, Microsoft Yahei, Arial, Helvetica, sans-serif">strtol 将 string to long int</font>
- <font face="微软雅黑, Microsoft Yahei, Arial, Helvetica, sans-serif">在ANSI C里规范定义了 <font color="#FF0000">stof( ),atoi( ),atol( ),strtod( ),strtol( ),strtoul( )</font> 可以将字符串转换成数字</font>
- <font face="微软雅黑, Microsoft Yahei, Arial, Helvetica, sans-serif">long int strtol(const char* str,char* endptr,int base)</font>
- <font face="微软雅黑, Microsoft Yahei, Arial, Helvetica, sans-serif">Python里的int与此作用相似</font>

<font color="#A600C4" face="微软雅黑, Microsoft Yahei, Arial, Helvetica, sans-serif" size="4"><b><br></b></font>