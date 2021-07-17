



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
li_all = html.xpath('//div/li/a/@title')
print("所有属性值: ", li_all)
li_first = html.xpath('//div/li[1]/a/@title')
print("第一个属性值: ", li_first)
li_four = html.xpath('//div/li[4]/a/@title')
print('第四个属性值：', li_four)

结果：
所有属性值:  ['Java API文档', 'JDK的下载', 'JDK的安装', '配置JDK']
第一个属性值:  ['Java API文档']
第四个属性值： ['配置JDK']


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
li_last = html.xpath('//div/li[last()]/a/@title')
print('最后一个属性值：', li_last)
li = html.xpath('//div/li[position()=1]/a/@title')
print('第一个位置的属性值：', li)
li = html.xpath('//div/li[last()-1]/a/@title')
print('倒数第二个位置的属性值：', li)
li = html.xpath('//div/li[position()>1]/a/@title')
print('位置大于1的属性值：', li)

结果：
最后一个属性值： ['配置JDK']
第一个位置的属性值： ['Java API文档']
倒数第二个位置的属性值： ['JDK的安装']
位置大于1的属性值： ['JDK的下载', 'JDK的安装', '配置JDK']

