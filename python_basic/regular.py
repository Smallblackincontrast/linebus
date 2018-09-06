import re

text = 'tsasaa<html>A<title>regular test</title>B</html>'

greedy_regular = re.compile('</?.+>')  # 贪婪匹配
none_greedy_regular = re.compile('</?.+?>')  # 非贪婪匹配

# match值匹配开头
match_result = re.match(greedy_regular, text)
print(match_result)

# search匹配所有
search_result = re.findall(greedy_regular, text)
print(search_result)

# 非贪婪模式,找到第一个就截止
search_result = re.findall(none_greedy_regular, text)
print(search_result)
