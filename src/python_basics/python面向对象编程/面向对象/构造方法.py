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
#         self.name = "Tom"
#         self.age = 14
#
#
# s1 = Student()
# s2 = Student()
# print(f"我叫 {s1.name}, 今年 {s1.age} 了")
# print(f"我叫 {s2.name}, 今年 {s2.age} 了")


# 带参构造方法
# 构造方法也可以携带参数，根据类中属性的定义，传入对应的参数对实例属性进行实始化。
# 格式： __init__(self, args....)
# class Student:
#     def __init__(self, name, age):
#         print("It's Running...")
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"我叫 {self.name}, 今年 {self.age} 了")
#
#
# if __name__ == '__main__':
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
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name} -- Age: {self.age}"


s1 = Student("Tom", 17)
s2 = Student("Jack", 23)
print(s1)
print(s2)
