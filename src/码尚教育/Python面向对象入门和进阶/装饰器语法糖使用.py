import time


# 计算程序运行时间

def get_time(f):
    def inner():
        start = time.time()
        f()
        stop = time.time()
        print(f"程序运行的时长为 {stop - start} 秒")

    return inner

# 装饰器的语法糖格式，@ + 函数名，并且必须放到函数定义的上面
@get_time
def test():
    for i in range(100000):
        print(i)
    else:
        time.sleep(2)
        print("循环结束")


test()  # 此时执行的test()函数，实际上是执行inner()
# test = get_time(test)
# test()


