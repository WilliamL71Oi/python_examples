
# 在获取HTML代码中的所有节点时，可以使用"//*"的方式
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
node_all = html.xpath('//*')
print("数据类型：", type(node_all))
print("数据长度：", len(node_all))
print("数据内容：", node_all)
print("节点名称：", [i.tag for i in node_all])

结果：
数据类型： <class 'list'>
数据长度： 11
数据内容： [<Element html at 0x5a5dc88>, <Element body at 0x5aa52d8>, <Element div at 0x5aa52b0>, <Element li at 0x5aa5288>, <Element a at 0x5aa5260>, <Element li at 0x5aa5238>, <Element a at 0x5aa1f30>, <Element li at 0x5aa1b48>, <Element a at 0x5aa1760>, <Element li at 0x5aa1990>, <Element a at 0x5aa1738>]
节点名称： ['html', 'body', 'div', 'li', 'a', 'li', 'a', 'li', 'a', 'li', 'a']



# 如果需要获取HTML代码中所有指定名称的节点，可以在"//"的后面添加节点的名称。以获取所有"li"节点为例。
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
li_all = html.xpath('//li')
print('所有li节点',li_all)
print('获取指定li节点：',li_all[1])
li_txt = etree.tostring(li_all[1],encoding='utf-8')
print('获取指定节点HTML代码：',li_txt.decode('utf-8'))

结果：
所有li节点 [<Element li at 0x5df5378>, <Element li at 0x5df5350>, <Element li at 0x5df5328>, <Element li at 0x5df5300>]
获取指定li节点： <Element li at 0x5df5350>
获取指定节点HTML代码： <li> <a href="javascript:" onclick="login(0)" title="JDK的下载">JDK的下载</a> </li>


# "//"可以用来获取直接的子节点，如果需要获取子孙节点时，就可以使用"//"来实现，以获取ul节点中所有子孙节点a为例。
# 在获取ul子孙节点时，如果使用"//ul/a"的方式获取，是无法匹配任何结果的。因为"/"用来获取直接子节点，ul的直接子节点为li，并没有a节点，所以无法匹配。
from lxml import etree

html_str = '''
<div class="level one on">
<ul>
<li>
<a href="/index/index/view/id/1.html" title="什么是java" class="on">什么是java</a>
<a>Java</a>
</li>
<li> <a href="javascript:" onclick="login(0)" title="java的版本">java的版本</a> </li>
<li>
<a href="javascript:" onclick="login(0)" title="javaAPT文档">
<a>a节点中的节点</a>
</a>
</li>
</ul>
</div>
'''
html = etree.HTML(html_str)
a_all = html.xpath('//ul//a')
print('所有子节点a', a_all)
print('获取指定a节点：',a_all[4])
a_txt = etree.tostring(a_all[4],encoding='utf-8')
print('获取指定节点HTML代码：',a_txt.decode('utf-8'))

结果：
所有子节点a [<Element a at 0x4f95300>, <Element a at 0x4f952d8>, <Element a at 0x4f952b0>, <Element a at 0x4f95288>, <Element a at 0x4f95260>]
获取指定a节点： <Element a at 0x4f95260>
获取指定节点HTML代码： <a>a节点中的节点</a>



# 在获取一个节点的父节点时，可以使用".."来实现，以获取所有a节点的父节点为例。
# 除了使用".."获取第一个节点的父节点以外，还可以使用"/parent::*"的方式来获取。

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
a_all_parent = html.xpath('//a/..')
print('所有a的父节点', a_all_parent)
print('获取指定a的父节点：',a_all_parent[0])
a_txt = etree.tostring(a_all_parent[0], encoding='utf-8')
print('获取指定节点HTML代码：\n',a_txt.decode('utf-8'))

结果：
所有a的父节点 [<Element li at 0x4f45378>, <Element li at 0x4f45350>, <Element li at 0x4f45328>, <Element li at 0x4f45300>]
获取指定a的父节点： <Element li at 0x4f45378>
获取指定节点HTML代码：
 <li> <a href="javascript:" onclick="login(0)" title="Java API文档">Java API文档</a> </li>
  
 


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

