



# 如果同时匹配了多个节点，但只需要其中的某一节点时，可以使用指定索引的方式获取对应的节点内容，不过xpath中的索引是从1开始的。
from lxml import etree

html_str = '''
<div class="video_scroll">
<li> <a href="javascript:" onclick="login(0)" title="Java API文档">Java API文档</a> </li>
<li> <a href="javascript:" onclick="login(0)" title="JDK的下载">JDK的下载</a> </li>
<li> <a href="Javascript:" onclick="login(0)" title="JDK的安装">JDK的安装</a> </li>
<li> <a href="javascript:" onclick="login(0)" title="配置JDK">配置JDK</a> </li>
</div>
'''
html = etree.HTML(html_str)
# 获取所有li/a节点中title属性值
li_all = html.xpath('//div/li/a/@title')
print("所有属性值: ", li_all)
# 获取第一个li/a节点中title属性值
li_first = html.xpath('//div/li[1]/a/@title')
print("第一个属性值: ", li_first)
# 获取第四个li/a节点中title属性值
li_four = html.xpath('//div/li[4]/a/@title')
print('第四个属性值：', li_four)

结果：
所有属性值:  ['Java API文档', 'JDK的下载', 'JDK的安装', '配置JDK']
第一个属性值:  ['Java API文档']
第四个属性值： ['配置JDK']


# 除了固定的索引来获取指定节点中的内容以外，还可以使用xpath中提供的函数来获取指定节点中的内容。
from lxml import etree

html_str = '''
<div class="video_scroll">
<li> <a href="javascript:" onclick="login(0)" title="Java API文档">Java API文档</a> </li>
<li> <a href="javascript:" onclick="login(0)" title="JDK的下载">JDK的下载</a> </li>
<li> <a href="Javascript:" onclick="login(0)" title="JDK的安装">JDK的安装</a> </li>
<li> <a href="javascript:" onclick="login(0)" title="配置JDK">配置JDK</a> </li>
</div>
'''
html = etree.HTML(html_str)
# 获取最后一个li/a节点中title属性值
li_last = html.xpath('//div/li[last()]/a/@title')
print('最后一个属性值：', li_last)
# 获取第一个li/a节点中title属性值
li = html.xpath('//div/li[position()=1]/a/@title')
print('第一个位置的属性值：', li)
# 获取倒数第二个li/a节点中title属性值
li = html.xpath('//div/li[last()-1]/a/@title')
print('倒数第二个位置的属性值：', li)
# 获取位置大于1的li/a节点中title属性值
li = html.xpath('//div/li[position()>1]/a/@title')
print('位置大于1的属性值：', li)

结果：
最后一个属性值： ['配置JDK']
第一个位置的属性值： ['Java API文档']
倒数第二个位置的属性值： ['JDK的安装']
位置大于1的属性值： ['JDK的下载', 'JDK的安装', '配置JDK']



# xpath提供了一些节点轴的匹配方法，例如，获取祖节点、子孙节点、兄弟节点等。
from lxml import etree

html_str = '''
<div class="video_scroll">
<li> <a href="javascript:" onclick="login(0)" title="Java API文档">Java API文档</a> </li>
<li> <a href="javascript:" onclick="login(0)" title="JDK的下载">JDK的下载</a> </li>
<li> <a href="Javascript:" onclick="login(0)" title="JDK的安装">JDK的安装</a> </li>
<li> <a href="javascript:" onclick="login(0)" title="配置JDK">配置JDK</a> </li>
</div>
'''
html = etree.HTML(html_str)
ancestors = html.xpath('//li[2]/ancestor::*')
print('li[2]所有祖先节点名称：', [i.tag for i in ancestors])
body = html.xpath('//li[2]/ancestor::body')
print('li[2]指定祖先节点名称：', [i.tag for i in body])
class_div = html.xpath('//li[2]/ancestor::*[@class="video_scroll"]')
print('li[2]class="video_scroll"的祖先节点名称：', [i.tag for i in class_div])
attributes = html.xpath('//li[2]/a/attribute::*')
print('li[2]/a的所有属性值：', attributes)
div_chlid = html.xpath('//div/child::*')
print('div的所有子节点名称：', [i.tag for i in div_chlid])
body_descendant = html.xpath('//body/descendant::*')
print('body的所有子孙节点名称：', [i.tag for i in body_descendant])
li_following = html.xpath('//li[1]/following::*')
print('li[1]之后的所有节点名称：', [i.tag for i in li_following])
li_sibling = html.xpath('//li[1]/following::*')
print('li[1]之后的所有同级节点名称：', [i.tag for i in li_sibling])
li_preceding = html.xpath('//li[3]/preceding::*')
print('li[3]之前的所有节点名称：', [i.tag for i in li_preceding])

结果：
li[2]所有祖先节点名称： ['html', 'body', 'div']
li[2]指定祖先节点名称： ['body']
li[2]class="video_scroll"的祖先节点名称： ['div']
li[2]/a的所有属性值： ['javascript:', 'login(0)', 'JDK的下载']
div的所有子节点名称： ['li', 'li', 'li', 'li']
body的所有子孙节点名称： ['div', 'li', 'a', 'li', 'a', 'li', 'a', 'li', 'a']
li[1]之后的所有节点名称： ['li', 'a', 'li', 'a', 'li', 'a']
li[1]之后的所有同级节点名称： ['li', 'a', 'li', 'a', 'li', 'a']
li[3]之前的所有节点名称： ['li', 'a', 'li', 'a']

