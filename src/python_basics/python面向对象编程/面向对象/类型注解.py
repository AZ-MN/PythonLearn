"""
类型注解
简介
Python 是一种动态类型语言，变量的类型是程序在运行时通过保存的数据动态推导得到，该特性使得在开发过程中不必过度关注变量的类型。
但随着项目越来越大，代码也就会越来越多，在这种情况下，很容易不记得某一个方法的入参类型是什么，一旦传入了错误类型的参数，再加上 Python 是解释性语言，只有运行时候才能发现问题， 这对大型项目来说是一个巨大的灾难。
在 Python3.5 版本中，引进了一种新的语法来给函数或变量增加注释，即类型注解。
Python 类型注解是一种可选的静态类型检查机制，它在注释中标注变量的类型，以提高程序的可读性和可维护性。

类型注解的特征如下：
类型检查，防止运行时出现参数和返回值类型、变量类型不符合。
作为开发文档附加说明，方便使用者调用时传入和返回参数类型。
在函数参数中使用时，形参变量会根据类型进行相应的代码提示。
PyCharm 目前支持 typing 检查，参数类型错误会黄色提示。
加入类型注解后并不会影响程序的运行，不会报正式的错误，只有提醒。
"""

# 类型注解基本使用
# Python 类型注解采用冒号 : 后跟预期类型的方式进行标注。
# num = 10
# print(num)
#
# num: int = 20
# print(num)
#
# num = "30"  # 类型不符，IDE会给出提示，但程序可以正常运行
# print(num)


# n: int : 指定了输入参数 n 为 int 类型，
# msg: str : 指定了输入参数 msg 为 str 类型，
# -> None : 指定了 show 函数的返回值为 None 类型，即无返回值。
# def show(n: int, msg: str) -> None:
#     for i in range(n):
#         print(msg)
#
#
# def display(msg):
#     print(msg.upper())  # 不会主动提示 upper() 等字符串函数
#
#
# def info(msg: str) -> None:
#     print(msg.upper())  # 添加了类型注解后，主动提示 upper() 函数
#
#
# if __name__ == '__main__':
#     show(5, "hello")
#     # show("10", "world")
#     display("Test")
#     info("World")


# 容器类型注解
# tuple 类型注解
# 元组基本使用
# def show(data: tuple) -> None:
#     for d in data:
#         print(d, end="")
#     print("")
#
#
# show((1, 2, 3))
# show(('a', 'b', 'c'))
# show((1, 2, 3, 'a', 'b', 'c'))


# 由于元组的不可变特殊性，当指定了元素类型，随之也指定了元组的元素个数，代码中约定传入具有一个整型数据元素的元组。
# 指定元组中多个不同类型的元素
# def show(data: tuple[int, str, bool]) -> None:
#     for d in data:
#         print(d)
#
#
# show((1, "hello", True))  # 多个类型数据要一一对应
# show((1, 2, 3))  # 不符合注解类型
# show(('a', 'b', 'c'))  # 不符合注解类型


# 指定元组中任意个不同类型的元素
# 使用任意类型时，需要使用 typing 模块中的 Any 类型，可变数量使用 ... 表示。
# from typing import Any
#
#
# def show(data: tuple[Any, ...]) -> None:
#     for d in data:
#         print(d, end="-")
#     print("")
#
#
# show((1, "hello", True, 123))
# show((1, 2, 3))
# show(('a', 'b', 'c'))


# list 类型注解
# 由于列表的可变特性，使用相对简单。
# 列表基本使用
# def show(data: list) -> None:
#     for d in data:
#         print(d, end="")
#     print("")
#
#
# show([1, 2, 3])
# show(["a", 'b', 'c'])
# show([1, 2, 3, "a", 'b', 'c'])


# 列表中指定元素类型
# def show(data: list[int]) -> None:
#     for d in data:
#         print(d, end="")
#     print("")
#
#
# show([1, 2, 3])
# show(["a", 'b', 'c'])  # 不符合注解类型
# show([1, 2, 3, "a", 'b', 'c'])
# 在指定元素中元素类型时，实参列表中只要存在注解类型数据，即使包含了其它类型也认为符合类型要求。


# dict 类型注解
# 字典与列表类似，具有元素个数可变性，所以只需指定 key 与 value 的类型即可。
# def show(data: dict[str, int]) -> None:
#     for d in data:
#         print(d)
#
#
# show({"a": 97})
# show({"a": 97, "b": 98})
# show({"c": "CC"})  # 不符合注解类型


# Union 类型注解
# 可以使用 typing 模块中的 Union 指定多个类型
# from typing import Union
#
#
# def show(data: Union[str, int, float, bool]) -> None:
#     print(data)
#
#
# show(4)
# show("hello")
# show(3.1415926)
# show(True)


# Sequence 类型注解
# 可以使用 typing 模块中的 Sequence 指定任意可迭代类型。
# Sequence 所提示的是任何可以被索引的数据: 列表,元祖,字符串等。
# 注意：在定义函数时 [] 中只可以指定一个数据类型，意味着在传入的列表或者元组等可索引数据时，内部元素的数据类型需要是统一的。
# from typing import Sequence
#
#
# def show(data: Sequence[int]) -> None:
#     print(data)
#
#
# show((1, 2, 3))
# show([1, 2, 3])
# show([1, 2, 3, "a", "b", "c"])
# show("123")  # 不符合注解类型


# Optional 类型注解
# 当函数的参数有默认值，导致参数不是必须要传入的，那么你可以尝试使用 typing 模块中的Optional 来做到类型提示。
# from typing import Optional
#
#
# def show(data: Optional[int] = 0) -> None:
#     print(data)
#
#
# show()  # 可以不用传入参数
# show(1)


# Callable 类型注解
# 当需要表明某个函数的参数是函数时可以使用 typing 模块中的 Callable 作为类型提示。
# from typing import Callable
#
#
# def show(data: int) -> None:
#     print(data)
#
#
# def callback(func: Callable, data: int) -> None:
#     func(data)
#
#
# callback(show, 1)


# 自定义类作为类型注解
# 自定义类可以直接做为类型进行注解使用。
class Person:
    pass


def show(obj: Person) -> None:
    print(obj)


show(Person())
p = Person()
show(p)

