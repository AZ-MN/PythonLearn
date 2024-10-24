"""
类属性
简介
在 Python 中，一切皆为对象，类也不例外，在程序运行过程中，类也会做为一个对象使用。
类对象与实例对象不同，可以理解为实例对象是由类对象复制而来，每个实例对象之间具有数据独立性。而类对象在程序运行过程中，只有一个。
既然是对象，那么就可以拥有自己的属性，在类中定属性时，属性名有 self 前缀的是实例属性，而在类中直接定义的属性即为类属性。
"""


# 定义一个饮水机类
class WaterDispenser:
    # 剩余水量
    surplus_water = 1500

    # 出水口
    def water_outlet(self, n):
        WaterDispenser.surplus_water -= n
        print("剩余水量：", WaterDispenser.surplus_water)


# 定义一个人的类，持有一个饮水机的对象
class Person:
    def __init__(self, wd):
        self.wd = wd

    # 人有一个接水的行为（方法）
    def get_water(self, n):
        self.wd.water_outlet(n)


if __name__ == '__main__':
    wd = WaterDispenser()

    # 每个有都有饮水机的使用权
    Tom = Person(wd)
    Jake = Person(wd)

    # 杯子大小导致每人接水量的不同
    Tom.get_water(100)
    Jake.get_water(200)


# wd1 = WaterDispenser()
# wd2 = WaterDispenser()
#
# wd1.water_outlet(100)
# print(wd1.surplus_water)
# wd2.water_outlet(200)
# print(wd2.surplus_water)
# print(WaterDispenser.surplus_water)


# 类属性特征：
# 在类中直接定义的变量为类属性
# 在方法中使用类属性时，需要使用类名做为前缀 类名.类属性名
# 在类的外部可以通过类名或实例对象名访问类属性
# 所有的实例对象名共享一个类属性
# 实例对象只能获取类属性的值，不能直接进行修改，只能通过方法进行修改
