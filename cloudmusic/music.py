# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 17:07:23 2019

@author: aotodata

微信公众号: 凹凸数读

微信公众号: 凹凸玩数据
"""
import os
import random
import time

import jsonpath
import requests
from fake_useragent import UserAgent
from pyquery import PyQuery as pq

ua = UserAgent()
headers = {'User-Agent': ua.random}


def restaurant(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
    except Exception:
        print('此页有问题！')
        return None


def get_json(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            json_text = response.json()
            return json_text
    except Exception:
        print('此页有问题！')
        return None


def get_list():
    list1 = []
    for i in range(0, 35, 35):  # 跑一页试试，如果跑全部，改为 range(0,1295,35)
        url = 'https://music.163.com/discover/playlist/?order=hot&cat=%E5%8D%8E%E8%AF%AD&limit=35&offset=' + str(i)
        print('已成功采集%i页歌单\n' % (i / 35 + 1))
        data = []
        print(url)
        html = restaurant(url)
        doc = pq(html)
        for i in range(1, 36):  # 一页35个歌单
            a = doc('#m-pl-container > li:nth-child(' + str(i) + ') > div > a').attr('href')
            a1 = 'https://music.163.com/api' + a.replace('?', '/detail?')
            data.append(a1)
        list1.extend(data)
        time.sleep(5 + random.random())
    return list1


# 获取歌单和下载音乐
def get_music():
    """
    https://music.163.com/#/user/home?id=291775263
    https://music.163.com/#/playlist?id=720833877
    https://music.163.com/#/my/m/music/playlist?id=3167379544

    #获取用户歌单
    https://music.wio.me/user/playlist?uid=291775263

    #获取音乐url
    /song/url?id=33894312
    #获取歌单详情
    https://music.wio.me/playlist/detail?id=720833877

    https://music.wio.me/playlist/detail?id=3167379544
    """

    url = 'https://music.wio.me/playlist/detail?id=3167379544'

    # 日志
    with open('../log.txt', 'a') as log:
        # 日志头部
        log.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n')
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        log.write("=====================================================\n")
        print("=====================================================")
        # 获取歌单json
        data = []
        doc = get_json(url)
        jobs = doc['playlist']['tracks']
        index = 0
        for job in jobs:
            dic = {}
            # 序号自加+
            index += 1
            dic['number'] = index  # 序号
            dic['name'] = jsonpath.jsonpath(job, '$..name')[0]  # 歌曲名称
            dic['id'] = jsonpath.jsonpath(job, '$..id')[0]  # 歌曲ID
            dic['artists'] = jsonpath.jsonpath(job, '$..ar')[0][0]['name']  # 歌手
            dic['album'] = jsonpath.jsonpath(job, '$..al')[0]['name']  # 专辑
            dic['duration'] = jsonpath.jsonpath(job, '$..dt')[0]  # 时长
            dic['url'] = 'http://music.163.com/song/media/outer/url?id=' + str(dic['id']) + '.mp3'  # 链接
            # print(dic)
            data.append(dic)

        # 下载歌曲
        if download:
            for i in data:
                # 判断歌曲是否已经下载
                if not os.path.exists(i['name'] + '.mp3'):
                    # 写入日志
                    log.write('正在下载第%i首歌曲, ' % i['number'] + i['name'] + "\n")
                    print('正在下载第%i首歌曲, ' % i['number'] + i['name'])
                    url = 'http://music.163.com/song/media/outer/url?id=' + str(i['id']) + '.mp3'
                    # print(url)
                    song = requests.get(url, headers=headers, stream=True)
                    with open(i['name'] + '.mp3', 'wb') as f:
                        for ch in song:
                            f.write(ch)
                        f.close()
                    time.sleep(5 + random.random())

        if enable_delete:
            # 判断文件大小，如果小于1M，则删除
            file_size = os.path.getsize(i['name'] + '.mp3')
            print(file_size / 1024 / 1024)
            if file_size < 1024 * 1024:
                os.remove(i['name'] + '.mp3')
                data.remove(i)
                log.write('删除了第%i首歌曲, ' % i['number'] + i['name'] + '.mp3' + "\n")
                # 删除第几首歌曲
                print('删除了第%i首歌曲, ' % i['number'] + i['name'] + '.mp3')

        ## 获取歌单信息,写入cloudmusic/myplaylist.txt
        with open('myplaylist.txt', 'w', encoding='utf-8') as f:
            f.write(str(data))
        f.close()
        log.write('歌单信息写入成功\n')
        print('歌单信息写入成功')
        log.close()


def play():
    # log日志
    with open('../log.txt', 'a') as log:
        # 读取歌单
        with open('myplaylist.txt', 'r', encoding='utf-8') as f:
            # 将读取的歌单转换为字典
            data = eval(f.read())
            # print(data)
            # 随机播放一首歌
            i = random.choice(data)
            log.write('正在播放' + i['name'] + "\n")
            print('正在播放' + i['name'])
            log.write('正在播放第%i首歌曲,' % i['number'] + " 来自 " + i['artists'] + " 的 " + i['name'] + ".mp3\n")
            print('正在播放第%i首歌曲,' % i['number'] + " 来自 " + i['artists'] + " 的 " + i['name'] + ".mp3")
            # print(i['name'])
            # print(i['artists'])
            # print(i['album'])
            # print(i['duration'])
            # print(i['url'])
            # 音乐路径
            music = i['name'] + '.mp3'
            # 播放音乐
            os.system('mplayer ' + music)
            log.write('播放结束\n')
            print('播放结束')
        f.close()
    log.close()


download = 1
enable_delete = 0
if __name__ == '__main__':
    get_music()
    play()
