# -*- coding: utf-8 -*-
# @Time     : 2017/1/15 15:16
# @Author   : woodenrobot
# @url      ： https://zhuanlan.zhihu.com/p/24983204

import os
import sys
import re
import json
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import time,sys,urllib,urllib2,hashlib,base64,time,binascii

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit'
                      '/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safar'
                      'i/537.36',
    }


def numtozh(num):
    num_dict = {1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六', 7: '七',
                8: '八', 9: '九', 0: '零'}
    num = int(num)
    if 100 <= num < 1000:
        b_num = num // 100
        s_num = (num-b_num*100) // 10
        g_num = (num-b_num*100) % 10
        if g_num == 0 and s_num == 0:
            num = '%s百' % (num_dict[b_num])
        elif s_num == 0:
            num = '%s百%s%s' % (num_dict[b_num], num_dict.get(s_num, ''), num_dict.get(g_num, ''))
        elif g_num == 0:
            num = '%s百%s十' % (num_dict[b_num], num_dict.get(s_num, ''))
        else:
            num = '%s百%s十%s' % (num_dict[b_num], num_dict.get(s_num, ''), num_dict.get(g_num, ''))
    elif 10 <= num < 100:
        s_num = num // 10
        g_num = (num-s_num*10) % 10
        if g_num == 0:
            g_num = ''
        num = '%s十%s' % (num_dict[s_num], num_dict.get(g_num, ''))
    elif 0 <= num < 10:
        g_num = num
        num = '%s' % (num_dict[g_num])
    elif -10 < num < 0:
        g_num = -num
        num = '零下%s' % (num_dict[g_num])
    elif -100 < num <= -10:
        num = -num
        s_num = num // 10
        g_num = (num-s_num*10) % 10
        if g_num == 0:
            g_num = ''
        num = '零下%s十%s' % (num_dict[s_num], num_dict.get(g_num, ''))
    return num


def get_weather():
    # 下载墨迹天气主页源码
    res = requests.get('http://tianqi.moji.com/', headers=headers)
    # 用BeautifulSoup获取所需信息
    soup = BeautifulSoup(res.text, "html.parser")

    # 依次为： 温度 天气 湿度 风向 空气质量 个性导语
    temp = soup.find('div', attrs={'class': 'wea_weather clearfix'}).em.getText()
    temp = numtozh(int(temp))
    weather = soup.find('div', attrs={'class': 'wea_weather clearfix'}).b.getText().encode("utf-8")
    sd = soup.find('div', attrs={'class': 'wea_about clearfix'}).span.getText()
    sd_num = re.search(r'\d+', sd).group()
    sd_num_zh = numtozh(int(sd_num)).decode("utf-8")
    sd = sd.replace(sd_num, sd_num_zh)
    sd = sd.replace(' ', '百分之'.decode("utf-8")).replace('%', '')
    wind = soup.find('div', attrs={'class': 'wea_about clearfix'}).em.getText().encode("utf-8")
    aqi = soup.find('div', attrs={'class': 'wea_alert clearfix'}).em.getText()
    aqi_num = re.search(r'\d+', aqi).group()
    aqi_num_zh = numtozh(int(aqi_num)).decode("utf-8")
    aqi = aqi.replace(aqi_num, aqi_num_zh).replace(' ', ',空气质量'.decode("utf-8"))
    # aqi = 'aqi' + aqi
    info = soup.find('div', attrs={'class': 'wea_tips clearfix'}).em.getText()
    info = info.replace('，'.decode("utf-8"), ',')

    # 获取今天的日期
    today = datetime.now().date().strftime('%Y年%m月%d日')

    # 将获取的信息拼接成一句话
    text = '早上好！今天是%s,天气%s,温度%s摄氏度,%s,%s,%s,%s' % \
           (today, weather, temp, sd.encode("utf-8"), wind, aqi.encode("utf-8"), info.encode("utf-8"))
    return text


# 和风天气签名生成算法-Python版本
# params API调用的请求参数集合的关联数组（全部需要传递的参数组成的数组），不包含sign参数
# secret 用户的认证 key
# return string 返回参数签名值
def weather_api_sign(params, secret):
    canstring = ''
    #先将参数以其参数名的字典序升序进行排序
    params = sorted(params.items(), key=lambda item:item[0])
    #遍历排序后的参数数组中的每一个key/value对
    for k,v in params:
        if( k != 'sign' and k != 'key' and v != '') :
         canstring +=  k + '=' + v + '&'
    canstring = canstring[:-1]
    canstring += secret
    md5 = hashlib.md5(canstring).digest()
    return base64.b64encode(md5)


def get_weather_api():

    # weather.com.cn api(作废)
    # 大连天气
    # http://www.weather.com.cn/data/cityinfo/101070201.html
    # http://www.weather.com.cn/data/sk/101070201.html
    #
    # weather_host = 'http://www.weather.com.cn/data/cityinfo/101070201.html'
    # res = requests.get(weather_host)
    # mjson = json.loads(res.content)
    #
    # time = mjson['weatherinfo']['ptime'].encode('utf-8')
    # weather = mjson['weatherinfo']['weather'].encode('utf-8')
    # lowTemp = mjson['weatherinfo']['temp1'].encode('utf-8')
    # hightTemp = mjson['weatherinfo']['temp2'].encode('utf-8')
    #
    # # 将获取的信息拼接成一句话
    # text = '现在是%s,天气%s,最高温度%s,最低温度%s '% \
    #        (time, weather, lowTemp, hightTemp)
    # return text

    # 和风天气api
    # 请求示例 https://free-api.heweather.com/s6/weather/now?&key=******************************** \
    # &location=%E5%8C%97%E4%BA%AC
    # 返回参数详见 https://www.heweather.com/documents/api/s6/weather-now

    # 无签名请求方式
    # weather_host_withoutSign = 'https://free-api.heweather.com/s6/weather/now?' \
    #                '&key=********************************&location=大连'

    # 签名请求方式
    weather_host = "https://free-api.heweather.com/s6/weather/now?"
    secret_key = "********************************"
    username = "HE1804122025361292"
    location = '大连'
    timestamp = str(int(time.time()))
    params = {'location':location,'username':username,'t':timestamp}
    sign = weather_api_sign(params,secret_key)
    url = weather_host + '&username='+ username  + '&t='+ timestamp +  '&location='+ location + '&sign='+ sign
    res = requests.get(url,headers=headers,timeout=3)
    mjson = json.loads(res.text)
    # print mjson

    # 报时日期
    today = datetime.now().date().strftime('%m月%d日')
    weekday = str(datetime.now().weekday()+1)
    nowHours = datetime.now().strftime('%H点%M分')
    ntime = today + '星期'+weekday + ','+nowHours

    # 处理请求失败的情况
    if mjson['HeWeather6'][0]['status'] =='ok':
        nWeather = mjson['HeWeather6'][0]['now']

        # 依次为 天气、温度、体感温度、相对湿度、风向 风力 风速
        weather =nWeather['cond_txt'].encode('utf-8')
        tmp = nWeather['tmp'].encode('utf-8')
        fl = nWeather['fl'].encode('utf-8')
        hum = nWeather['hum'].encode('utf-8')
        wind_dir = nWeather['wind_dir'].encode('utf-8')
        wind_sc = nWeather['wind_sc'].encode('utf-8')
        wind_spd = nWeather['wind_spd'].encode('utf-8')
        # print weather,tmp,fl,hum,wind_dir,wind_sc,wind_spd

        # 将获取的信息拼接成一句话
        text = '现在是%s,天气%s,室外温度%s摄氏度,体感温度%s摄氏度,%s，%s级, 风速%s公里每小时,记得注意休息'% \
               (ntime, weather, tmp, fl, wind_dir, wind_sc, wind_spd)

    else :
        print mjson['HeWeather6'][0]['status']
        text = '现在是%s' %(ntime)

    return text


def text2voice(text):

    # 百度语音合成请求地址 http://tts.baidu.com/text2audio?
    # 接口文档：http://yuyin.baidu.com/docs/tts/196
    # 参数示意：
    #         tex 待合成文本
    #         lang   语言选择, 填写zh
    #         ctp 客户端类型选择，web端填写1
    #         spd  语速，取值0 - 9，默认为5中语速
    #         pit 音调，取值0 - 9，默认为5中语调
    #         vol 音量，取值0 - 15，默认为5中音量
    #         per 发音人选择, 0为女声，1为男声，3 为情感合成 - 度逍遥，4为情感合成 - 度丫丫，默认为普通女

    url = 'http://tts.baidu.com/text2audio?idx=1&tex={0}&cuid=baidu_speech_demo' \
          '&pdt=1&cod=2&lan=zh&ctp=1&spd=5&pit=5&vol=5&per=0'.format(text)

    # 调用mplayer直接播放语音
    os.system('mplayer "%s"' % url)

def main():
    # 获取需要转换语音的文字
    # text = get_weather()
    # print(text)
    text = get_weather_api()
    print text

    # 获取音乐文件绝对地址
    mp3path = os.path.join(os.path.dirname(__file__), 'alarm.wav')
    # 先播放一首音乐做闹钟
    os.system('mplayer %s' % mp3path)

    # 播报语音天气
    text2voice(text)


if __name__ == '__main__':
    main()
