#!/usr/bin/env python
# -*- coding=utf-8 -*-

import requests
import pandas
from lxml import etree

ip_table = pandas.read_excel('ip.xlsx')
ip = ip_table['ip']
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}
for i in ip:
    proxyes = {'http':'http://{ip}'.format(ip=i),
               'https':'https://{ip}'.format(ip=i)}
    try:
        response = requests.get('http://202020.ip138.com',headers=headers,proxyes=proxyes,timeout=2)
        if response.status_code == 200:
            response.encoding = 'utf-8':
            html = etree.HTML(response.text)
            info = html.xpath('/html/body/p[1]//text()')
            print(info)
    except Exception as e:
        pass
        print('错误异常信息为：',e)
