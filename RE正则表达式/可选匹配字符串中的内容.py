import re
# "?" 可以理解为可选符号， 通过该符号即可实现可选匹配字符串中的内容。
# (\d?)+表示多个数字可有可无
# \s空格可有可无
# ([\u4e00-\u9fa5]?)+多个汉字可有可无
pattern = '(\d)?+mrsoft\s?([\u4e00-\u9fa5]?)+'
match = re.search(pattern, '01mrsoft')
print(match)
match = re.search(pattern, 'mrsoft')
print(match)
match = re.search(pattern, 'mrsoft ')
print(match)
match = re.search(pattern, 'mrsoft 第一')
print(match)
match = re.search(pattern, 'rsoft 第一')
print(match)

# 从以上的运行结果中可以看出，"01mrsoft" "mrsoft" "mrsoft " "mrsoft 第一" 均可匹配成功，只有"rsoft 第一"没有匹配成功，因为该字符中没有一个完整的mrsoft。
