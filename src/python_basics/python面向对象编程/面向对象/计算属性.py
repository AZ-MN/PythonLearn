"""
计算属性
简介
在封装类时，如果实例属性定义为公有属性，在使用过程中不安全，一般建议定义为私有属性，但是私有属性又不能在类的外部直接访问，此时，需要为私有实例属性提供访问的操作接口方法。

属性访问器和修改器
属性访问器：也称为 Getter 方法，用来返回某个属性的值，该方法无参数，但必须有返回值，一般以 get_xxx 命名。 属性修改器：也称为 Setter 方法，用来给某个属性值进行修改，该方法接收一个参数，且无返回值，一般以 set_xxx 命名。
"""

# 常规写法
# class Person(object):
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     def get_name(self):
#         return self._name
#
#     def set_name(self, name):
#         self._name = name
#
#
# if __name__ == '__main__':
#     obj = Person("Tom", 18)
#
#     print(obj.get_name())
#     obj.set_name("Jack")
#
#     print(obj.get_name())

# 虽然实现了需求，但此方式在使用实例属性时，变成了以方法形式使用，不够简洁。


"""
@property 装饰器
Python 提供了一个名为 property 的装饰器，通过该装饰器可以为私有属性提供访问器和修改器方法，但在使用时，依然可以以属性的形式进行使用。

提供数据访问功能（getter）
计算属性
语法：使用@property装饰器
调用：实例.方法名
提供数据操作功能（setter）
语法：使用@计算属性名.setter装饰器
调用：实例.方法名
注意：

当定义计算属性时，必须先使用 property 装饰器定义计算属性的访问器访问，然后才可以利用计算属性名定义修改器方法。
访问器方法和修改器方法不需要再使用 get 和 set 做为前缀。
"""


class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def username(self):
        return self._name

    @username.setter
    def username(self, name):
        if name.isalpha():
            self._name = name
        else:
            print("数据有误")


if __name__ == '__main__':
    obj = Person("Tom", 12)
    print(obj.username)
    obj.username = "123"
    print(obj.username)
