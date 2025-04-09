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
# 使用反射内建函数hasattr()判断对象是否存在该对象的所有方法和属性中
print(hasattr(x, "a"))  # True
print(hasattr(x, "b"))  # True
print(hasattr(x, "c"))  # True
print(hasattr(x, "d"))  # True
print(hasattr(x, "o"))  # True
print(hasattr(x, "i"))  # True
print(hasattr(x, "e"))  # False
print(hasattr(x, "f"))  # False
print("-" * 50)
delattr(x, "i")
# 使用反射内建函数delattr()删除对象属性, 该属性就不会被hasattr()判断到
print(hasattr(x, "i"))

# 可以使用内建函数hasattr（）判断对象是否存在该属性或者方法（所有的属性和方法）
