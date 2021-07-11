from requests_html import HTMLSession, UserAgent    # 导入HTMLSession类

session = HTMLSession()   # 创建HTML会话对象
ua = UserAgent().random   # 创建随机请求头
# 发送网络请求
r = session.get('https://movie.douban.com/tag/#/?sort=U&range=0,10&tags=2020', headers={'user-agent': ua})
r.encoding = 'gb2312'   # 编码
if r.status_code == 200:
    r.html.render()   # 调用render()方法，没有Chromium浏览器自动下载
class_wp = r.html.xpath('.//div[@class="list-wp"]/a')   # 获取当前页面中所有电影信息的a标签
for a in class_wp:
    title = a.find('p span')[0].text
    rate = a.find('p span')[1].text
    details_url = a.attrs.get('href')
    img_url = a.find('img')[0].attrs.get('src')
    print('电影名称为：', title)
    print('电影评分为：', rate)
    print('详情页面地址为：', details_url)
    print('图片地址为：', img_url)
