#! /usr/bin/python3
# -*- coding: UTF-8 -*-

import requests
from lxml import etree
import pandas as pd
from requests.packages.urllib3.exceptions import InsecureRequestWarning

ip_list = []
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def get_ip(url, headers):
    response = requests.get(url, headers=headers, verify=False)
    response.encoding = 'utf-8'
    if response.status_code == 200:
        html = etree.HTML(response.text)
        li_all = html.xpath('//li[@class="f-list col-lg-12 col-md-12 col-sm-12 col-xs-12"]')
        for i in li_all:
            ip = i.xpath('span[@class="f-address"]/text()')[0]
            port = i.xpath('span[@class="f-port"]/text()')[0]
            ip_list.append(ip + ':' + port)
            print('代理ip为：', ip, '对应端口为：', port)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0'}

if __name__ == '__main__':
    ip_table = pd.DataFrame(columns=['ip'])
    for i in range(1, 5):
        url = 'https://www.dieniao.com/FreeProxy/{page}.html'.format(page=i)
        get_ip(url, headers)
    ip_table['ip'] = ip_list
    ip_table.to_excel('ip.xlsx', sheet_name='data')
