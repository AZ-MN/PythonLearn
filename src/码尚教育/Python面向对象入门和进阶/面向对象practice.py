# class Moive:
# 魔法方法，构造方法
#     def __init__(self):
#         self.name = input("请输入电影名称:")
#         self.director = input("请输入导演:")
#         self.time = input("请输入电影时长:")
# 类方法
#     def get_info(self):
#         print("电影名称：%s" % self.name)
#         print("导演：%s" % self.director)
#         print("电影时长：%s" % self.time)
#
#
# moive = Moive()
# moive.get_info()
# print(moive.name)


class Coder:
    money = 0

    def work(self):
        print("coding")

    def sleep(self):
        print("sleeping")

    def imagine(self):
        print("imagine")


class Xiaowang(Coder):
    company = "程序员"

    def work(self):
        print("practicing")

    def show_company(self):
        print(f"{self.company}")


xiaowang = Xiaowang()
xiaowang.show()
xiaowang.work()
