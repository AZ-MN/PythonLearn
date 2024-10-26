"""
静态方法
简介
除了类方法，Python 的类中还有一种静态方法。
静态方法在定义时，需要使用 @staticmethod 装饰器进行装饰，与类方法不同的是，静态方法没有默认参数。
静态方法和普通的函数本质上是一样的，只是定义在了类中。
一般情况下，静态方法同类方法一样，也是在封装工具类时使用，区别在于，静态方法中不需要使用类属性（不是不能使用，只是不建议）。
"""

# 示例：封装两个数字操作的简单计算器


class Calc:
    @staticmethod
    def add(n1, n2):
        return n1 + n2

    @staticmethod
    def sub(n1, n2):
        return n1 - n2

    @staticmethod
    def mul(n1, n2):
        return n1 * n2

    @staticmethod
    def div(n1, n2):
        return n1 / n2


print(Calc.add(10, 20))
print(Calc.sub(10, 20))
print(Calc.mul(10, 20))
print(Calc.div(10, 20))