# DNS-Unlock

本DNS服务部署于香港地区，且本DNS服务不提供任何翻越GFW的功能。
{发现新大陆，某场提供个人免费私有dns服务，等功能完善我会教程，无需服务器（优点，轻松简单，可以直连，且可以直接设置为私人dns使用，缺点是无法解析YouTube（解决了，但是要等轮询结束），telegram（目前没啥想法，搞不好）等服务，这些服务设置比较复杂，而且不太稳定），该服务将在教程推送后停止提供}

## 转移服务前期准备
### 解决方案
方案一 ： 利用Zero Trust 对域名进行
[dns.afosne.icu](https://dns.afosne.icu/dns-query)<br/>
[cdns.afosne.icu](https://cdns.afosne.icu/dns-query)<br/>
[adns.afosne.icu](https://adns.afosne.icu/dns-query)<br/>
### 查询接口：
https://dnsip.afosne.workers.dev/?domain=netflix.com （未完善）代码出现逻辑问题
### 部署接口：
详情见js目录（完善中)

## 使用教程

[不会使用，点击这里](/tutorial.md)

## DNS服务地址

域名已经被污染，将更改域名地址

DNS-over-HTTP：（失效） 

IP：141.11.75.124



## 目前该服务已经提供的加速服务有

1. Netflix 网飞 港区 （服务器提供商：绿云 绕美了，在优化路线）
2. Disney 迪士尼 美区 （服务器提供商：绿云 绕美了，在优化路线）
3. 谷歌翻译 
4. Github {github raw gist}（手机客户端可能会报错，但是浏览器加速没问题，具体问题在研究中）
5. Steam {商城，好友列表，创意工坊} 
6. Discord （目前测试失效）
7. Spotify 声田 港区 仅加速播放，无法加速登录页面
8. bilibili海外 
9. notion 笔记（更新中）
10. 育碧 {登录、云同步、相关的服务}
11. 幻兽帕鲁（已取消）
12. Epic {登录、商城、云同步}
13. hcaptcha 验证码
14. YouTube 直连 {移动、联通可能失效，且需要设备支持ipv6，解决办法:重进YouTube客户端???，反正我有效，若不行开启飞行模式后关闭} （解锁方法，轮询所有谷歌ip，找到未被gfw封禁的ip并自动切换解析地址，大概需要等待30秒后才能使用，速度极快）
15. telegram 直连 {可能失效，随缘解锁解决办法同YouTube} 
16. Tidal
17. TMDB
18. HBO
19. Hulu 葫芦 香港（服务器提供商：绿云 绕美了，在优化路线）


## 还在计划加速的网站

- [x] tidal
- [ ] R星类
- [x] 育碧类
- [ ] 烂橘子类
- [ ] EA类
- [x] TMDB
- [ ] 微软全家桶
- [x] hulu
- [x] HBO
- [ ] TVB
- [ ] AbemaTV
- [ ] Happyon
- [ ] Pandora
- [x] YouTube
- [x] telegram
- [ ] .........



## Other

由于本人时间有限，后续解锁服务有需求请提交Issues

由于本项目部署于香港地区，Dns查询延迟稍微有点高，且有部分地址只能通过ip访问该DNS（域名已被gfw识别且封禁此条请忽略），目前准备通过隧道中转以降低延迟。

目前项目预计增加不同地区的DNS服务器以解锁更多地区的流媒体或其他平台

## 如何赞助

公益不宜，请大家多多支持,如有疑问请联系[7920a9c2@gmail.com](mailto:7920a9c2@gmail.com) 

![爱发电](/img/afd.jpg)

