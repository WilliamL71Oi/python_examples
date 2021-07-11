import re
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
