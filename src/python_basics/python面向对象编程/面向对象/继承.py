"""
继承
简介
继承是面向对象编程中的三大概念之二，指的是一个类基于另一个类来创建。
创建出来的新类称为子类或派生类。被继承的类称为父类或基类。
通过继承，子类可以继承父类的属性和方法，并且可以在此基础上添加新的属性和方法，或者对继承的属性和方法进行修改。

继承的主要特点包括：
继承关系：继承创建了一个父类和子类之间的关系。子类继承了父类的特性，包括属性和方法。子类可以重用父类的代码，减少了代码的冗余。
子类的扩展：子类可以在继承父类的基础上，添加新的属性和方法。这样可以对父类进行扩展，使得子类具有更多的功能。
代码共享和重用：通过继承，子类可以共享父类的代码。父类中通用的属性和方法可以被多个子类继承和使用，提高了代码的重用性，并减少了开发时间和成本。
继承的层次结构：继承可以形成一个层次结构，其中一个父类可以有多个子类，而子类又可以成为其他子类的父类。这种层次结构可以更好地组织和管理代码，使得代码更加结构化和模块化。

继承的优势包括：
代码重用：继承允许子类重用父类的代码，减少了代码的冗余，提高了代码的可维护性和复用性。
扩展性：通过继承，子类可以在父类的基础上添加新的属性和方法，实现对父类的扩展，使得子类具有更多的功能。
类型的兼容性：由于子类继承了父类的特性，子类可以被当作父类的实例来使用。这样，在需要父类类型的地方，可以使用子类的实例，增加了代码的灵活性和可扩展性。

需要注意的是，虽然继承可以提供代码重用和扩展的好处，但过度使用继承可能导致代码的复杂性和耦合性增加。因此，在设计代码时，应该合理使用继承，并遵循单一责任原则和开闭原则，保持代码的简洁和灵活。
"""


# 单继承
# 单继承是指一个子类只继承一个父类。
# class A(object):
#     # A 继承自 object 根类
#     def show(self):
#         print("父类A的方法")
#
# class B(A):
#     # B类 继承自 A类
#     def show(self):
#         print("改写父类A的方法")
#     def display(self):
#         print("子类B的方法")
#
# b = B()
# # 子类对象使用自己的方法
# b.display()
# # 子类对象使用父类的方法，如果父类有没有该方法则继续向上查找，直到根类
# b.show()


# 方法重写
# 在子类中，可以对父类中的方法实现进行重写，实现新的功能实现。
# class A(object):
#     # A 继承自 object 根类
#     def show(self):
#         print("父类A的方法")
#
#
# class B(A):
#     # 子类重写父类方法
#     def show(self):
#         print("子类B的方法")
#
#
# b = B()
# # 当子类方法与父类方法同名时，调用子类方法
# b.show()


# super() 函数
# 如果在子类中还要使用父类中的方法，可以使用 super() 函数来调用父类中的方法。
# 比如在重写父类方法时，还要保留父类方法的功能。
# class A(object):
#     # A 继承自 object 根类
#     def show(self):
#         print("父类A的方法")
#
#
# class B(A):
#     # 子类重写父类方法
#     def show(self):
#         # 使用 super() 调用父类方法
#         super().show()
#         print("子类B的方法")
#
#
# b = B()
# # 当子类方法与父类方法同名时，调用子类方法
# b.show()


# 单继承的初始化
# 在子类对象初始化时，需要给出父类初始化所需的参数，然后使用 super() 调用父类初始化方法去初始化父类的属性。
# class A(object):
#     # A 继承自 object 根类
#     def __init__(self, a):
#         self.a = a
#
#
# class B(A):
#     def __init__(self, a, b):
#         super().__init__(a)
#         self.b = b
#
#
# b = B("A","B")
# print(b.a)
# print(b.b)


# 继承的访问控制
# 无论在方法的重写，还是初始化时，父类的工作就让父类自己去完成，子类只负责自己部分的实现。
# 比如：如果在初始化时，想在子类中初始化父类的一个私有属性，这是不能实现的，但是可以调用父类的初始化方法对私有属性进行初始化
# class A:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def show(self):
#         print(f'A: {self.a}')
#         print(f'B: {self.b}')
#         print(f'C: {self.c}')
#
# class B(A):
#     def __init__(self, a, b, c, d):
#         super().__init__(a, b, c)
#         self.d = d
#
#     def show(self):
#         super().show()
#         print(f'D: {self.d}')
#
#
# if __name__ == '__main__':
#     b = B(2, 3, 4, 5)
#     b.show()


# 多继承
# 多继承是指一个子类可以同时继承多个父类，此时子类同时拥有多个父类中的属性和方法
# class FA(object):
#     def fa_show(self):
#         print("FA Show Run...")
#
#
# class FB(object):
#     def fb_show(self):
#         print("FB Show Run...")
#
#
# class S(FA, FB):
#     def s_show(self):
#         print("S Show Run...")
#
#
# s = S()
# s.s_show()
# s.fa_show()
# s.fb_show()


# 多继承同名方法查找顺序
# 如果在一个子类所继承的多个父类中，具有同名方法，那么在调用该方法名的方法时，Python 会使用 C3 算法实现的 MRO（方法解析顺序）顺序来确定查找的先后顺序，一般情况可以理解成是按继承类的书写顺序。
# class FA(object):
#     def show(self):
#         print("FA Show Run...")
#
#
# class FB(object):
#     def show(self):
#         print("FB Show Run...")
#
#
# class S(FB, FA):
#     def s_show(self):
#         print("S Show Run...")
#
#
# s = S()
# s.s_show()
# s.show()


# 多继承初始化
# 在多继承中，由于有多个父类，每个父类的属性都需要单独初始化，这时 super() 函数只能引用继承书写顺序上的第一个父类，其它的父类是无法通过 super()引用的，所以也就无法利用 super()函数进行初始化。
# 此时，可以使用直接指定父类名的方式调用该父类中的方法。
# 此方法也适用于多继承中的方法重写。
class FA(object):
    def __init__(self, a):
        self.a = a


class FB(object):
    def __init__(self, b):
        self.b = b


class S(FB, FA):
    def __init__(self, a, b, c):
        FA.__init__(self, a)
        FB.__init__(self, b)
        # super().__init__(a)  # 初始化无法用super() 函数
        # super().__init__(b)
        self.c = c


c = S(1, 2, 3)
print(c.a)
print(c.b)
print(c.c)
