# 随便定义一些方法、变量


def show():
    print("custom_module run")


num: int = 20


isApproved: bool = False

# 导入模块时会被执行一遍，放入程序入口里面会避免在导入的时候执行
# show()


if __name__ == '__main__':
    show()

