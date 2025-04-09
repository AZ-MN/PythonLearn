class A:
    o = 888

    def __init__(self):
        self.i = 666

    def a(self):
        print("调用a实例方法")

    def b(self):
        print("调用b实例方法")

    def c(self):
        print("调用c实例方法")

    def d(self):
        print("调用d实例方法")

    @classmethod
    def e(cls):
        print("调用e类方法")


x = A()

# 可以把该对象的所有属性和方法进行引用后再传递和调用
# f = getattr(x, 'a')
# f()  # 调用a实例方法
#
# f2 = getattr(x, 'e')
# f2()  # 调用e类方法
#
# o_2 = getattr(x, 'o')
# print(o_2)
#
# i_2 = getattr(x, 'i')
# print(i_2)
#
# # 函数和方法的引用都是可以传递的
# func = getattr(x, 'a')
# func()  # func() = x.a()

# 通过遍历获取对象中的所有属性和方法
for i in ['a', 'b', 'c', 'd', 'e']:
    func = getattr(x, i)
    func()

for j in ['o', 'i']:
    y = getattr(x, j)
    print(y)

# 通过getattr（）内建函数读取对象所有的属性和方法，进行引用传递之后，调用

