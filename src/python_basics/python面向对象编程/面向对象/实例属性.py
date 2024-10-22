"""
实例属性
动态绑定
Python 中的属性变量都是使用动态绑定的方式绑定到实例对象上的。
"""

# 格式：实例对象名.实例属性名
# class Student:
#     def info(self):
#         print(f"我叫 {self.name}, 今年 {self.age} 岁了")
#
# if __name__ == '__main__':
#     # 实例对象
#     s1 = Student()
#     s2 = Student()
#
#     print(s1)
#     print(s2)
#
#     # 为实例对象s1动态绑定属性
#     s1.name = "Tom"
#     s1.age = 22
#     # 访问实例对象s1的属性
#     print(s1.name)
#     print(s1.age)
#
#     s1.info()
#
#     # 输出什么？
#     print(s2.name)
#     print(s2.age)

# 从代码中可以看出，在使用动态绑定属性时，给哪个实例对象绑定的属性，哪个对象才会拥有属性变量，没有绑定的则没有。
# 这显示是不符合面向对象思想的。

class Student:
    def born(self, name, age):
        self.name = name
        self.age = age


    def info(self):
        print(f"我叫 {self.name}, 今年 {self.age} 岁了")

if __name__ == '__main__':
    s1 = Student()
    s2 = Student()

    s1.born("Tom", 12)
    s2.born("Jack", 20)
    s1.info()
    s2.info()