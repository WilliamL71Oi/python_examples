import requests
from bs4 import BeautifulSoup
# 伪造请求头，防止服务器端触发反爬机制
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
# 爬取目标网站的地址
res = requests.get('https://icp.aizhan.com/www.baidu.com/', headers=headers)
try:
    # BeautifulSoup可以读取HTML文件进行解析
    soup = BeautifulSoup(res.text, 'lxml')
# 找到需要爬取内容的DOM位置
    div = soup.find('div', attrs={'id': 'icp-table'})
    td_list = div.find_all('td')
# 使用: nth - child(n)选择器匹配父元素中的第n个子元素
# https: // icp.aizhan.com / www.baidu.com /
# icp - table > table > tbody > tr: nth - child(3) > td:nth - child(2) > span
    icp = soup.select('#icp-table > table > tbody > tr:nth-of-type(3) > td:nth-of-type(2) > span')
    if len(icp):
        print(icp[0].get_text())
    # 遍历构造打印出来的内容
    for i in range(0, len(td_list), 2):
        info = td_list[i].text + ":" + td_list[i + 1].text
        print(info)
        print("-" * 20)

except ConnectionError:
    print("网站连接失败")
