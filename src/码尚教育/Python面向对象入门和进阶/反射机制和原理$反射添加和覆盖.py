# 反射的原理
# 基于面向对象的基础，通过使用字符串对象对应对象中的具体某个属性或者方法
# 可以对实例对象属性或者方法进行修改或者调用
# 添加
# 删除
# 修改
# 查看

# 反射添加和覆盖
class A:
    def a(self):
        print("调用a实例方法")

    def b(self):
        print("调用b实例方法")

    def c(self):
        print("调用c实例方法")

    def d(self):
        print("调用d实例方法")


def func():
    print("调用func函数")


x = A()
y = A()

# 给对象添加新的方法: 前提必须要有该方法或者函数的引用
# setattr(x, "e", input)
# password = x.e("请输入密码：")
# print(password)

# setattr(x, "w", func)
# x.w()
# y.e()  # 'A' object has no attribute 'e', 因为x对象没有e方法，所以会报错, 给对象设置的方法，仅限于被设置的对象本身，对类没有影响

x.a()
setattr(A, "a", print)
x.a("我不是a方法")  # a() = print()
# 被反射之后的对象调用方法时，会被覆盖之前的方法或属性
# 通过setattr内建函数完成对象的新增方法和覆盖原来的方法
