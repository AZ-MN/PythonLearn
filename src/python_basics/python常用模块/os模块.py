"""
os模块
简介
Python 的内置库 os（Operating System Interface 提供了与操作系统交互的函数，允许用户与操作系统进行各种操作，如文件和目录操作、环境变量访问、进程管理等。

使用 os 库，您可以编写跨平台的代码，因为它提供了对操作系统底层功能的抽象，而不用担心特定操作系统的细节。
"""
import os

# 路径操作
# os.getcwd(): 获取当前工作目录
# print(os.getcwd())  # 和控制台命令pwd（print work directory）一样


# os.chdir()：用于改变当前的工作目录。
# 工作目录是指当前正在执行的脚本所在的目录，通过使用 os.chdir()方法，可以在脚本执行过程中切换到不同的目录。
# 切换到指定目录
# os.chdir('../python语法与数据结构')
# 切换后的工作目录
# print(os.getcwd())

"""
path方法	                说明
os.path.abspath(path)	返回绝对路径
os.path.basename(path)	返回文件名
os.path.dirname(path)	返回文件路径
os.path.split(path)	    分割路径
os.path.join(path)	    拼接路径
os.path.exists(path)	判断路径是否存在
os.path.isdir(path)	    判断是否是目录
os.path.isfile(path)	判断是否是文件
os.path.getsize(path)	获取文件大小
"""
# os.path.abspath(path)：获取绝对路径。path 是要获取绝对路径的路径
# print(os.path.abspath("python常用模块"))
path = 'E:\PythonCode\PythonLearn\src\python_basics\python常用模块'
# print(os.path.basename(path))  # python常用模块(只取文件名)
# print(os.path.dirname(path))  # E:\PythonCode\PythonLearn\src\python_basics\python常用模块(取路径名)
# print(os.path.split(path))  # os.path.split(path)：用于将一个路径拆分为目录部分和文件名部分
# filename = os.path.join(path, 'test.txt')  # os.path.join(path)：用于连接多个路径部分。它将多个路径片段组合在一起，形成一个新的路径字符串。
# print(filename)
# print(os.path.exists(path))  # os.path.exists(path) 判断路径是否存在（可以是文件或目录）
# print(os.path.isdir(path))  # os.path.isdir(path) 判断是否是目录

# file_path = 'E:\PythonCode\PythonLearn\src\python_basics\python常用模块\os模块.py'
# print(os.path.isfile(file_path))  # os.path.isfile(path) 判断是否是文件

# print(os.path.getsize(file_path))  # os.path.getsize(path) 获取文件大小

# 目录和文件操作
# os.listdir()：列出当前目录内容
# 获取目录内容
# directory_path = 'E:\PythonCode\PythonLearn\src\python_basics\python常用模块'
# content = os.listdir(directory_path)
# print("Directory Content:", content)

# 创建新目录
# new_directory = 'E:\PythonCode\PythonLearn\src\python_basics\python常用模块/new_directory'
# os.mkdir(new_directory)

# os.makedirs()：递归创建多级目录
# 创建多级目录
# nested_directory = 'E:\PythonCode\PythonLearn\src\python_basics\python常用模块/new_directory/L1/test'
# os.makedirs(nested_directory)

# os.rmdir()：删除空目录
# 删除目录
# directory_to_delete = 'E:\PythonCode\PythonLearn\src\python_basics\python常用模块/new_directory/L1/test'
# os.rmdir(directory_to_delete)

# os.rename()：重命名目录
# 重命名目录
# old_directory_name = 'E:\PythonCode\PythonLearn\src\python_basics\python常用模块/new_directory'
# new_directory_name = 'E:\PythonCode\PythonLearn\src\python_basics\python常用模块/old_directory'
# os.rename(old_directory_name, new_directory_name)


# os.remove()：删除文件(只能删除文件，不能删除目录)
# 删除指定的文件
# file_to_delete = 'E:\PythonCode\PythonLearn\src\python_basics\python常用模块/old_directory/L1/test'
# file_to_delete = 'E:\PythonCode\PythonLearn\src\python_basics\python常用模块/old_directory/L1/aa.txt'
# os.remove(file_to_delete)

# 其它操作
# os.name：获取系统名称，在Windows上，os.name 值为 nt。在Linux、macOS，os.name 为 posix。
# 获取当前平台名称
# platform_name = os.name
# print("Platform Name:", platform_name)

# os.chmod(path, mode)：更改文件权限模式。 path 是要更改权限的文件路径，mode 是权限模式，通常用八进制表示，如 0o755
# 更改文件权限模式为-rwxr-xr-x
# read  write  execute
# r     w      x
# 2^2   2^1    2^0
# 4     2      1


file_path = 'E:\PythonCode\PythonLearn\src\python_basics\python常用模块/old_directory/L1/bb.txt'
os.open(file_path, os.O_CREAT)
# os.chmod(file_path, 0o755)

# 更改文件权限模式为-rwx-r--,计算后为0o740(八进制用 0o 表示, 12进制用 0x 表示)
os.chmod("E:\PythonCode\PythonLearn\src\python_basics\python常用模块/old_directory/L1/bb.txt", 0o761)

# os.sep：用于表示操作系统特定的路径分隔符。在Windows操作系统上，路径分隔符是反斜杠 \ ；而在POSIX系统（如Linux、macOS等）上，路径分隔符是正斜杠 /。
# 获取路径分隔符
# path_separator = os.sep
# print("Path Separator:", path_separator)
