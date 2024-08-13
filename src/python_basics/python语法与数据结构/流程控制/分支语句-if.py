"""
    流程控制
    1、顺序流程
    2、分支流程
    3、循环流程
"""


# 顺序流程
def order_flow():
    print(1)
    print(2)
    print(3)


# 条件流程
# 分支结构方式一
def if_info():
    # student = "测试工程师"
    # if student == "测试工程师":
    #     print("测试工程师")
    # print("请学习如何成为一名优秀的测试工程师！")

    while True:
        age = int(input("请输入你的年龄："))
        if age >= 18:
            print("已成年\n可以上网吧了！")
            print("可以学习驾照了")


# 分支结构方式二
def if_else_info():
    student = input("请输入你的身份：")
    if student == "测试工程师":
        print("我是测试工程师")
    else:
        print("请学习如何成为一名优秀的测试工程师！")


# 分支结构方式三
def if_elif_info():
    student = input("请输入你的身份：")
    if student == "测试工程师":
        print("我是测试工程师")
    elif student == "运维工程师":
        print("我是运维工程师")
    else:
        print("无论你是那个岗位，都是最优秀的！")


# 嵌套方式
def if_elif_else_info():
    subject = ""
    name = input("请输入你的名字：")
    hobby = int(input("请输入你擅长的科目，文科选1，理科选2："))
    course = []
    if hobby == 1:
        print(name + "擅长文科！")
        subject = "文科"
        choose = int(input("请选择你喜欢的课程，1-语文，2-历史："))
        if choose == 1:
            course.append("语文")
        else:
            course.append("历史")
    elif hobby == 2:
        print(name + "擅长理科！")
        subject = "理科"
        choose = int(input("请选择你喜欢的课程，1-数学，2-物理，3-化学："))
        if choose == 1:
            course.append("数学")
        elif choose == 2:
            course.append("物理")
        else:
            course.append("化学")
    else:
        print("请输入正确的选项！")
    for i in course:
        print(name + "擅长" + subject + "，并且喜欢的科目是：" + i)


if __name__ == '__main__':
    while True:
        # order_flow()
        # if_info()
        # if_else_info()
        if_elif_else_info()
