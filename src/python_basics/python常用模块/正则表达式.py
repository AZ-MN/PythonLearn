"""
正则表达式
简介
正则表达式是一种强大的文本处理工具，可以用于在字符串中进行模式匹配、搜索、替换等操作。
Python 的内置 re 模块，用于进行正则表达式操作，提供了一系列函数和方法，用于执行各种正则表达式操作。
"""

"""
常用正则表达式语法及含义
语法	        含义
普通字符	    大多数只会匹配字符本身
'.'	        匹配除换行符 \n 外的任意字符
'[]'	    匹配 [] 中列举的字符
'*'	        匹配前一个字符的零个或多个实例
'+'	        匹配前一个字符的一个或多个实例
'?'	        匹配前一个字符的零个或一个实例
'{m}'	    匹配前一个字符的 m 个实例
'{m, n}'	匹配前一个字符的 m 到 n 个实例
'^'	        匹配字符串的开头
'$'	        匹配字符串的结尾
'\d'	    匹配任意数字字符，相当于 [0-9]
'\D'	    匹配任意非数字字符，相当于除 [0-9]以外的字符
'\w'	    匹配任意字母、数字或下划线字符等非特殊字符，相当于 [a-zA-Z0-9_]
'\W'	    匹配任意除字母、数字或下划线字符以外的特殊字符，相当于除 [a-zA-Z0-9_] 以外的字符
'\s'	    匹配任意空白字符，如空格、制表符、换行等
'\S'	    匹配任意非空白字符
"""

# 常用正则表达式处理函数
# re.match() 方法
# re.match() ：尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回 none。
# 格式： re.match(pattern,string,flags =0)

# 函数参数说明
# 参数	    描述
# pattern	匹配的正则表达式
# string	要匹配的字符串
# flags	    标志位，用于控制正则表达式的匹配方式

# import re

# # 使用 re.match 进行匹配
# pattern = r"hello"  # r 表示 raw，原始的数据格式
# string = "hello world"
# match = re.match(pattern, string)
# if match:
#     print("匹配成功")
# else:
#     print("匹配失败")


# 结果查询方法
# group(): 获取匹配结果
# 使用 re.match 进行匹配
# pattern = r"\d+"
# string = "12345hello123 world"
# match = re.match(pattern, string)
# print(match)
# print(match.group())
# print(match.group(0))

# span(): 获取匹配结果在原字符串中的范围
# pattern = r"hello"
# string = "hello world"
# match = re.match(pattern, string)
# print(match.span())

# start(): 获取匹配结果在原字符串中起始下标位置
# end(): 获取匹配结果在原字符串中的结束下标位置
# pattern = r"hello"
# string = "hello world"
# match = re.match(pattern, string)
# print(match.start())
# print(match.end())


# re.search() 方法
# re.search：在字符串中搜索匹配指定的模式，如果找到则返回匹配对象，否则返回 None。
# 格式： re.search(pattern, string, flags=0)
#
# 函数参数说明
# 参数	    描述
# pattern	匹配的正则表达式
# string	要匹配的字符串
# flags	    标志位，用于控制正则表达式的匹配方式

# 使用 re.search 进行搜索
# pattern = r"wor"
# string = "hello world"
# search = re.search(pattern, string)
# print(search)
# if search:
#     print("找到匹配")
# else:
#     print("未找到匹配")

"""
re.match() 与 re.search() 的区别
re.match()只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None.
re.search()匹配整个字符串，直到找到一个匹配。
"""

# re.findall() 方法
# re.findall（）: 在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果有多个匹配模式，则返回元组列表，如果没有找到匹配的，则返回空列表。
# 格式： findall(string, pos, endpos)

# 函数参数说明
# 参数	    描述
# string	待匹配的字符串
# pos	    可选参数，指定字符串的起始位置，默认为 0
# endpos	可选参数，指定字符串的结束位置，默认为字符串的长度
# pattern = re.compile(r'\d+')   # 查找数字
# result = re.findall(r'\d+', 'hogwarts 123 python 456')
# print(result)
# result1 = pattern.findall('hogwarts 123 python 456')
# result2 = pattern.findall('hello123python563world', 0, 10)
#
# print(result)
# print(result1)
# print(result2)

# 多个匹配模式，返回元组列表
# result = re.findall(r'(\w+)=(\d+)', 'asd width=20 sdf height=10 python100')
# result1 = re.findall(r'(\w+)[= ](\d+)', 'asd width=20 sdf height=10 python 100')
# print(result)
# print(result1)

# re.sub() 方法
# re.sub() ：用于替换字符串中的匹配项。
# 格式：re.sub(pattern, repl, string, count=0, flags =0)

# 函数参数说明
# 参数	    描述
# pattern	匹配的正则表达式
# repl	    替换的字符串，也可为一个函数
# string	要被查找替换的原始字符串
# count	    模式匹配后替换的最大次数，默认 0 表示替换所有的匹配
# pattern = r"\d+"  # 匹配一个或多个数字
# string = "abc 123 def 456 ghi"
#
# # 将字符串中的数字替换为 "NUM"
# result = re.sub(pattern, "***", string)
# print("替换后的字符串:", result)


# re.split() 方法
# re.split:按照能够匹配的子串将字符串分割后返回列表。
# 格式： re.split(pattern, string[, maxsplit=0, flags=0])
#
# 函数参数说明
# 参数	    描述
# pattern	匹配的正则表达式
# string	要匹配的字符串
# maxsplit	分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数
# flags	    标志位，用于控制正则表达式的匹配方式
# pattern = r'\s+'  # 匹配一个或多个空白字符
# string = 'Hello   World  Python'
#
# # 使用正则表达式模式分割字符串
# result = re.split(pattern, string)
# print("分割后的子字符串:", result)

# 匹配模式
# 在大多数正则表达式的方法中，都会有一个 flags 的参数，该参数用于控制正则表达式的匹配方式。
# re.IGNORECASE
# re.IGNORECASE :用于在正则表达式中启用大小写不敏感的匹配，可简写为 re.I

# pattern = r'apple'
# string = 'Apple is a fruit. I like apple pie. aPPle'
#
# # 使用 re.IGNORECASE 标志进行匹配
# matches = re.findall(pattern, string, re.IGNORECASE)
# print("忽略大小写匹配的结果:", matches)


# re.MULTILINE
# re.MULTILINE: 用于启用多行模式，使用 ^ 和 $ 在每行的开头和结尾都能匹配, 可简写为 re.M
# pattern = r'^\d+'  # 匹配每行开头的数字
# string = '123 apple\n456 banana\n789 cherry'
#
# matches = re.findall(pattern, string)
# print("单行匹配的结果:", matches)
#
# # 使用 re.MULTILINE 标志进行匹配
# matches = re.findall(pattern, string, re.MULTILINE)
# print("多行匹配的结果:", matches)


# 匹配分组
# 模式	        功能
# |	            匹配左右任意一个表达式， \d+|\w+
# (xxx)	        将括号中字符作为一个分组
# \num	        引用分组 num 匹配到的字符串
# (?P<name>)	分组起别名
# (?P=name)	    引用别名为 name 分组匹配到的字符串


# | 匹配多个规则
# 使用 | 可以指定多个匹配表达式
# import re
#
# match_obj = re.match("[a-zA-Z0-9_]{4,20}@(163|126|qq|sina|yahoo)\.com", "hello@163.com")
# match_obj = re.match("[a-zA-Z0-9_]{4,20}@(163|126|qq|sina|yahoo)\.com", "son@163.com")
# match_obj = re.match("[a-zA-Z0-9_]{4,20}@(163|126|qq|sina|yahoo)\.com", "test@33.com")
# match_obj = re.match("[a-zA-Z0-9_]{4,20}@(163|126|qq|sina|yahoo)\.com", "hello@sina.com")
# match_obj = re.match("[a-zA-Z0-9_]{4,20}@(abc|123)\.com", "hello@abc.com")
# print(match_obj)
# if match_obj:
#     print(match_obj.group())
#     # 获取分组数据,一个元组算一个分组,即：(163|126|qq|sina|yahoo)中的匹配成功的数据
#     print(match_obj.group(1))
# else:
#     print("匹配失败")


# (xxx) 分组
# group() 方法可以获取完整的匹配结果，如果想获取匹配结果中某一个分组规则匹配到的结果，可以使用数字参数形式。
# import re
# match_obj = re.match("(\d{3,4})-(\d{4,10})", "010-888999")
#
# if match_obj:
#     print(match_obj.group())
#     print(match_obj.group(0))  # 和上面一样
#     # 分组:默认是1一个分组，多个分组从左到右依次加1
#     print(match_obj.group(1))
#     # 提取第二个分组数据
#     print(match_obj.group(2))
# else:
#     print("匹配失败")


# \xxx 引用规则
# 在一个匹配模式中，如果一个规则出现多次，可以将规则进行分组，然后在分组后引用该规则，避免重复书写。
# import re
#
# match_obj = re.match("<[a-zA-Z1-6]+>.*</[a-zA-Z1-6]+>", "<html>hh</div>")
#
# if match_obj:
#     print(match_obj.group())
# else:
#     print("匹配失败")
#
# match_obj = re.match("<([a-zA-Z1-6]+)>.*</\\1>", "<html>hh</html>")
# # 匹配失败，引用时前后都要一致
# # match_obj = re.match("<([a-zA-Z1-6]+)>.*</\\1>", "<html>hh</div>")
#
# if match_obj:
#     print(match_obj.group())
# else:
#     print("匹配失败")


# (?P<name>) (?P=name) 分组命名与引用
# 在使用分组时，可以给分组进行命名。在匹配规则中，可以通过分组命名引用某个分组中的规则。
import re
# 匹配多层嵌套
match_obj = re.match("<(?P<model1>[a-zA-Z1-6]+)><(?P<model2>[a-zA-Z1-6]+)>.*</(?P=model2)></(?P=model1)>",
                     "<html><h1>www.ceshiren.com</h1></html>")

if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")
