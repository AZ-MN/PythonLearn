# 导入模块
# import custom_module
#
# custom_module.show()
#
# print(custom_module.num)
# print(custom_module.isApproved)


# 使用 as 别名的方法
# import custom_module as cm
#
# cm.show()
# print(cm.num)


# from-import 导入方法
# from custom_module import show, isApproved
#
# show()
#
# print(num)  # 未导入不可用
#
# print(isApproved)


# 导入内置函数
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

