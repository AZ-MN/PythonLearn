"""
变量作用域
简介：作用域就是一个 Python 程序可以直接访问命名空间的正文区域。
变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python 的作用域一共有 4 种，分别是：
    L（Local）：最内层，包含局部变量，比如一个函数/方法内部。
    E（Enclosing）：包含了非局部（non-local）也非全局（non-global）的变量，一般在闭包中出现。
    G（Global）：当前脚本的最外层，比如当前模块的全局变量。
    B（Built-in）： 包含了内建的变量/关键字等，最后被搜索。
查找规则顺序： L –> E –> G –> B。
"""


# 局部变量


# 示例：
def show():
    # 局部变量
    a = 10
    print(a)


# 在函数外无法访问局部变量a
# print(a)
# 只能通过调用函数使用局部变量
# show()
# 函数外无法访问局部变量a
# print(a)


# 全局变量
# 全局变量定义
m = 20


def show1():
    # 使用全局变量
    print("show1:", m)


def show2():
    # 使用全局变量
    m = 40  # 只在函数内生效，无法影响到函数外
    print("show2:", m)


# # 使用全局变量
# print(m)
# show1()
# show2()
# # 使用全局变量
# print(m)


# 若想修改全局变量的值，需要使用 global 关键字
# 示例：
# 全局变量定义
m = 10


def show3():
    # 声明此变量是函数外定义的全局变量
    global m
    # 修改全局变量的值
    m = "ABC"
    # 使用全局变量
    print("show:", m)


# 使用全局变量
print(m)
show3()
# 使用全局变量
print(m)

num = input()
num = int(num)
print(round(num, 2))
