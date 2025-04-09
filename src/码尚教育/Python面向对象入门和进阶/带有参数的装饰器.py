# 目前加减法的函数，拿到对应的符号进行判断再输出内容

def cal(flag):  # flag = "+"
    def outer(f):  # outer(add), f = add
        def inner(num1, num2):  # inner(num1, num2) = add(num1, num2) = f(num1, num2)
            print(f"你输入的装饰器符号是 {flag}, 输入的参数是 {num1} 和 {num2}, 运算结果是 {f(num1, num2)}")

        return inner  # inner = add(num1, num2)

    return outer  # outer = add


@cal("+")  # 相当于 outer(add)
def add(num1, num2):
    return num1 + num2


add(1, 2)


@cal("-")
def sub(num1, num2):
    return num1 - num2


sub(5, 3)
