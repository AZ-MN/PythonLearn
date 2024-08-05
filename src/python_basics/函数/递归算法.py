"""
递归的基本原则
递归函数通常遵循以下原则：
 定义基本情况 确定一个或多个输入的特殊情况，当满足这些条件时，递归函数将直接返回结果而不再调用自身。
 减小问题规模 通过调用自身来解决一个规模更小的问题，这样每次递归调用都在问题规模上取得了进展。 也就是需要一个已定义好的规则来使其它非基本的情况转化为基本情况。
 终止条件 递归函数必须包含能够导致函数不再递归调用的条件，以避免无限递归。
"""


# 通过递归，实现5的阶乘
def factorial(n):
    #  设置终止条件
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# print(factorial(5))


# 通过递归，斐波那契数列
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# 计算斐波那契数列的第 10 项
n = 10
fib_result = fibonacci(n)
print(f"斐波那契数列的第 {n} 项为：{fib_result}")
