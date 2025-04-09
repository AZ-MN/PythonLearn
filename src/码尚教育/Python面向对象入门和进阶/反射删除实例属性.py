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


x = A()
# 删除对象的实例属性
# print(x.i)
# delattr(x, "i")
# print(x.i)  # AttributeError: 'A' object has no attribute 'i', 因为x对象的i属性被删除了，所以会报错

# print(x.o)
# delattr(x, "o")  # 类属性和实例方法类方法都不能删除，只能删除对象的实例属性

print(x, "d")
delattr(x, "d")

# 通过dealttr()内建函数可以删除对象的实例属性
