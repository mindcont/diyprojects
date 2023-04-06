<img src="https://cdn-mindcont.opengps.cn/blog/images/iot/diy-user-avatars.png" width ="256px">

我们的愿景是打造一款基于树莓派的智能家居中心。它的特点不在于重复制造轮子，而是集成现有的开源方案，提供一种低成本、透明、实用的整体解决方案。

### TODO列表

- [x] 1 基础能力（远程界面、穿透内网、状态检测）
- [x] 2 智能相册（feh + mplayer + seafile，见pi-frame文件夹）
- [x] 3 天气报时（天气api+tts语音合成，见weather文件夹）
- [x] 4 远程推流（motion + frp + ifttt通知推送）
- [x] 5 每日一歌（自动抓取网易用户歌单，并随机播放一首，见cloudmusic文件夹）
- [x] 6 iphone图片热力轨迹(见gps文件夹)


### Acknowledgements

| | | |
|:------:|:------:|:------:|
|<a herf="http://raspberrypi.org"><img  src="https://www.home-assistant.io/images/supported_brands/raspberry-pi.png" alt="raspberrypi" width="64px"> <p>Raspberry Pi</p> </a> |<a herf="https://github.com/haiwen/seafile"><img  src="https://www.rosehosting.com/blog/wp-content/uploads/2015/03/seafile-logo.png" alt="seafile" width="64px" > <p>Seafile</p> </a>|<a herf="http://www.mplayerhq.hu/design7/news.html"><img  src="https://upload.wikimedia.org/wikipedia/commons/8/81/MPlayer.svg" alt="mplayer" width="80px"> <p>MPlayer</p> </a>|
|<a herf="https://github.com/Motion-Project/motion"><img  src="https://motion-project.github.io/motion.gif" alt="motion" width="96px"> <p>Motion</p> </a> |<a herf="https://github.com/home-assistant/home-assistant"><img  src="http://d33wubrfki0l68.cloudfront.net/075995fe17a5351e2699b2dd878652ec4f1d8654/8bfdd/demo/favicon-192x192.png" alt="home-assistant" width="64px"> <p>Home Assistant</p> </a>|<a herf="https://ifttt.com"><img  src="https://www.home-assistant.io/images/supported_brands/ifttt.png"  alt="ifttt" width="96px"> <p>IFTTT</p> </a>|
|<a herf="https://github.com/wzpan/wukong-robot"><img src="https://camo.githubusercontent.com/fa4d1a09384eade716bfc63f6bd92b3df09b5d812a5c686cb137eb971d2f389c/687474703a2f2f68616861636b2d313235333533373037302e66696c652e6d7971636c6f75642e636f6d2f696d616765732f77756b6f6e672d69636f6e732f3235365f3235362e706e67" alt="wukong-robot" width="64px"> <p>wukong-robot</p> </a>

其他工具和api接口
- [Frp](https://github.com/fatedier/frp)
- [Homebridge](https://github.com/nfarina/homebridge)
- [Wechatpy](http://wechatpy.readthedocs.io/zh_CN/master/)
- [和风天气](https://www.heweather.com/)
- [百度语音合成](http://yuyin.baidu.com/docs/tts/196)
- [网易云音乐-第三方API](https://music.wio.me)
