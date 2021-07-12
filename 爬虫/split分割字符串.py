import re
pattern = r'[?|&]'
url = 'http://mingrisoft.com/login.jsp?username="mr"&pwd="mrsoft"'
result = re.split(pattern, url)
print(result)


# 如果需要分割的字符串非常大，并且不希望使用模式字符串一直分割下去，此时可以指定split方法中的maxsplit参数来指定最大的分割次数。
import re
string = '预定|K7577|CCT|THL|CCT|LYL|14:47|16:51|02:04|Y|'
pattern = '\|'
match = re.split(pattern, string, maxsplit=1)
print(match)
