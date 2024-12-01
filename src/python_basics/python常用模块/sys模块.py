"""
sys模块
简介
sys 是 Python 的内置标准库模块。
提供了访问与 Python 解释器相关的变量和函数的功能。
它的主要用途是与系统交互、解释器配置、命令行参数处理、标准输入输出、异常处理等。
"""
import sys

# 常用属性
# sys.argv 获取命令行参数列表，包括脚本名称和传递给脚本的其他参数
# print(sys.argv)
# print(f"WebServer is running on {sys.argv[1]}:{sys.argv[2]}")

# sys.version 获取当前 Python 解释器的版本信息
# print(sys.version)

# sys.version_info 获取当前 Python 解释器的版本信息，以元组形式表示详细的版本号信息
# print(sys.version_info)
# print(sys.version_info[0])
# print(sys.version_info[1])
# print(sys.version_info[2])
#
# result = sys.version_info[1]
# print(type(result))
#
# if result < 10:
#     print("Use low python version")
# else:
#     print("Use high python version")

# sys.path 获取模块搜索路径列表，用于指定 Python 解释器搜索模块的路径
# for path in sys.path:
#     print(path)
#
# print(type(sys.path))
# sys.path.append('/mySite')  # 可追加路径，但不建议使用

# sys.platform 获取当前运行的操作系统平台名称。
# print(sys.platform)

# sys.modules 返回已导入的模块信息，返回一个字典
import custom_module
from mp.mm import *

# for module_name, module in sys.modules.items():
#     print(f'模块名: {module_name}, 模块对象: {module}')

# sys 常用方法
# sys.getdefaultencoding()：获取编码方式
# 获取系统当前编码
print(sys.getdefaultencoding())

# sys.exit()：运行时退出
import time

i = 0
while True:
    time.sleep(1)
    i += 1
    print(i)
    if i > 10:
        sys.exit()
# 运行之后退出，不会运行后面的代码
