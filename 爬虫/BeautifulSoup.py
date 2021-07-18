#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup

html_doc = '''
<html>
<head>
<title>横排响应登录</title>
<meta http-equiv="Content-Type" content="text/html" charset="utf-8"/>
<meta name="viewport" content="width=device-width"/>
<link href="font/css/bootstrap.min.css" type="text/css" rel="stylesheet">
<link href="css/style.css" type="text/css" rel="stylesheet">
</head>
</html>
'''

soup = BeautifulSoup(html_doc, features='lxml')
print("head节点内容如下：\n", soup.head)
print("head节点数据类型为：\n", type(soup.head))
print("head节点中的title节点内容如下：\n", soup.head.title)
print("head节点中的title节点数据类型为：\n", type(soup.head.title))
print("head节点中的title节点中的文本内容为：\n", soup.head.title.string)
print("head节点中的title节点中文本内容的数据类型为：\n", type(soup.head.title.string))
