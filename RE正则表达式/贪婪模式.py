import re
# "."可以匹配除换行符以外的任意字符，而"*"表示匹配前面字符0次或无限次,当它们组合在一起时变成了万能的匹配方式。
pattern = 'https://.*/'
# 匹配成功后将打印字符串的所有内容，如果只需要单独获取".*"所匹配的中间内容时，可以使用"(.*)"的方式进行匹配
pattern2 = 'https://(.*)/'
match = re.findall(pattern, 'https://www.hao123.com/')
match2 = re.findall(pattern2, 'https://www.hao123.com/')
print(match)
print(match2)
