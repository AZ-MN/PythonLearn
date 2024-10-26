"""
构造方法
简介
在上一节中，通过动态绑定的方式为实例对象添加了属性。
但是这种操作显然是不符合逻辑的。每个实例对象一旦被实例，就应该含有类中定义的属性。
此时就需要使用构造方法来实现。
"""


# 构造方法
# 构造方法 __init__(self) 在实例对象时自动调用, self 参数不需要手动传参，该参数在实例对象时，由解释器自动传入被实例的对象。
# self 是一个特殊的关键字，用来表示当前被实例的对象，可以理解为人称代词我。
# 通过 self 可以定义或访问实例对象的属性或方法
# 格式：self.属性名 = 值
# class Student:
#     def __init__(self):
#         print("It's Running...")
#         self.person = "Tom"
#         self.age = 14
#
#
# s1 = Student()
# s2 = Student()
# print(f"我叫 {s1.person}, 今年 {s1.age} 了")
# print(f"我叫 {s2.person}, 今年 {s2.age} 了")


# 带参构造方法
# 构造方法也可以携带参数，根据类中属性的定义，传入对应的参数对实例属性进行实始化。
# 格式： __init__(self, args....)
# class Student:
#     def __init__(self, person, age):
#         print("It's Running...")
#         self.person = person
#         self.age = age
#
#     def info(self):
#         print(f"我叫 {self.person}, 今年 {self.age} 了")
#
#
# if __person__ == '__main__':
#     s1 = Student("Tom", 14)
#     s2 = Student("Rose", 18)
#
#     s1.info()
#     s2.info()
#
#     print(s1)
#     print(s2)


# __str__(self) 方法
# 在实例对象后，如果直接打印对象，输出该对象的相关信息，发现实际输出的并不是想要的结果。而是该实例对象的类型和地址。
# 如果想在输出实例对象时，按指定的格式输出，需要实现 __str__(self) 方法
# 该方法不接收除 self 以外的参数，self 参数自动传入，函数只能返回一个字符串。
# class Student:
#     def __init__(self, person, age):
#         self.person = person
#         self.age = age
#
#     def __str__(self):
#         return f"person: {self.person} -- Age: {self.age}"
#
#
# s1 = Student("Tom", 17)
# s2 = Student("Jack", 23)
# print(s1)
# print(s2)


# 【练习】购物车
# 作业要求
# 定义一个商品类，包含 商品名称 和 商品价格 两个属性，
# 实现商品类的对象描述方法和添加到购物车方法
# 定义一个购物车类，包含一个商品列表 属性，和 添加商品 及 显示所有商品 两个方法

class Product:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return {self.name}, {self.price}

    def add_cart(self, cart):
        cart.bookmark[self.name] = self.price

class ShoppingCart:

    def __init__(self, person, bookmark):
        self.person = person
        self.bookmark = {}

    # 购物车显示个人所有商品
    def __str__(self):
        print(f"{self.person} 购买了以下商品：")
        return f"{self.bookmark}"


class Person:
    def __init__(self, cart, person):
        self.cart = cart
        self.person = person

    # 客户挑选商品
    def select(self, goods, price):
        self.person.add_cart(self.cart, goods, price)

    # 清空购物车
    def clear(self):
        self.cart.bookmark.clear()

    # 购买某件商品
    def buy(self, goods):
        self.cart.bookmark.pop(goods)


if __name__ == '__main__':
    cart1 = ShoppingCart("Tom",{})
    tom = Person(cart1, 'Tom')
    tom.select('手机', 5000)
    tom.select('电脑', 10000)
    tom.select('鼠标', 200)
    print(cart1)
    tom.clear()

    cart2 = ShoppingCart("Rose", {})
    rose = Person(cart2, 'Rose')
    rose.select('键盘', 300)
    rose.select('口红', 199)
    rose.select('化妆品', 888)
    rose.buy('化妆品')
    rose.buy('口红')
    print(cart2)