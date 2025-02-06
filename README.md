# DNS-Unlock

欢迎使用DNS-Unlock！！！本项目致力于DNS实现网络解锁与加速功能。

注意!!!本应用不能翻越长城防火墙,防火墙黑名单的域名一律不准访问!!!

## 原理简述

利用DNS重写功能，对网站的来源进行重写并根据 TCP 会话初始请求中包含的主机名，代理传入的 HTTP 和 TLS 连接。这样，无需在代理机上安装私钥，就能将基于 HTTPS 名称的虚拟主机连接到独立的后端服务器。将特定网站的DNS解析重定向到[SNIproxy](https://github.com/dlundquist/sniproxy) 反向代理来实现对网站的加速的效果。

## 使用方法

我们需要从解锁的方式来区分不同需求用户来使用改服务!!!

### 普通方法

请您更具您的需求点击下面的链接地址:

1. [DNS解锁使用DNS - UNLOCK](md/DNS.md)
2. [本地解锁使用 DNS - UNLOCK](md/Local.md)
3. [使用VPS 搭配 DNS - UNLOCK](md/VPS.md)

### 高级用法

我们继续延续了某些用户需要API来实现高级操作采用 [Swagger API](https://swagger.io/)
提供接口方法,请您点击 [dns_unlock.swagger.json](api/dns_unlock.swagger.json) 获取其中的json格式文件用于导入支持Swagger
API 的程序来使用.

