def outer(num1):
    def inner(num2):
        result = num1 + num2
        print(f"外部函数的参数num1: {num1}, 内部函数的参数num2: {num2}, 计算结果result: {result}")

    return inner  # 外函数一定要返回内函数的引用


# 内函数只有被外部函数调用后才会执行，所以外函数的参数num1在函数内部被使用，所以外函数的参数num1是必须的。
func = outer(10)  # func = inner
func(20)  # func(20) = inner(20)

outer(3)(4)  # outer(3) = inner -> inner(4)
