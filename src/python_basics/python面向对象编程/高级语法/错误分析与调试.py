# def input_data():
#     n = input("请输入一个数字：")  # 输入字符串类型的值
#     msg = input("请输入一个字符串信息：")
#     return n, msg
#
#
# def output_data(n, msg):
#     for i in range(n):
#         print(f"第 {i + 1} 次输出{msg}")
#
#
# if __name__ == '__main__':
#     n, msg = input_data()
#     output_data(n, msg)


def decorator(func):
    def inner(*args, **kwargs):
        print("装饰器内容1")
        result = func(*args, **kwargs)
        print("装饰器内容2")
        return result
    return inner
# show = decorator(show)
@decorator
def show():
    print("Show Run")


if __name__ == '__main__':
    show()