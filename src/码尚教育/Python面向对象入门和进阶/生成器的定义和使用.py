# 自定义函数和生成器唯一的区别就是函数中有yield关键字


def func():
    print(1)
    print(2)
    print(3)
    print(4)
    return 5
    print(6)
    print(7)


# 函数一旦调用, 会从头开始执行, 遇到return就返回, 不会执行return后面的代码
# func()

# 当函数中有yield关键字时, 函数就变成生成器, 生成器会记住上一次执行的位置, 下次再执行时从上一次执行的位置继续执行
def generator():
    print(1)
    print(2)
    print(3)
    print(4)
    yield 5
    # 会结束本次生成器的执行，并且携带返回值
    # 当使用生成器对象通过next内建函数调用时，下次调用会从yield下面开始
    print(6)
    print(7)
    yield 8
    print(9)
    yield 10
    print(11)
    print(12)


# 生成器的调用方式和普通函数调用不一样，调用生成器时，会返回一个生成器对象
# print(generator())  # <generator object generator at 0x0000015467200C10>

# 生成器对象通过next内建函数调用, 但是直接使用next内建函数不会记录上一次执行的位置, 会从头开始执行
# print(next(generator()))
# print(next(generator()))

# 一般会将生成器对象赋值给一个变量, 然后通过变量调用生成器对象
gen = generator()
print("第一次调用生成器")
print(next(gen))
print("第二次调用生成器")
print(next(gen))
print("第三次调用生成器")
print(next(gen))
print("第四次调用生成器")
print(next(gen))
# print("第五次调用生成器")
# print(next(gen))  # 报错 StopIteration
