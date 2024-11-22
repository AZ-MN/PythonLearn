"""
模块
简介
Python 的模块是用于组织、封装和重用代码的文件，一个 Python 文件就是一个模块。
一个模块中可以包含变量、函数、类和其他 Python 语句，它允许将代码逻辑划分为独立的单元，并提供了一种组织代码的方式，使代码更加模块化和易于维护。
Python的模块可以分为三类，非别是 内建模块、第三方模块 和 自定义模块。
"""


# 模块的导入
# Python 可通过模块导入引用其它模块中的数据，提供了 import 和 from - import 两种导入方式。

# 导入模块
# Python中使用 import 关键字来导入模块，导入模块后，在当前文件中做为一个对象使用，可以通过 . 来引用模块中定义的函数、变量或类等。
# import custom_module
#
# custom_module.show()
#
# print(custom_module.num)
# print(custom_module.isApproved)


# 使用 as 别名的方法
# 如果被导入的模块名比较长，在使用时会不太方便，也可以使用 as 为模块指定一个别名，一旦指定了别名，原模块名就不能使用了。
# import custom_module as cm
#
# cm.show()
# print(cm.num)


# from-import 导入方法
# 导入 还可以使用 from module_name import object_name 语法，从模块中导入特定的对象，这样可以直接使用对象名，无需使用模块名前缀。
# from custom_module import show, isApproved
#
# show()
#
# print(num)  # 未导入不可用
#
# print(isApproved)


# 导入内置模块
# Python 标准库中包含了大量的内建模块，这些模块提供了各种功能，如数学计算、字符串处理、日期时间操作、文件操作等。通过导入相应的内建模块，可以使用这些功能，避免重复编写代码。
# import math
# import time
# print("*" * 20)
# print(time.localtime())
#
# time.sleep(2)
#
# print(math.pi)
# print(math.pow(5,2))


# dir() 函数是Python内置函数，用于获取指定对象的所有属性和方法的列表。
import math
import time
print(dir(math))
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2',
# 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs',
# 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf',
# 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm',
# 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']


print(dir(time))

# ['_STRUCT_TM_ITEMS', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'altzone', 'asctime', 'ctime',
# 'daylight', 'get_clock_info', 'gmtime', 'localtime', 'mktime', 'monotonic', 'monotonic_ns', 'perf_counter',
# 'perf_counter_ns', 'process_time', 'process_time_ns', 'sleep', 'strftime', 'strptime', 'struct_time',
# 'thread_time', 'thread_time_ns', 'time', 'time_ns', 'timezone', 'tzname']

# 由开发者编写，用于封装代码、组织功能，以便在其他 Python 程序中复用。自定义模块是一个 Python 文件，可以包含函数、类、变量等。
# import custom_module
#
# custom_module.show()
#
# print(custom_module.num)
# print(custom_module.isApproved)

