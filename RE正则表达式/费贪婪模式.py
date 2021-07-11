import re
# "(\d+)"并没有匹配我们所需要的结果123，而是只匹配了一个数字3而已。这是因为在贪婪匹配下".*"会尽量匹配更多的字符，而"\d+"表示至少匹配一个数字并没有指定数字的多少，
# 所以".*"将"www.hao12"全部匹配了，只把数字3留给"\d+"进行匹配，因为也就有了数字3的结果。
pattern = 'https://.*(\d+).com/'
match = re.findall(pattern, 'https://www.hao123.com/')
print(match)


# 非贪婪模式".*?"可以尽量匹配更少的字符，但不会影响我们需要匹配的数据
pattern2 = 'https://.*?(\d+).com/'
match2 = re.findall(pattern2, 'https://www.hao123.com/')
print(match2)

# 非贪婪匹配虽然有一定的优势，但是如果需要匹配的结果在字符串的尾部时，".*?"就很有可能匹配不到任何内容，因为它会尽量匹配更少的字符。
pattern3 = 'https://(.*?)'
match3 = re.findall(pattern3, 'https://www.hao123.com/')
print(match3)
pattern4 = 'https://(.*)'
match4 = re.findall(pattern4, 'https://www.hao123.com/')
print(match4)
