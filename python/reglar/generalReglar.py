'''常用的正则表达式

常用的symbol
1> . 表示所有字符包括它本身
2> + 表示前面一个字符或子表达式可以重复一次或多次,比如说"ab+"能匹配"abbbbb",但不能匹配"a"
3> * 表示前面一个字符或子表达式可以重复0次或多次，比如说"ab+"能匹配"a"以及"abbb"
4> ? 表示匹配一个字符或子表达式可以重复0到1次，
4> \ 转义符号，比如像让匹配规则自匹配一星号*，"\*"
5> [] 表示中括号内的字符任意一个
6> [^...] 表示除了其后面的字符，其他都匹配。
7> () 表示一个子表达式的起始位置如：(sd)* 同时也用来表示需要提取的字符内容
1、校验数字相关
2、
''' 

import re

#---------------------1
p1 = r'[0-9]+' #匹配一个
print(re.findall(p1,"123sdd"))

partern = re.compile(p1)
print((re.search(partern,"123sd12")).group())


















