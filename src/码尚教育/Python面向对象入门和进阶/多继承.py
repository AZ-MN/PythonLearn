class A:
    def __init__(self):
        self.a = "aaa"

    def b(self):
        print("A类中的b 实例方法被调用")
        return "实例方法b的返回值"

    @classmethod
    def c(cls):
        print("A类中的c 类方法被调用")
        return "类方法c的返回值"

    @staticmethod
    def d():
        print("A类中的d 静态方法被调用")
        return "静态方法d的返回值"


class B:
    i = 1

    def __init__(self):
        self.e = "bbb"

    def b(self):
        print("B类中的b 实例方法被调用")


class C(A, B):
    def __init__(self):
        super().__init__()
        self.e = "ccc"

    pass


c = C()
print(c.a)
print(c.i)
c.b()
c.c()
c.d()
