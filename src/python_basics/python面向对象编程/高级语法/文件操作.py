"""
简介
文件操作是每一门编程语言中都必不可少的一项语法，通过文件，可以实现数据持久化存储，测试数据驱动文件的处理，程序配置文件的处理等。
在程序中操作文件和使用图形界面操作文件的过程基本一致，都要进行找到文件位置，打开文件，读写文件，关闭文件等操作。
"""
# 打开文件
# Python 使用 open 方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。
# 完整格式：
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# 简化格式
# open(file, mode='r', encoding=None)
# file: 必选，指定打开文件的相对路径或者绝对路径。
# mode: 可选，文件打开模式，默认为 r 只读模式
# encoding: 一般使用 utf8

"""
mode参数常见下表：
字符	 含意
r	 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
w	 以只写方式打开文件。如果该文件已存在则覆盖文件。如果该文件不存在则创建新文件。
a	 以追加写入方式打开文件，如果文件存在则在末尾追加，文件不存在则创建新文件
b	 二进制模式
t	 文本模式（默认）
"""

# 示例：以写入文件打开 index.html 文件
# file = open("test.py", "w")
# length = file.write("print('Hellow World')")
# print(f"文件成功写入{length}个字节")


# 文件关闭
# 文件在操作完以后，需要将其关闭，close() 方法用于关闭一个已打开的文件。
# 关闭后的文件不能再进行读写操作， 否则会触发 ValueError 错误。
# close() 方法允许调用多次。
# 使用 close() 方法关闭文件是一个好的习惯。

# 关闭文件
# file.close()


# 文件写入
# write() 方法
# write() 方法用于向文件中写入指定字符串。如果文件打开模式为 b，则要将字符串转换成 bytes 类型的二进制字符串,函数返回成功写入数据的长度。
# 格式：fileObject.write( [ str ])
# 以写入文件打开 index.html 文件
# file = open("index.html", "w", encoding="utf-8")
# # 写入数据
# file.write("<h1>文件写入标题</h1>",)
# file.write("\n")
# file.write("<h1>Hellow World</h1>")
# file.write("\n")
# file.write("<p>文件写入内容。。。。。。</p>")
# # 关闭文件
# file.close()

# writelines() 方法
# writelines() 方法用于向文件中写入一序列的字符串。
# 这一序列字符串可以是由迭代对象产生的，如一个字符串列表。
# 注意：不要被方法名所迷惑，如果每个元素独占一行，需要在数据后指定换行符 \n。
# 格式：fileObject.writelines(seq)
# datas = ["AAAAAAAAAAAA\n", "BBBBBBBBBBBB\n", "CCCCCCCCCCCC\n", "DDDDDDDDDDDD\n"]
# file = open('data.txt', "w")
# file.writelines(datas)
# file.close()


# 读取文件
# read() 方法
# read() 方法用于从文件读取指定的字节数，如果未给定或为负则读取所有。
# 格式：fileObject.read([size=-1])
# file = open('data.txt', "r")
# # 读取10个字符
# content = file.read(1)
# print(content)
# # 读取所有内容
# content = file.read()
# print(content)
# file.close()

# readline() 方法
# readline() 方法用于从文件读取整行，包括 \n 字符。如果指定了一个非负数的参数，则返回指定大小的字节数，包括 \n 字符。
# 格式：fileObject.readline(size=-1)
# file = open('data.txt', "r")
# 读取10个字符
# content = file.readline(10)
# print(content)
# 读取文件指针所在行剩余所有内容
# content = file.readline()
# print(content)
# file.close()
#
# # readlines() 方法
# # readlines() 方法用于读取所有行(直到结束符 EOF)并返回列表。
# # 格式：fileObject.readlines()
# file = open('data.txt', "r")
# # 以行为单位读取文件所有的内容
# contents = file.readlines()
# print(contents)
# file.close()


# 上下文管理器
with open('data.txt', "r") as file:
    content = file.read(10)
    print(content, end="")
    content = file.read(10)
    print(content, end="")
