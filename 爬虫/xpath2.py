# 属性匹配

# 如果需要更精确地获取某个节点中的内容，可以使用"[@..]"实现节点属性的匹配，其中".."表示属性匹配的条件。例如，获取所有class="level"的所有div节点。
# 使用"[@..]"实现属性匹配时，不仅可以用于class属性的匹配，还可以用于id、href等属性的匹配。
from lxml import etree

html_str = '''
<div class="video_scroll">
<div class="level">什么是java</div>
<div class="level">java的版本</div>
</div>
'''
html = etree.HTML(html_str)
div_one = html.xpath('//div[@class="level"]/text()')
print(div_one)



# 如果某个节点的某个属性出现了多个值时，可以将所有值作为匹配条件，进行节点的筛选。
from lxml import etree

html_str = '''
<div class="video_scroll">
<div class="level one">什么是java</div>
<div class="level">java的版本</div>
</div>
'''
html = etree.HTML(html_str)
div_one = html.xpath('//div[@class="level one"]/text()')
print(div_one)



# 如果需要获取class="level one"又获取class="level"的div节点时，，可以使用contains()方法，该方法中邮两个参数，第一个参数用于指定属性名称，第二个参数用于指定属性值
# 如果HTML代码中包含指定的属性值，就可以匹配成功。
from lxml import etree

html_str = '''
<div class="video_scroll">
<div class="level one">什么是java</div>
<div class="level">java的版本</div>
</div>
'''
html = etree.HTML(html_str)
div_all = html.xpath('//div[contains(@class,"level")]/text()')
print(div_all)



# 多属性匹配
#通过属性匹配HTML代码的节点时，还会遇到一种情况：那就是一个节点中出现多个属性，这时就需要同时匹配多个属性，才可以更精确地获取指定节点中的数据。
from lxml import etree

html_str = '''
<div class="video_scroll">
<div class="level" id="one">什么是java</div>
<div class="level">java的版本</div>
</div>
'''
html = etree.HTML(html_str)
div_all = html.xpath('//div[@class="level" and @id="one"]/text()')
print(div_all)



# "@"不仅可以实现通过属性匹配节点，还可以直接获取属性所对应的值。

from lxml import etree

html_str = '''
<div class="video_scroll">
<li class="level" id="one">什么是java</li>
</div>
'''
html = etree.HTML(html_str)
li_class = html.xpath('//div/li/@class')
li_id = html.xpath('//div/li/@id')
print('class属性值：', li_class)
print('id属性值：', li_id)
