#!/usr/bin/env python
# -*- coding=utf-8 -*-

from requests_html import HTMLSession, UserAgent    # 导入HTMLSession类

session = HTMLSession()     # 创建HTML会话对象
ua = UserAgent().random     # 创建随机请求

r = session.get('http://news.youth.cn/jsxw/index.htm', headers={'user-agent': ua})
r.encoding = 'gb2312'
if r.status_code == 200:       # 判断请求是否成功
    li_all = r.html.xpath('.//ul[@class="tj3_1"]/li')
    for li in li_all:       # 循环遍历每个<li>标签
        news_title = li.find('a')[0].text       # 提取新闻标题内容
        # 获取新闻详情对应的地址
        news_href = 'http://news.youth.cn/jsxw' + li.find('a[href]')[0].attrs.get('href').lstrip('.')
        news_time = li.find('font')[0].text     # 获取新闻发布的时间
        print('新闻标题为：', news_title)     # 打印新闻标题
        print('新闻url地址为：', news_href)   # 打印新闻URL地址
        print('新闻发布时间为:', news_time)   # 打印新闻发布时间

"""
#  可以使用find()方法中的containing参数，以获取关于"国家"相关新闻内容。
for li in r.html.find('li',containing='国家'):
    news_title = li.find('a')[0].text
    news_href = 'http://news.youth.cn/jsxw' + li.find('a[href]')[0].attrs.get('href').lstrip('')
    news_time = li.find('font')[0].text
    print("新闻标题为：",news_title)
    print('新闻url地址为：',news_href)
    print('新闻发布时间为:',news_time)

# search()方法表示查找符合条件的第一个元素。
for li in r.html.find('li', containing='国家'):
    a = li.search('<a href="{}">{}</a>')        # 获取<li>标签中<a>标签内的新闻地址与新闻标题
    news_title = a[1]       # 提取新闻标题
    news_href = 'https://news.youth.cn/jsxw' + a[0]     # 提取新闻地址
    news_time = li.search('<font>{}</font>')[0]
    print('新闻标题为：', news_title)
    print('新闻url地址为:', news_href)
    print("新闻发布时间为：", news_time)
    
# search_all()方法则表示符合条件的所有元素。
import re
class_tj3_1 = r.html.xpath('.//ul[@class="tj3_1"]')     # 获取class=tj3_1的标签
# 使用search_all()方法获取所有class=tj3_1中的<li>标签
li_all = class_tj3_1[0].search_all('<li>{}</li>')
for li in li_all:
    if "国家" in li[0]:   # 判断<li>标签内内容中是否存在关键字“国家”
    # 通过正则表达式获取<a>标签中的新闻信息
        a = re.findall('<font>(.*?)</font><a href="(.*?)">(.*?)</a>',li[0])
        news_title = a[0][2]
        news_href = 'http://news.youth.cn/jsxw' + a[0][1]
        news_time = a [0][0]
        print("新闻标题为：", news_title)
        print("新闻url地址为：", news_href)
        print("新闻发布时间为：", news_time)
