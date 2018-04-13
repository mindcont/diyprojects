# 天气报时

基于[和风天气](https://www.heweather.com/documents/api/s6/weather-now)和[百度语音合成](http://yuyin.baidu.com/docs/tts/196)的天气报时闹钟，感谢[木制robot](https://zhuanlan.zhihu.com/p/24983204)。

### 安装
安装依赖`mplayer`和`pulseaudio`

```css
# mplayer, voice player
$ sudo apt-get install mplayer pulseaudio
$ cd /home/pi/
$ git clone https://github.com/mindcont/diyprojects-raspbian diy
$ cd diy/weather
$ sudo pip install -r requirements.txt
```
注册[和风天气](https://console.heweather.com/register)免费开发者获取`key`

替换`weather_host.py`中`secret_key`即可。

```css
$ python weather_voice.py
```

#### 定时运行
例如，7-21点时间段内，正点报告当前时间和天气

```css
# minute   hour   day   month   week   command
0 7-21 * * * python /home/pi/iot/weather/weather_voice.py >> "/home/pi/iot/weather/log/weather_debug_$(date +"\%Y-\%m-\%d").log" 2>&1

```

### License
© 2018 张正轩 [知识共享 署名-非商业性使用](http://creativecommons.org/licenses/by-nc-sa/4.0/)
