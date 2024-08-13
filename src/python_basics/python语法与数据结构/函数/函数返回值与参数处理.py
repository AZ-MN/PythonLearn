"""
函数简介:
函数通过接收一定的数据，根据业务逻辑进行相应的处理，然后将处理结果返回给调用者。
函数思想:
实现函数要基于高内聚，低耦合的思想。
"""


# 函数返回值与参数处理
# 函数返回值
# Python 中使用 return 返回函数的结果，同时，return 也具有结束函数的作用。
def show():
    print("循环前输出内容")
    for i in range(10):
        print(i)
        if i == 2:
            return
    print("循环后输出内容")


# print("函数调用前输出内容")
# show()
# print("函数调用后输出内容")

# 函数只能返回一个值
def getString():
    s = input("请输入一个字符串:")
    return s  # 返回函数值


# result = getString()  # 获得函数返回值
# print(result.upper())  # 对函数返回值做处理


# 如果想返回多个值
def getTwoNum():
    a = int(input("请输入第一个数字："))
    b = int(input("请输入第二个数字："))
    return a, b


# m, n = getTwoNum()
# print(m, n)
# result = getTwoNum()
# print(result)
# print(type(result))


# 组包与解包
nums = 1, 2, 3, 4, 5  # Python会进行自动组包操作，将所有的数字组合成一个元组，再将元组赋值给变量
# 组包
# print(nums)
# print(type(nums))  # 组包类型是元组

# 解包
a, b, c, d, e = nums  # 当使用一个元组为多个变量进行赋值时，Python 会将元组中的元素值，依次赋值给变量，这称为解包操作
# print(a, b, c, d, e)


# 多个return语句
n = 1


def multiReturn():
    if n == 1:
        return 1  # 从第一个return就结束了函数，如果想要return多个，需要使用判断条件
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    elif n == 4:
        return 4
    else:
        return 5


# print(multiReturn())
# print(multiReturn())
# n = 3
# print(multiReturn())
# print(multiReturn())
# n = 10
# print(multiReturn())


"""
在程序中，函数调用时指定数据的过程，称为参数传递，这时有四个概念，如下：
 主调函数：主动调用其它函数执行的称为主调函数。
 被调函数：被动调用执行的函数称为被调函数。
 实际参数：在调用函数的时候，函数名称后面括号中的数据即为实际参数，简称实参，通俗讲就是实际值。
 形式参数：在定义函数的时候，函数名称后面括号中的变量即为形式参数，称称形参，通俗讲就是一个记号。
"""


# 参数传递
# 示例：
# name, age, gender 为形参


def info(name, age, gender):
    print(f"我叫{name}, 年龄{age}岁，性别{gender}")


# 调用时的数据为实参
# info("Tom", 22, "男")
# info("Rose", 23, "女")


# 位置参数
# 示例：


def printMsg(n, msg):
    for i in range(n):
        print(f'第{i + 1}次输出{msg}')


# 正确使用位置参数
# printMsg(5, "Hogworts")
# 错误使用位置参数
# printMsg("Hogworts", 5)


# 关键字参数
# printMsg(n=5, msg="Hogworts")
# print("- " * 10)
# printMsg(msg="Hogworts", n=5)


# 默认值参数
# 实现一个乘方函数
def my_power(m, n=2):
    return m ** n


# 使用指定的参数
# print(my_power(2, 3))  # 虽然有参数有默认值，但调用函数的时候可以将默认值覆盖掉
# # 使用默认值参数
# print(my_power(2))  # 没有传参数的时候，函数会自动拿默认值使用

# def show(a, b=2, c):
#     print(a, b, c)
# show(2, 3, 4) # 需要注意的是：指定默认值的形式参数必须放在所有未指定默认值参数的后面，否则会产生语法错误


# 可变参数
"""
可变位置参数:
 Python使用 *args 参数做为形参，接收不确定个数的位置参数。
 *args 将接收到的任意多个实际参数放到一个元组中。
"""


# 不确定个数数字求和
def my_sum(*args):
    print(args)
    print(*args)
    print(type(args))
    s = 0
    for i in args:
        s += i

    print(s)
    print("*" * 10)


# my_sum(1, 2, 3)
# my_sum(1, 2, 3, 4)
# my_sum(1, 2, 3, 4, 5)
# my_sum(1, 2, 3, 4, 5, 6)

"""
可变关键字参数
 Python使用 **kwargs 参数做为形参，接收不确定个数的关键字参数。
 **kwargs 将接收到的任意多个实际参数放到一个字典中。
"""


# 定义可变关键字参数
def print_info(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for k, v in kwargs.items():
        print(k, v)
    print("*" * 10)


# print_info(Tom=18, Jim=20, Lily=12)
# print_info(name="tom", age=22, gender="male", address="BeiJing")

# 混合参数
"""
当定义函数时，参数列表中出现了多种类型的参数，定义时需要注意参数的定义顺序，如果顺序使用不正确，在调用函数时，可能会报错。
正确顺序的定义格式为：
def funcname(位置参数，可变位置参数，默认值参数，可变关键字参数):
    pass
"""


def info(name1, name2, *args, age1=18, age2=21, **kwargs):
    print("Positional Arguments:")
    print("name1:", name1)
    print("name2:", name2)
    print("args:", args)
    print("Keyword Arguments:")
    print("age1:", age1)
    print("age2:", age2)
    print("kwargs:", kwargs)


info("Alice", "Bob", "Charlie", "Dave", age2=30, occupation="Engineer", city="New York")
info("Alice", "Bob", "Charlie", "Dave", age1=25, age2=30, occupation="Engineer", city="New York")


# 一般函数在不确定参数的情况下，会将上面的形式简化定义，用来接收任意数量的参数。
def funcname(*args, **kwargs):  # 在此定义形式中，使用 *args 接收所有的位置参数，使用 **kwargs 接收所有的关键字参数。
    pass
