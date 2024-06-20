# DNS-Unlock
  DNS服务器方案即将取消，请大家更换DNS地址。
  目前dns解析通过 Adguard DNS 和 Cloudflare Zero Trust 提供，但是依旧需要代理服务器提供解锁服务。（解决了一部分部署DNS服务器的费用）缺点是DNS延迟相较于服务器DNS解析延迟较高。

## 使用的DNS服务(服务器若出现故障请及时上报
默认服务 [https://dns.afosne.icu/afosne](https://dns.afosne.icu/afosne)<br/>
#### 以下服务器目前仅支持Netflix 和 Disneyplus 等部分网站的加速.后续将持续更新服务
ANYCAST服务器[https://dns.afosne.icu/afosneanycast](https://dns.afosne.icu/afosneanycast)<br/>
澳大利亚服务器[https://dns.afosne.icu/afosneau](https://dns.afosne.icu/afosneau)<br/>
欧洲服务器[https://dns.afosne.icu/afosneeu](https://dns.afosne.icu/afosneeu)<br/>
香港服务器[https://dns.afosne.icu/afosnehk](https://dns.afosne.icu/afosnehk)<br/>
日本服务器[https://dns.afosne.icu/afosnejp](https://dns.afosne.icu/afosnejp)<br/>
韩国服务器[https://dns.afosne.icu/afosnekr](https://dns.afosne.icu/afosnekr)<br/>
新加坡服务器[https://dns.afosne.icu/afosnesg](https://dns.afosne.icu/afosnesg)<br/>
泰国服务器[https://dns.afosne.icu/afosneth](https://dns.afosne.icu/afosneth)<br/>
土耳其服务器[https://dns.afosne.icu/afosnetr](https://dns.afosne.icu/afosnetr)<br/>
台湾地区服务器[https://dns.afosne.icu/afosnetw](https://dns.afosne.icu/afosnetw)<br/>
美国服务器[https://dns.afosne.icu/afosneus](https://dns.afosne.icu/afosneus)<br/>
赞助服务器[https://dns.afosne.icu/afosnefreeany](https://dns.afosne.icu/afosnefreeany)<br/>

## 解锁用服务器探针
[https://status.afosne.icu/](https://status.afosne.icu/)

## 测试是否正确连接
  连接后访问网址[afosne.afosne](http://afosne.afosne/)若弹出nginx页面则DNS服务器连接正常，若不正常请尝试访问[browserleaks](https://browserleaks.com/dns)来测试你的dnsisp。{[afosne](https://dns.afosne.icu/dns-query)的isp为Cloudlfare，[afosnec](https://dns.afosne.icu/afosnec)的isp为NetActuate，[afosnea](https://dns.afosne.icu/afosnea)的isp为Datacamp Limited和Cdn77 LAX。}，若不是则您与dns服务器的连接出现故障。

## 使用教程

[不会使用，点击这里](/tutorial.md)


## 目前该服务已经提供的加速服务有
AFOSNE
- [x] Netflix 
- [x] Disneyplus.com 
- [x] Hulu 
- [x] 谷歌翻译
- [x] OP.GG
- [x] Spotify 播放列表加载和音频流
- [x] Notion 笔记
- [x] Cloudflare worker 和 pages
- [x] Github Github raw

AFOSNEC
      
- [x] Netflix 
- [x] disneyplus.com 


AFOSNEA（暂时停止提供解锁服务）

- [ ] Netflix 
- [ ] disneyplus.com 

# 后期维护和优化
目前开发客户端中，满足各个区服之间的解锁和使用。
后期尝试使用dns直接解锁登录Netflix，Disney，等网站会员共享等功能。
建立负载均衡以满足大量用户的需求。

# 后期维护和优化
有问题可以进入群组讨论 [Dns_Unlock](https://t.me/Dns_Unlock)
## 如何赞助

公益不宜，请大家多多支持,如有疑问请联系[7920a9c2@gmail.com](mailto:7920a9c2@gmail.com) 

![爱发电](/img/afd.jpg)

