import re
# 如果字符串在开始处、结尾处，或者是字符串的分界符为空格、标点符号以及换行，可以使用"\b"匹配字符串的边界.
pattern = r'\bmr\b'  # 表达式，mr两则均有边界
match = re.search(pattern, 'mrsoft')  # 匹配字符串，mr右侧不是边界是soft，匹配失败
print(match)
match = re.search(pattern, 'mr soft')  # 匹配字符串， mr左侧为边界右侧为空格，匹配成功
print(match)
match = re.search(pattern, ' mrsoft ')  # 匹配字符串， mr左侧为空格右侧为soft空格，匹配失败
print(match)
match = re.search(pattern, 'mr .soft')  # 匹配字符串， mr左侧为边界右侧为"."，匹配成功
print(match)
# 表达式中的r表示"\b"不进行转义，如果将表达式中的r去掉将无法进行字符串边界的匹配。
