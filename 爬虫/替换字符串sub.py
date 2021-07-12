#!/usr/bin/env python
# -*- coding=utf-8 -*-

import re
pattern = r'1[34578]\d{9}'
string = '中奖号码为：84978981 联系电话为：13611111111'
result = re.sub(pattern, '1xxxxxxxxxx', string)
print(result)


# sub除了有替换字符串的功能外，还可以使用该方法实现删除字符串中我们不需要的数据。
import re
string = 'hk400 jhkj6h7k5 jhkjhk1j0k66'
pattern = '[a-z]'
match = re.sub(pattern, '', string, flags=re.I)
print(match)
