#!/usr/bin/env python
# -*- coding=utf-8 -*-

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys

def bing_search(site, pages):
    Subdomain = []
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
               'Accept': '*/*',
               'Accept-Language': 'en-US,en;q=0.5',
               'Accept-Encoding': 'gzip,deflate',
               'referer': "http://cn.bing.com/search?q=email+site%3abaidu.com&qs=n&sp=-1&pq=emailsite%3abaidu.com&first=2&FORM=PERE1"
               }
    for i in range(1, int(pages) + 1):
        # str((int(i)-1)*10)意思为每十页。
        url = "https://cn.bing.com/search?q=site%3a" + site + "&go=Search&qs=ds&first=" + str((int(i)-1)*10) + "&FORM=PERE"
        # 你使用session成功的登录类某个网站，则在再次使用该session对象请求该网站的其他网页都会默认使用该session之前使用的cookie等参数。
        conn = requests.session()
        conn.get('https://cn.bing.com', headers=headers)
        # stream：当true时，不会立即下载，当使用iter_content或iter_lines遍历内容或访问内容属性时才开始下载。注意：文件没有下载之前，也需要保持连接。
        html = conn.get(url, stream=True, headers=headers, timeout=8)
        # HTMLParser主要是用来解析HTML文件（包括HTML中无效的标记）。
        soup = BeautifulSoup(html.content, 'html.parser')
        job_bt = soup.findAll('h2')
        for i in job_bt:
            link = i.get('href')
            # https://www.baidu.com
            # scheme://netloc/path;parameters?query#fragment
            # scheme：获取链接中的http或者是https
            # netloc：获取了www.baidu.com
            domain = str(urlparse(link).scheme + "://" + urlparse(link).netloc)
            if domain in Subdomain:
                pass
            else:
                Subdomain.append(domain)
                print(domain)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        site = sys.argv[1]
        page = sys.argv[2]
    else:
        print("usage: %s baidu.com 10" % sys.argv[0])
        sys.exit(-1)
    Subdomain = bing_search(site, page)
