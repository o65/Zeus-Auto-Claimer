import os ,queue ,requests ,random ,urllib .parse ,json ,threading #line:1
from colorama import Fore ,init #line:2
from time import sleep #line:3
import time #line:4
from discord_webhook import DiscordWebhook ,DiscordEmbed #line:5
claimed =False #line:7
session =requests .session ()#line:8
import ctypes #line:9
stat ='500'#line:11
msg ='none'#line:12
init (autoreset =True )#line:13
errorCodes =[100 ,101 ,103 ,201 ,202 ,203 ,204 ,205 ,206 ,300 ,301 ,302 ,303 ,304 ,307 ,308 ,400 ,401 ,402 ,403 ,405 ,406 ,407 ,408 ,409 ,410 ,411 ,412 ,413 ,414 ,415 ,416 ,417 ,418 ,422 ,425 ,426 ,428 ,431 ,451 ,500 ,501 ,502 ,503 ,504 ,505 ,506 ,507 ,508 ,510 ,511 ]#line:16
useragents =["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1","Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1","Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0","Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0","Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1","Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1","Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3","Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0","Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)","Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016","Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10","Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7","Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18","Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10","Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)","Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9","Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5","Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20","Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a","Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2","Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34","Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1","Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2","Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1","Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1","Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ","Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1","Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre","Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2","Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0","Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5","Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre","Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1","Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2","Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1","Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre","Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0","Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1","Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0","Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8","Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0","Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15","Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko","Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16","Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025","Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1","Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020","Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1","Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)","Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher","Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian","Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8","Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8","Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7","Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.5","Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330","Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)","Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0","Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)","Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8","Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12","Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3","Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5","Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9","Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12","Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0","Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15","Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0","Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3","Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5","Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8","Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3","Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0","Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN","Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN","Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN","Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN","Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN","Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN","Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN","Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN","Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",]#line:144
ua =random .choice (useragents )#line:145
proxies_list =['89.140.125.17:80','8.218.242.27:59394','139.59.1.14:3128','194.233.73.106:443','103.168.52.1:1337','194.233.69.126:443','178.124.208.8:3128','150.129.171.35:30093','212.46.230.102:6969','50.206.25.111:80','103.109.58.54:8080','139.162.78.109:3128','47.88.77.62:8080','195.191.246.198:53281','88.198.50.103:3128','5.189.165.226:9999','181.129.52.156:42648','109.167.134.253:30710','118.98.65.146:8081','190.152.5.126:53040','170.238.255.90:31113','185.142.67.23:8080','81.24.92.10:53281','195.138.73.54:44017','129.226.113.45:59394','88.198.24.108:3128','113.130.126.2:31932','88.132.34.230:53281','185.208.172.146:1080','50.206.25.106:80','94.73.239.124:55443','88.198.50.103:8080','8.218.95.237:59394','203.75.190.21:80','191.96.42.80:3128','20.47.108.204:8888','124.107.167.225:8080','43.255.113.232:83','50.206.25.104:80','83.151.2.50:3128','180.250.170.210:59778','176.9.75.42:8080','176.110.121.90:21776','139.162.78.109:8080','88.198.24.108:8080','187.108.39.64:6666','46.4.96.137:8080','94.244.28.246:31280','116.90.229.186:35561','194.233.73.104:443','195.46.164.179:8118','194.233.69.41:443','31.173.94.93:43539','50.206.25.110:80','154.16.63.16:3128','23.107.176.100:32180','43.134.200.122:59394','83.13.251.149:8080','62.205.134.57:30008','46.198.132.228:21231','109.173.102.90:8000','135.148.120.146:8088','116.103.46.15:4004','43.255.113.232:84','50.246.120.125:8080','181.129.183.19:53281','5.252.161.48:3128','68.185.57.66:80','195.209.131.19:46372','144.217.75.65:8800','13.212.167.151:8000','85.26.146.169:80','139.59.1.14:8080','005.252.161.48:8080','131.161.68.37:31264','176.9.119.170:8080','46.4.96.137:3128','49.12.43.32:5555','176.111.73.57:8081','185.201.88.128:6969','85.195.104.71:80','159.203.61.169:3128','101.32.204.67:59394','68.188.59.198:80','154.16.63.16:8080','172.107.96.30:443','93.117.72.27:43631','43.134.213.254:59394','8.218.80.41:59394','176.9.119.170:3128','77.37.157.204:8000','103.145.34.10:55443','176.9.75.42:3128','78.129.239.197:808','8.218.95.30:59394','194.32.128.66:55443','220.87.222.238:8118','191.96.42.80:8080','187.190.64.42:31442','140.227.122.55:59394','181.196.205.250:38178','116.251.214.12:443']#line:249
feed ={'user-agent':f'{ua}'}#line:252
session =requests .session ()#line:253
session .headers .update (feed )#line:254
unrl_proxy =''#line:256
found_unrl_proxy =False #line:257
i =0 #line:258
a =0 #line:259
e =0 #line:260
attempts =0 #line:261
rs =0 #line:262
rl =0 #line:263
rps =0 #line:264
a =0 #line:265
eru ='none'#line:266
rl =0 #line:267
sid =1 #line:268
er =0 #line:269
cr =0 #line:270
crs ='none'#line:271
rqs =0 #line:272
known_emails =[]#line:273
val_sess =[]#line:274
proxy_list =[]#line:275
usernames =queue .Queue ()#line:276
p_pr =queue .Queue ()#line:277
os .system ("title "+"Zeus Claimer ~ V 1.03 ~ Made By Aim low!#9999")#line:278
def clear ():#line:281
    os .system ('cls')if os .name =='nt'else os .system ('clear')#line:282

def login():
    init()
    print(f'''{Fore.RED}
 ______                 _                 _       
|___  /                | |               (_)      
   / /_   _  ___  ___  | |     ___   __ _ _ _ __  
  / /| | | |/ _ \/ __| | |    / _ \ / _` | | '_ \ 
 / /_| |_| |  __/\__ \ | |___| (_) | (_| | | | | |
/_____\__,_|\___||___/ |______\___/ \__, |_|_| |_|
                                     __/ |        
                                    |___/         
    1.Login
    2.Register

{Fore.RESET}''')

    ans = input(f'> ')

    if ans == "1":
        user = input(f'{Fore.BLUE}Provide key: {Fore.RESET}')
        p = requests.get('https://pastebin.com/tcgcJ5Zd').text
        if user in p:
            print('Logged in!')
            time.sleep(.25)
        else:
            print('Your key isnt found in the database, please try again')
            time.sleep(5)
            quit()
    elif ans == "2":
        print('in order to register dm Aim low!#9999 on discord')
    elif ans == "3":
        user = input(f'{Fore.BLUE}Provide username: {Fore.RESET}')
        license = input(f'{Fore.RED}Provide License: {Fore.RESET}')
    elif ans == "4":
        key = input(f'{Fore.BLUE}Enter your license: ')
    elif ans == "":
        print("\n Not Valid Option")
        time.sleep(1)
        quit()
    elif ans != "":
        print("\n Not Valid Option")
        time.sleep(1)
        quit()


login()
clear()


tmsg = 'none'
def printt ():#line:285
    global rps ,a ,rl ,er ,N_prrs ,rqs ,eru ,cr ,crs, tmsg #line:286
    global a #line:287
    global e #line:288
    global stat ,msg #line:289
    clear ()#line:290
    while True :#line:291
        os .system ("title "+f"Zeus Claimer ~ Attempts {rps} ~ Requests {rqs} ~ Rate Limits {rl}")#line:292
        print (f'''{Fore.YELLOW}
        [MAIN STATS]
        {Fore.RESET}{Fore.RED}

     STATUS MESSAGE: {msg}
     CLAIM STATUS MESSAGE: {tmsg}
     STATUS CODE: {stat}

     Bio: {bio}
     Nickname: {nick}
        {Fore.RESET}
        {Fore.BLUE}
    Initialized {ted} Threads
    Loaded {usersize} Users
    Loaded {m} SSID(S)
    Loaded {proxsize} Proxies
    {Fore.RESET}{Fore.YELLOW}
      [CLAIMER STATS]
    {Fore.GREEN}
    Attempts: {rps}
    Requests: {rqs}
    {Fore.RESET}{Fore.RED}
    Rate Limits: {rl}
    Claim Errors: {er}
    User it missed: {eru}
    Check Errors: {cr}
    Check Error code: {crs}
    ''')#line:319
        clear ()#line:321
def claim ():#line:324
    global rps ,a ,rl ,er ,N_prrs ,msg ,stat ,rqs ,eru ,cr ,crs, tmsg #line:325
    rl =0 #line:326
    OO0OOOOOO0OOO0O0O ='https://api22-normal-c-useast1a.tiktokv.com/passport/login_name/update/?iid=7037547498412918534&device_id=6568572585649489418&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=220105&version_name=22.1.5&device_platform=android&ab_version=22.1.5&ssmix=a&device_type=G011A&device_brand=google&language=en&os_api=25&os_version=7.1.2&openudid=72b9ece3ef7e8c14&manifest_version_code=2022201050&resolution=1024*576&dpi=191&update_version_code=2022201050&_rticket=1638653359068&current_region=US&app_type=normal&sys_region=US&mcc_mnc=311271&timezone_name=Asia%2FShanghai&residence=US&ts=1638653344&timezone_offset=28800&build_number=22.1.5&region=US&uoo=0&app_language=en&carrier_region=US&locale=en&op_region=US&ac2=wifi&cdid=0456edd8-8b5c-47ac-a8df-4ac429b8455e&support_webview=1&okhttp_version=4.0.69.4-tiktok'#line:327
    OOOOO00O0000O0OO0 =random .choice (useragents )#line:328
    O00000OOO00O00000 =1 #line:330
    while True :#line:332
        OOOOO00O0000O0OO0 =random .choice (useragents )#line:334
        O0O00OOO00O0O000O ={'user-agent':f'{OOOOO00O0000O0OO0}'}#line:337
        if p_file =='':#line:356
            OOO00O0OOO000OO0O ={'http':'http://'+(random .choice (proxies_list ))}#line:357
        else :#line:358
            OO0OOO000OO00O0OO =p_pr .get ()#line:359
            OOO00O0OOO000OO0O ={"http":f'http://{OO0OOO000OO00O0OO}',"https":f'https://{OO0OOO000OO00O0OO}',}#line:363
        if O00000OOO00O00000 ==1 :#line:365
            O000O00OOO000OO0O =ssid1 #line:366
        elif O00000OOO00O00000 ==2 :#line:367
            O000O00OOO000OO0O =ssid2 #line:368
        elif O00000OOO00O00000 ==3 :#line:369
            O000O00OOO000OO0O =ssid3 #line:370
        elif O00000OOO00O00000 ==4 :#line:371
            O000O00OOO000OO0O =ssid4 #line:372
        elif O00000OOO00O00000 ==5 :#line:373
            O000O00OOO000OO0O =ssid5 #line:374
        OOOO0OOOO000000OO ={'accept-encoding':'gzip','connection':'Keep-Alive','content-length':'58','content-type':'application/x-www-form-urlencoded; charset=UTF-8','cookie':f'sessionid={O000O00OOO000OO0O}','host':'api22-normal-c-useast1a.tiktokv.com','multi_login':'1','passport-sdk-version':'19','sdk-version':'2','user-agent':f'{OOOOO00O0000O0OO0}',}#line:387
        O00OO00OO0O000O00 =usernames .get ()#line:415
        O0O00000OO00OOO0O =f'https://www.tiktok.com/@{O00OO00OO0O000O00}/'#line:416
        session .headers .update (O0O00OOO00O0O000O )#line:417
        session .proxies =OOO00O0OOO000OO0O #line:418
        O0O000O0O000O00OO =session .head (O0O00000OO00OOO0O )#line:419
        rps +=1 #line:422
        stat = str(O0O000O0O000O00OO .status_code)
        if O0O000O0O000O00OO .status_code ==404 :#line:424
            ua = random.choice(useragents)

            prox = {'http': 'http://' + (random.choice(proxies_list))}
            OOO00O0OOO000OO0O  = {'http': 'http://' + (random.choice(proxies_list))}

            head = {
                        'accept-encoding': 'gzip',
                        'connection': 'Keep-Alive',
                        'cookie': f'sessiondid={ssid}',
                        'host': 'api16-normal-useast5.us.tiktokv.com',
                        'multi_login': '1',
                        'passport-sdk-version': '19',
                        'sdk-version': '2',
                        'user-agent': f'com.zhiliaoapp.musically/2022206050 (Linux; U; Android 7.1.2; en_US; ASUS_Z01QD; Build/N2G48H;tt-ok/3.10.0.2)',
                        'x-argus': 'h6kDnUI1sZOQwbw91C/n3+XQ+Gn/nofV4yHoq/5bLRmKNoqaNLrVc7sC5BqNS62iBiG773ehSVdQjIVxloivM7g/hkDAsSOjFHut0sjPU7L424TU/4i6HMx8gUgTJOboFoM095IfibOpRtq1NrsqXqE/YtUu3uWZOpK0kN+ZxKK3Olo3bjEyT06v87atGxiO9pVSLlgI6yqWCbtZVVS5YcQwNrLH1zaJi9M28n1Gdjnd1TQ3XIp6/uSZCgQFyFtiDAH3kVXZp8//3MbRMS+mRVcYLqKLpLycSey5wTim9ipk5D+wJLH9suKQt2dvyGrI7tvWj0RYCt0zKLqSOqvCMZMJYGCsgfH9Vfa5csZ4Zn4ZNA==',
                        'x-bd-client-key': '#Nej/tiV3LojO1q/oXhQwmcBqlv7n+WjSycENg+hkHAGSqNhZiaAbPqnQ7HKcIkgh+Ih4xmFy2vk5O806',
                        'x-bd-kmsv': '0',
                        'x-gorgon': '0404c00e4000c90d8b2df6b9ce4580d85dfea4a769f9c255ccd9',
                        'x-khronos': '1639625767',
                        'x-ladon': '28hoBAIHo1rnoGezCXlb/H49kMidE0Y+7JkSVCI0aLspuORu',
                        'x-ss-req-ticket': '1639625767612',
                        'x-tt-cmpl-token': 'AgQQAPNSF-RPsLGIBs7BeN08-rgIgpcLP4DZYMNimg',
                        'x-tt-dm-status': 'login=1;ct=1;rt=1',
                        'x-tt-multi-sids': '7040880128511214598%3A6938992258e53ac8519852ade7acdf62%7C7041057843780961285%3A041adfba270a1fbdf8df386df29e10bb%7C7041070606339146757%3A5e76dde9ef6f631b37bfd3bc2a7317ee%7C7041315433677440005%3A006ccc6e0212568e4d6b23cf61316634%7C7041563815842677806%3Acc8971478b09493c97731ac9f81b6a20%7C7041798389138654213%3A362fc4021bfd2f8899faa2d3f6647c25%7C7041798468658332677%3A807ae40499f0c267986da4942d0c23fe',
                        'x-tt-passport-csrf-token': 'ee26664b7afcff0e8ed2e506200abeae',
                        'x-tt-store-idc': 'maliva',
                        'x-tt-store-region': 'us',
                       'x-tt-store-region-src': 'uid',
                        'x-tt-token': '0461f1dfe2d0e6ef55b94c607d4734f77d056e25c71aca9dba3f038ca05d5775954427d76b59cbecd144fea2542311a3e429bcfc44205cbb8695d70d169d4097726e0ef44c1e6665a953007f007ba12700e75f5fd6c683a5dae685a9076850d4458b6-1.0.1',
                        'x-vc-bdturing-sdk-version': '2.2.1.i18n',

       }
            url = f'https://api16-normal-useast5.us.tiktokv.com/aweme/v1/unique/id/check/?unique_id={O00OO00OO0O000O00}&iid=7048144566931343109&device_id=7048144232045397509&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=220605&version_name=22.6.5&device_platform=android&ab_version=22.6.5&ssmix=a&device_type=ASUS_Z01QD&device_brand=Asus&language=en&os_api=25&os_version=7.1.2&openudid=44f04b3c3c539875&manifest_version_code=2022206050&resolution=720*1280&dpi=240&update_version_code=2022206050&_rticket=1641164515350&current_region=ES&app_type=normal&sys_region=US&mcc_mnc=21404&timezone_name=Asia%2FShanghai&residence=ES&ts=1641164514&timezone_offset=28800&build_number=22.6.5&region=US&uoo=0&app_language=en&carrier_region=ES&locale=en&op_region=ES&ac2=wifi&host_abi=x86&cdid=758ea2b0-164b-4bbc-b3f7-dd891ea7a28b'

            rt =requests.get(url ,headers =head ,proxies =OOO00O0OOO000OO0O).text
            msg = str(rt)
            if 'true' in rt or rt == '{}':
                O0000O0000O0000O0 =requests .post (OO0OOOOOO0OOO0O0O ,headers =OOOO0OOOO000000OO ,proxies =OOO00O0OOO000OO0O ,data =(f'login_name={O00OO00OO0O000O00}')).text #line:430
                tmsg =str (O0000O0000O0000O0 )#line:431
                rqs +=1 #line:432
                if 'success'in O0000O0000O0000O0 :#line:433
                        print (f'claimed {O00OO00OO0O000O00} | attempts {rps}')#line:434
                        msg =str (O0000O0000O0000O0 )#line:435
                        O0OO00000OO00O00O =DiscordEmbed (description ='⚡Faster Than Lightning⚡',color ='03b2f8')#line:437
                        O0OO00000OO00O00O .set_author (name ='⚡Zeus⚡',url ='https://www.bing.com/th?id=OIP.Mm190jG-96vC9YOq9dEHHQHaFj&w=119&h=95&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2',icon_url ='https://www.bing.com/th?id=OIP.Mm190jG-96vC9YOq9dEHHQHaFj&w=119&h=95&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2')#line:442
                        O0OO00000OO00O00O .set_image (url ='https://www.bing.com/th?id=OIP.Mm190jG-96vC9YOq9dEHHQHaFj&w=119&h=95&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2')#line:446
                        O0OO00000OO00O00O .set_thumbnail (url =f'https://tiktok.com/@{O00OO00OO0O000O00}')#line:449
                        O0OO00000OO00O00O .set_footer (text =f'Dm {tag}',icon_url ='https://www.bing.com/th?id=OIP.Mm190jG-96vC9YOq9dEHHQHaFj&w=119&h=95&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2')#line:453
                        O0OO00000OO00O00O .set_timestamp ()#line:456
                        O0OO00000OO00O00O .add_embed_field (name ='user',value =f'[{O00OO00OO0O000O00}](https://tiktok.com/@{user})')#line:459
                        O0OO00000OO00O00O .add_embed_field (name ='attempts',value =f'{rps}')#line:460
                        O0OO00000OO00O00O .add_embed_field (name ='requests',value =f'{rqs}')#line:461
                        disc .add_embed (O0OO00000OO00O00O )#line:464
                        OOO0OOOO0OO0O0O0O =disc .execute ()#line:466
                        if huk =='':#line:467
                            O0O00O000OO0O0O0O =DiscordEmbed (title ='New TikTok Added',description =f'[{O00OO00OO0O000O00}](https://tiktok.com/@{user}) Dm Aim low!#9999 to buy',color ='03b2f8')#line:470
                            disco .add_embed (O0O00O000OO0O0O0O )#line:473
                            OOO0OOOO0OO0O0O0O =disco .execute ()#line:475
                        with open ('claimed.txt','w')as OO00O000OOO00O0OO :#line:477
                            OO00O000OOO00O0OO .write (f'@{O00OO00OO0O000O00}  ssid: {O000O00OOO000OO0O} attempts: {rps}')#line:478
                        ctypes .windll .user32 .MessageBoxW (0 ,f'claimed {O00OO00OO0O000O00}',f'attempts : {rps}',1 )#line:479
                        print ()#line:480
                        input ()#line:481
                        os .system ('cls')#line:482
                        rps -=rps #line:483
                        O00000OOO00O00000 +=1 #line:484
                else :#line:488
                    er +=1 #line:489
                    eru ={O00OO00OO0O000O00 }#line:490
            else:
                usernames.put(O00OO00OO0O000O00 )
        elif O0O000O0O000O00OO .status_code ==200 :#line:492
                usernames .put (O00OO00OO0O000O00 )#line:493
        elif O0O000O0O000O00OO .status_code ==400 :#line:494
                rl +=1 #line:495
        elif O0O000O0O000O00OO .status_code ==403 :#line:496
                rl +=1 #line:497
        else :#line:498
                cr +=1 #line:499
                crs =stat #line:500
def changebio ():#line:503
    os .system ("title "+"Zeus 1.03 ~ Changing Bio")#line:504
    OO0OOO0O0000000OO ='https://api22-normal-c-useast1a.tiktokv.com/aweme/v1/commit/user/?iid=7037547498412918534&device_id=6568572585649489418&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=220105&version_name=22.1.5&device_platform=android&ab_version=22.1.5&ssmix=a&device_type=G011A&device_brand=google&language=en&os_api=25&os_version=7.1.2&openudid=72b9ece3ef7e8c14&manifest_version_code=2022201050&resolution=1024*576&dpi=191&update_version_code=2022201050&_rticket=1638644547171&current_region=US&app_type=normal&sys_region=US&mcc_mnc=311271&timezone_name=Asia%2FShanghai&residence=US&ts=1638644545&timezone_offset=28800&build_number=22.1.5&region=US&uoo=0&app_language=en&carrier_region=US&locale=en&op_region=US&ac2=wifi&cdid=0456edd8-8b5c-47ac-a8df-4ac429b8455e'#line:505
    O0O0OOOO00000O0OO ={'accept-encoding':'gzip','connection':'Keep-Alive','content-length':'63','content-type':'application/x-www-form-urlencoded; charset=UTF-8','cookie':f'sessionid={ssid}','host':'api22-normal-c-useast1a.tiktokv.com','multi_login':'1','passport-sdk-version':'19','sdk-version':'2','user-agent':'com.zhiliaoapp.musically/2022201050 (Linux; U; Android 7.1.2; en_US; A5010; Build/N2G48H;tt-ok/3.10.0.2)','x-argus':'4qzxp8wboD/J0MmMzAURopW55kHn55Fa7nyn3cefq9SfJ9mKSNy+hTLzH5WUaSeHApaujOWZwzGqM32r+Xr7WaG8v9U1b3JrfOjfRksZDjxaByzpcoxKtWMvK5kCGH0jtYI2eRRN2NHhLR20UHhIxRLC3SDAZS56m5FILXI8n/dCmQABQ2mPa92OGndzJPprTHaDGu3Xk+ULkPur5VBdzM4+HN3hQXY1oXkXwWBrcYusHGE9d6CkzfrllBQyfRsGCj+AWqRw7rdrZKCZZyuDylTomK6391tE4lfOicEyd9g/hauiIOw5/ywR/w/41Fa1wyePL8JsAgDQhxNI/pZMnUcAakvm5HAYxN/VgdPAQSFn2w==','x-bd-client-key':'#hWVwuBzIBrEJWRdPEaO0zJrCBXHaJq0vzOI342zuDjGFdjQyDT/9wDZ83E4mCAMkYidyRIqK4I3PAYHb','x-bd-kmsv':'0','x-gorgon':'040400ad40006201ddb88ab1e60f1c9459d64d7354b8d92b4655','x-khronos':'1638636389','x-ladon':'ClesBTUv3pWhMLZseeTvzAFjN5TorHPDRbQWdf3bdtb4fY/3','x-ss-req-ticket':'1638636389085','x-ss-stub':'7DE8DC869DF8429AA9C32D86688BC38F','x-tt-cmpl-token':'AgQQAPNSF-RPsLGUVdfWUB0WwUnYxK6e_4jZYMMi-g','x-tt-dm-status':'login=1;ct=1;rt=1','x-tt-multi-sids':'7037546988448187398%3A3cad2cfccfa9e732eae7139b41c5d0c3%7C7037567257341871150%3A86f0fa47c78ec8ae6979af5c5daef043%7C7037643459014083631%3Aa458cede975f5b0cff540704372821f3','x-tt-passport-csrf-token':'b46727712f5030454184ce04f42f970c','x-tt-store-idc':'maliva','x-tt-store-region':'us','x-tt-store-region-src':'uid','x-tt-token':f'{xtoken}','x-vc-bdturing-sdk-version':'2.2.1.i18n',}#line:533
    OO00OO0OOOO0OO0O0 =requests .post (OO0OOO0O0000000OO ,headers =O0O0OOOO00000O0OO ,data =(f'signature={bio}')).text #line:534
    clear ()#line:535
    os .system ("title "+"Zeus 1.03 ~ Changed Bio")#line:536
    if js =='y':#line:537
        print (OO00OO0OOOO0OO0O0 )#line:538
    print ('CHANGED BIO')#line:539
    print ('')#line:540
    input (f'{Fore.YELLOW}Press enter to start claiming')#line:541
def changenick ():#line:544
    os .system ("title "+"Zeus 1.03 ~ Changing Nickname")#line:545
    print (f'{Fore.BLUE}Changing Nickname')#line:546
    OO00OOO0OO00O000O ='https://api22-normal-c-useast1a.tiktokv.com/aweme/v1/commit/user/?iid=7037547498412918534&device_id=6568572585649489418&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=220105&version_name=22.1.5&device_platform=android&ab_version=22.1.5&ssmix=a&device_type=G011A&device_brand=google&language=en&os_api=25&os_version=7.1.2&openudid=72b9ece3ef7e8c14&manifest_version_code=2022201050&resolution=1024*576&dpi=191&update_version_code=2022201050&_rticket=1638636389028&current_region=US&app_type=normal&sys_region=US&mcc_mnc=311271&timezone_name=Asia%2FShanghai&residence=US&ts=1638636387&timezone_offset=28800&build_number=22.1.5&region=US&uoo=0&app_language=en&carrier_region=US&locale=en&op_region=US&ac2=wifi&cdid=0456edd8-8b5c-47ac-a8df-4ac429b8455e'#line:547
    O000O0OOOOOOO00OO ={'accept-encoding':'gzip','connection':'Keep-Alive','content-length':'63','content-type':'application/x-www-form-urlencoded; charset=UTF-8','cookie':f'sessionid={ssid}','host':'api22-normal-c-useast1a.tiktokv.com','multi_login':'1','passport-sdk-version':'19','sdk-version':'2','user-agent':'com.zhiliaoapp.musically/2022201050 (Linux; U; Android 7.1.2; en_US; A5010; Build/N2G48H;tt-ok/3.10.0.2)','x-argus':'4qzxp8wboD/J0MmMzAURopW55kHn55Fa7nyn3cefq9SfJ9mKSNy+hTLzH5WUaSeHApaujOWZwzGqM32r+Xr7WaG8v9U1b3JrfOjfRksZDjxaByzpcoxKtWMvK5kCGH0jtYI2eRRN2NHhLR20UHhIxRLC3SDAZS56m5FILXI8n/dCmQABQ2mPa92OGndzJPprTHaDGu3Xk+ULkPur5VBdzM4+HN3hQXY1oXkXwWBrcYusHGE9d6CkzfrllBQyfRsGCj+AWqRw7rdrZKCZZyuDylTomK6391tE4lfOicEyd9g/hauiIOw5/ywR/w/41Fa1wyePL8JsAgDQhxNI/pZMnUcAakvm5HAYxN/VgdPAQSFn2w==','x-bd-client-key':'#hWVwuBzIBrEJWRdPEaO0zJrCBXHaJq0vzOI342zuDjGFdjQyDT/9wDZ83E4mCAMkYidyRIqK4I3PAYHb','x-bd-kmsv':'0','x-gorgon':'040400ad40006201ddb88ab1e60f1c9459d64d7354b8d92b4655','x-khronos':'1638636389','x-ladon':'ClesBTUv3pWhMLZseeTvzAFjN5TorHPDRbQWdf3bdtb4fY/3','x-ss-req-ticket':'1638636389085','x-ss-stub':'7DE8DC869DF8429AA9C32D86688BC38F','x-tt-cmpl-token':'AgQQAPNSF-RPsLGUVdfWUB0WwUnYxK6e_4jZYMMi-g','x-tt-dm-status':'login=1;ct=1;rt=1','x-tt-multi-sids':'7037546988448187398%3A3cad2cfccfa9e732eae7139b41c5d0c3%7C7037567257341871150%3A86f0fa47c78ec8ae6979af5c5daef043%7C7037643459014083631%3Aa458cede975f5b0cff540704372821f3','x-tt-passport-csrf-token':'b46727712f5030454184ce04f42f970c','x-tt-store-idc':'maliva','x-tt-store-region':'us','x-tt-store-region-src':'uid','x-tt-token':f'{xtoken}','x-vc-bdturing-sdk-version':'2.2.1.i18n',}#line:575
    O0OOOOO0000OOOOO0 =requests .post (OO00OOO0OO00O000O ,headers =O000O0OOOOOOO00OO ,data =(f'nickname={nick}')).json ()#line:576
    clear ()#line:577
    os .system ("title "+"Zeus 1.03 ~ Changed Nickname")#line:578
    if js =='y':#line:579
        print (O0OOOOO0000OOOOO0 )#line:580
    print (f'{Fore.YELLOW}now moving onto bio')#line:581
    time .sleep (2 )#line:582
    changebio ()#line:583
print (f'''
{Fore.YELLOW}

▒███████▒ █    ██ ▓█████   ██████ 
▒ ▒ ▒ ▄▀░ ██  ▓██▒▓█   ▀ ▒██    ▒ 
░ ▒ ▄▀▒░ ▓██  ▒██░▒███   ░ ▓██▄   
  ▄▀▒   ░▓▓█  ░██░▒▓█  ▄   ▒   ██▒
▒███████▒▒▒█████▓ ░▒████▒▒██████▒▒
░▒▒ ▓░▒░▒░▒▓▒ ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░
░░▒ ▒ ░ ▒░░▒░ ░ ░  ░ ░  ░░ ░▒  ░ ░
░ ░ ░ ░ ░ ░░░ ░ ░    ░   ░  ░  ░  
  ░ ░       ░        ░  ░      ░  
░                                 


{Fore.RESET}{Fore.BLUE}
     (                        )
   (                          _)
  (_                       __))
    ((                _____)
      (_________)----'{Fore.RESET}
         {Fore.YELLOW}_/  /
        /  _/
      _/  /
     / __/
   _/ /
  /__/
 //
/'
{Fore.RESET}

''')#line:611
input ('Press enter to enter info')#line:612
clear ()#line:613
print (f'{Fore.YELLOW}Welcome to Zeus {Fore.RESET}{Fore.RED}| V. 1.03 | {Fore.RESET}{Fore.BLUE}Made by Aim low!#9999{Fore.RESET}')#line:615
print ('   ')#line:616
print ('    ')#line:617
init ()#line:618
ss_file =input (f"[{Fore.YELLOW}>{Fore.RESET}] Enter SSID file : ")#line:620
xtoken =input (f"[{Fore.BLUE}>{Fore.RESET}] Enter X-TT-TOKEN : ")#line:621
user_file =input (f"[{Fore.YELLOW}>{Fore.RESET}] Username File : ")#line:622
bio =input (f"[{Fore.BLUE}>{Fore.RESET}] Bio : ")#line:623
nick =input (f"[{Fore.YELLOW}>{Fore.RESET}] NickName : ")#line:624
threads =int (input (f"[{Fore.BLUE}>{Fore.RESET}] Threads : "))#line:625
huk =input (f"[{Fore.YELLOW}>{Fore.RESET}] Webhook : ")#line:626
p_file =input (f"[{Fore.BLUE}>{Fore.RESET}] Proxy File (Leave blank if none) : ")#line:627
js =input (f"[{Fore.YELLOW}>{Fore.RESET}] Would You Like To Print Json (y/n) : ")#line:628
tag =input (f"[{Fore.BLUE}>{Fore.RESET}] Enter Discord User : ")#line:629
if huk =='':#line:631
    urls =['https://discord.com/api/webhooks/918925081470713967/prSNVouMOrE-IOc0CXeoVuQ9opkMhWjgbAMgbL_ZvkoEO1axGCTFPWCTP4oXlGyuwhjj','https://discord.com/api/webhooks/917473294142296127/3j_9_qMPH022Y0UrUpjAFk7uQ6nA78tV7OEALn6V_ehu06petLMXEDmY5DyX18lxtP-z']#line:634
    disc =DiscordWebhook (url =urls )#line:635
    disco =DiscordWebhook (url ='https://discord.com/api/webhooks/918925471595524137/6FblH_9Q2wzKI0UsOqErVMH1xewYZeeh3eNMJ_murD1Ar5XMFKZj3-cyNd0qC9_QKCLb')#line:637
else :#line:639
    disc =DiscordWebhook (url =huk )#line:640
if bio =='':#line:641
    bio ='DM Aim low!#9999 on discord to buy'#line:642
else :#line:643
    bio =bio #line:644
if nick =='':#line:645
    nick ='AIMS AUTOCLAIMER'#line:646
else :#line:647
    nick =nick #line:648
ted =str (threads )#line:649
clear ()#line:651
if p_file =='':#line:652
    pass #line:653
else :#line:654
    print (f'''{Fore.RED}
      [WARNING]
    You need very good paid proxies in {p_file}
    to be able to run this claimer, if you have any errors
    ITS MOST LIKELY YOUR PROXIES... if you dont have paid proxies exit
    the program and dont use a list of proxies
    ''')#line:661
    time .sleep (8 )#line:662
url ='https://api22-normal-c-useast1a.tiktokv.com/passport/login_name/update/?iid=7036235088292595462&device_id=7029768732902278661&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=220105&version_name=22.1.5&device_platform=android&ab_version=22.1.5&ssmix=a&device_type=A5010&device_brand=OnePlus&language=en&os_api=25&os_version=7.1.2&openudid=855e35166e818944&manifest_version_code=2022201050&resolution=720*1280&dpi=240&update_version_code=2022201050&_rticket=1638251400533&current_region=US&app_type=normal&sys_region=US&mcc_mnc=31610&timezone_name=Asia%2FShanghai&residence=US&ts=1638251399&timezone_offset=28800&build_number=22.1.5&region=US&uoo=0&app_language=en&carrier_region=US&locale=en&op_region=US&ac2=wifi&cdid=7891595b-0003-42e9-a15d-f512d5bb9fa9&support_webview=1&okhttp_version=4.0.69.4-tiktok'#line:663
for line in open (user_file ,'r'):#line:665
    usernames .put (line .strip ())#line:666
usersize =usernames .qsize ()#line:668
if p_file =='':#line:670
    pass #line:671
else :#line:672
    for line in open (p_file ,'r'):#line:673
        p_pr .put (line .strip ())#line:674
proxsize =p_pr .qsize ()#line:675
clear ()#line:676
print (f"{Fore.YELLOW}Awakening Zeus")#line:678
time .sleep (1 )#line:679
with open (ss_file ,'r')as fp :#line:683
    content =fp .readlines ()#line:684
    x =len (content )#line:685
    m =str (x )#line:686
    if x ==1 :#line:687
        ssid1 =content [0 ]#line:688
        ssid2 ='none'#line:689
        ssid3 ='none'#line:690
        ssid4 ='none'#line:691
        ssid5 ='none'#line:692
    elif x ==2 :#line:693
        ssid1 =content [0 ]#line:694
        ssid2 =content [1 ]#line:695
        ssid3 ='none'#line:696
        ssid4 ='none'#line:697
        ssid5 ='none'#line:698
    elif x ==3 :#line:699
        ssid1 =content [0 ]#line:700
        ssid2 =content [1 ]#line:701
        ssid3 =content [2 ]#line:702
        ssid4 ='none'#line:703
        ssid5 ='none'#line:704
    elif x ==4 :#line:705
        ssid1 =content [0 ]#line:706
        ssid2 =content [1 ]#line:707
        ssid3 =content [2 ]#line:708
        ssid4 =content [3 ]#line:709
        ssid5 ='none'#line:710
    elif x ==5 :#line:711
        ssid1 =content [0 ]#line:712
        ssid2 =content [1 ]#line:713
        ssid3 =content [2 ]#line:714
        ssid4 =content [3 ]#line:715
        ssid5 =content [4 ]#line:716
ssid =ssid1 #line:717
clear ()#line:718
print (f'''
            {Fore.RED}[Sessions]
            {Fore.RESET}{Fore.GREEN}
         1: {ssid1}
         2: {ssid2}
         3: {ssid3}
         4: {ssid4}
         5: {ssid5}
         ''')#line:727
time .sleep (4 )#line:728
clear ()#line:729
if m =='':#line:731
    print (f"[{Fore.RED}>{Fore.RESET}] No valid ssids to continue with")#line:732
    quit (1 )#line:733
changenick ()#line:734
threading .Thread (target =printt ).start ()#line:735
thread =[]#line:737
for i in range (threads ):#line:738
    t =threading .Thread (target =claim )#line:739
    t .daemon =True #line:740
    t .start ()#line:741
    thread .append (t )#line:742
for threads in thread :#line:743
    threads .join ()