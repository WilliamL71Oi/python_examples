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
