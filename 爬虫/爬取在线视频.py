#!/usr/bin/env python
# -*- coding=utf-8 -*-

import requests
import re
# 定义视频播放页面的url
url = 'http://site2.rjkflm.com:666/index/index/view/id/1.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
response = requests.get(url=url, headers=headers)   # 发送网络请求
if response.status_code == 200:   # 判断请求成功后
    video_url = re.findall('<source src="(.*?)" type="video/mp4">', response.text)[0]
    video_url = 'http://site2.rjkflm.com:666/' + video_url    # 将视频地址拼接完整
    video_response = requests.get(url=video_url, headers=headers)   # 发送下载视频的网络请求
    if video_response.status_code == 200:
        data = video_response.content   # 获取返回的视频二进制数据
        file = open('java视频.mp4', 'wb')   # 创建open对象
        file.write(data) 
        file.close()
