"""
类方法
简介
除了类属性，类还有类方法。
同样，类方法也可以通过类名直接进行使用，类方法在定义时，需要使用 @classmethod 装饰器进行修饰。
与实例方法不同的是，实例方法有一个默认参数 self，代表当前调用方法的实例对象，而类方法的默认参数为 cls， 该参数也是在使用时，由解释器自动传入的，但传入的对象不是实例对象，而是类对象。
在类方法中，可以通过参数 cls 使用使用类属性。
一般类方法用来封装工具类使用，将一些复杂的代码逻辑封装成类方法，由类名直接调用，不需要实例对象，比如时间处理，网络请求处理等。
需要注意的是，如果类中既定义了实例属性，又定义了类方法，那么在类方法中是不能使用实例属性的，因为在使用类方法的过程中，实例对象不存在，所以不能使用实例属性。
"""

# 示例：封装一个日期时间获取的工具类
import datetime


class Utils:
    now = datetime.datetime.now()

    @classmethod
    def current_date_time(cls):
        return cls.now

    @classmethod
    def current_date(cls):
        return cls.now.strftime("%Y-%m-%d")

    @classmethod
    def current_time(cls):
        return cls.now.strftime("%H-%M-%S")

    @classmethod
    def getYear(cls):
        return cls.now.year

    @classmethod
    def getMonth(cls):
        return cls.now.month

    @classmethod
    def getDay(cls):
        return cls.now.day

    @classmethod
    def getHour(cls):
        # 下面两种调用类方法的方式是错误的，这种调用少传了 self 参数
        # cls.show()
        # Utils.show()
        return cls.now.hour

    def show(self):
        print("show")


print(Utils.current_date_time())
print(Utils.current_date())
print(Utils.current_time())
print(Utils.getYear())
print(Utils.getMonth())
print(Utils.getDay())
print(Utils.getHour())

u = Utils()
u.show()

