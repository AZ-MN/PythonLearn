class A:
    pass


class B(A):
    d = 4

    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

    def show(self):
        print(f'A: {self.a}')
        print(f'B: {self.b}')
        print(f'C: {self.c}')
        print(f'D: {self.d}')


b = B()
b.show()
