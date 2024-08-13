# 函数引用
# 在学习闭包之前，需要理解一个概念，Python 中定义的函数，也可以像变量一样，将一个函数名，赋值给另一个变量名，赋值后，此变量名就可以做为该函数的一个别名使用，进行调用函数。
# 示例：
# def show():
#     print("Show Run ...")


# show()
# a = show  # 将一个函数名赋值给另一个变量名
# a()  # 调用赋值后的变量，此变量可以作为原函数的一个别名使用

"""
闭包
 闭包 Closure 是指在一个嵌套的函数内部访问其外部函数中定义的变量或函数的能力。换句话说，闭包是一个函数对象，它可以记住并访问它创建时的上下文环境中的变量。
 
闭包通常由两个部分组成：内部函数和与其相关的环境变量。
 内部函数是在外部函数中定义的函数，它可以访问外部函数中的局部变量和参数，以及外部函数所在的作用域中的变量。
 环境变量是在外部函数中定义的变量或其他函数对象，它被内部函数引用并记住，即使外部函数执行完成后仍然存在。

闭包的特点包括：
 内部函数可以访问外部函数中定义的变量和参数，即使外部函数已经执行完毕。
 闭包可以在外部函数的作用域之外被调用和执行。
 闭包可以访问并修改外部函数中的局部变量，使其具有持久性。

闭包的应用场景包括：
 保护私有变量：可以使用闭包来创建私有变量和方法，通过内部函数的作用域和环境变量，可以实现对外部访问的限制。
 延迟执行：可以使用闭包来延迟某个函数的执行，即在函数外部创建一个闭包，将需要执行的函数作为内部函数，通过调用闭包来触发函数的执行。
 缓存数据：可以使用闭包来缓存一些昂贵的计算结果，以避免重复计算，提高程序的性能。
"""

# 闭包的定义
# 外函数
# def out_func():
#     out_n = 100
#
#     # 内函数
#     def inner_func():
#         print(out_n)
#     # 外函数一定要返回内函数的引用
#     return inner_func
#
#
# if __name__ == '__main__':
#     of1 = out_func()
#     of2 = out_func()
#
#     of1()
#     of2()
#     print(of1)
#     print(of2)


"""
nonlocal
与全局变量一样，在函数内是不能直接修改函数外的变量的，如果修改全局变量需要使用 global 在函数内部声明变量为全局变量。

闭包中要修改变量也是一样，内函数是不能直接修改外函数中定义的变量的，如果需要修改，要在内函数中使用 nonlocal 关键字声明该变量为外函数的变量。
"""

# 不使用nonlocal装饰
# def out_func():
#     out_n = 100
#
#     def inner_func():
#         out_n = 200
#         print("inner:", out_n)
#
#     print("outer1:", out_n)
#     inner_func()
#     print("outer2:", out_n)
#     return inner_func
#
#
# if __name__ == '__main__':
#     of1 = out_func()
#     of1()

# 结果：
# outer1: 100
# inner: 200
# outer2: 100
# inner: 200


# 使用nonlocal装饰
# def out_func():
#     out_n = 100
#
#     def inner_func():
#         nonlocal out_n  # 使用nonlocal修饰，改变了外函数中变量的值
#         out_n = 200
#         print("inner:", out_n)
#
#     print("outer1:", out_n)
#     inner_func()
#     print("outer2:", out_n)
#     return inner_func
#
#
# if __name__ == '__main__':
#     of1 = out_func()
#     of1()

# 结果：
# outer1: 100
# inner: 200
# outer2: 100
# inner: 200


"""
装饰器
 装饰器是 Python 提供的一种语法糖，装饰器使用 @ 符号加上装饰器名称，用于修改其他函数的行为，并且在不修改原始函数定义和调用的情况下添加额外的功能。
 装饰器提供了一种简洁而优雅的方式来扩展和修改函数或类的功能。它本质上就是一个闭包函数。

装饰器的功能特点:
 不修改已有函数的源代码
 不修改已有函数的调用方式
 给已有函数增加额外的功能
"""
# 装饰器的使用
# 由于装饰器本质上就是一个闭包函数，所以在使用自定义装饰器之前，需要先定义一个用来做为装饰器的闭包。
# 而闭包的外部函数名，就作为装饰器名使用。


import time

# 定义一个闭包，用来统计一个函数执行时间
# def count_time(func):
#     def inner(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         stop = time.time()
#         print(f"程序运行的时长为 {stop - start} 秒")
#         return result
#
#     return inner


# 装饰器使用方法，@ + 装饰器名称
# @count_time
# def show():
#     s = 0
#     for i in range(1000001):
#         s += i
#     print(s)
#
#
# @count_time
# def display(n, msg):
#     for i in range(n):
#         print(msg)
#
#
# if __name__ == '__main__':
#     # show()  # 不改变函数，正常调用就可以
#
#     # Python 解释器解释过程：
#     show = count_time(show)  # 和装饰器一个作用
#     # show()
#     display(5, "hello")

"""
上面代码中，使用闭包实现了一个函数执行时间统计的功能。

在 show 函数上，使用闭包函数做为装饰器为 show 统计运行时间。

通过代码可以看出，在使用 count_time 函数做为装饰器时，即没有改变show函数的内部定义，也没有改变 show 函数的调用方式，但却为 show 函数额外扩展了运行时间统计的功能，这就是装饰器的作用。
"""

"""
装饰器的本质
装饰器提供了一种简洁而优雅的方式 -- 语法糖 来扩展和修改函数或类的功能。其本质就是函数的使用。

语法糖： 在计算机科学中，语法糖（Syntactic sugar）是指一种语法上的扩展，它并不改变编程语言的功能，只是提供了更便捷、更易读的写法，使得代码更加简洁和可理解。
常见的语法糖:
 推导式
 装饰器
 切片
 上下文管理器
 
Python 解释器在遇到装饰器时，会将被装饰函数引用做为参数传递给闭包的外函数，外函数执行后，返回内函数的引用，此时，再将内函数引用赋值给被装饰器函数。

当 Python 解释器执行完装饰过程后，被装饰函数的函数名就不在保存原函数的引用，而是保存的闭包函数 inner 的引用。

而当执行被装饰函数时，实际执行的是闭包函数 inner ，由 inner 间接调用被装饰函数，完成整个调用过程。
"""

"""
通用装饰器
理论上，一个装饰器可以装饰任何函数，但实际前面定义的做为装饰器的 count_time 函数却只能装饰特定的无参无返回值的函数。

如果需要装饰器可以装饰任何函数，那么就需要解决被装饰函数的参数及返回值的问题。

可以通过可变参数和在内函数中返回被装饰函数执行结果的形式解决此问题。
"""

# 做为装饰器名的外函数，使用参数接收被装饰函数的引用
# def decorator(func):
#     # 内函数的可变参数用来接收被装饰函数使用的参数
#     def inner(*args, **kwargs):
#         # 装饰器功能代码
#         # 调用被装饰函数，并将接收的参数传递给被装饰函数，保存被装饰函数执行结果
#         result = func(*args, **kwargs)
#         # 返回被装饰函数执行结果
#         return result
#
#     # 返回内函数引用
#     return inner


"""
带参数装饰器
除了普通的装饰器使用方式外，在使用装饰器时，还需要向装饰器传递一些参数，比如测试框架 pytest 实现数据驱动时，可以将测试数据以装饰器参数形式传入，此时，前面定义的做为装饰器的闭包形式就不能满足需求了。

可以在通用装饰器外，再定义一层函数，用来接收装饰器的参数。
"""

# 实现代码
# def decorator_args(vars, datas):
#     def decorator(func):
#         def inner(*args, **kwargs):
#             return func(*args, **kwargs)
#
#         return inner
#
#     return decorator
#
#
# data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]


# 装饰器传参
# @decorator_args("a,b,c", data)
# def show(a, b, c):
#     print(a, b, c)


"""
装饰器传参原理
装饰器传参的本质就是链式语法的多次函数调用
@decorator_args("a,b,c", data) 解析:
 1.先执行 decorator_args("a,b,c", data) 部分
 2.得到结果 decorator 与 @ 结合变成装饰器形式 @decorator
 3.通过结果 @decorator 装饰器正常装饰被装饰函数
"""


# 使用装饰器传参，实现数据驱动过程(了解)
# 此过程只用来讲解装饰器形式如何实现数据驱动过程，并没有完整实现。

# 接收装饰器参数的函数
# 参数一：以字符串形式接收被装饰函数的参数列表，需要与被装饰函数参数名保持一致，例："a,b,c"
# 参数二：以[(),(),()] 形式传入驱动数据。
def decorator_args(vars, datas):
    def decorator(func):
        # 将字符串参数分割备用
        v_keys = vars.split(",")
        # 定义保存 [{},{},{}] 形式的数据
        new_datas = []
        # 遍历数据，取出一组元素数据
        for item in datas:
            # 定义一个新字典，用来保存 变量名与传入数据组成的字典
            d_item = {}  # {"a": 1, "b": 2, "c": 3}
            # 使用 zip 函数，同时遍历两个元组，变量名做为key, 元素数据做为value
            # v_keys = [a, b, c]
            # item = (1, 2, 3)
            for k, v in zip(v_keys, item):
                # 将 变量名和值对应保存到字典中
                d_item[k] = v
            # 将组合好的字典追加到新数据中备用
            new_datas.append(d_item)  # new_datas = [{'a': 1, 'b': 2, 'c': 3}, {'a': 4, 'b': 5, 'c': 6}, {'a': 7,
            # 'b': 8, 'c': 9}]

        def inner(*args, **kwargs):
            return func(*args, **kwargs)

        # 遍历新数据，取出元素字典
        for item in new_datas:
            # 将字典中的数据解包传给内函数
            inner(**item)
        return inner

    return decorator


# 数据驱动数据
data = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]


# 装饰器传参
@decorator_args("a,b,c", data)
def show(a, b, c):
    print(a, b, c)
