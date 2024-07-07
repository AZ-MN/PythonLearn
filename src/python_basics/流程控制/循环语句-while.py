# 循环语句while
# 输出100次 Hogwarts
def print_100():
    # 循环构成要素1，循环变量初始化
    i = 1
    # 实现循环语句要素2，设置循环结束条件
    while i <= 100:
        # 循环语句要素3，循环体输出内容
        print("Hogwarts", i)
        # 循环语句要素4，循环变量趋近于结束
        i += 1


# 实战一
# 求1-100的累加和
def loop_func1():
    n = 1
    sum = 0
    while n <= 100:
        sum += n
        n += 1
    print(sum)


# 实战二
# 求1-10的累乘积
def loop_func2():
    n = 1
    result = 1
    while n <= 10:
        result *= n
        print(result)
        n += 1
    print("result:", result)


# 实战三
# 输入密码，只有输入正确的密码，才打印“登录成功”
def loop_func3():
    password = input("请输入密码：")
    while password != "Hogwarts":
        password = input("密码错误，请重新输入：")
    print("登录成功")


# 实战四
# 在行酒令中，有一个数7的小游戏，游戏参与者需要依次报数，但需要跳过7的倍数以及包含7的数字，编写程序找出100以内符合条件的数字并打印出来
def loop_func4():
    i = 1
    while i <= 100:
        # 7的倍数：i % 7 取余，余数为0，说明被整除，是7的倍数
        # 包含7的数字：7 in str(i)，如果数字在转换后的结果里，说明包含7
        if i % 7 == 0 or "7" in str(i):
            print(i)
        i += 1

# 程序入口
if __name__ == '__main__':
    # print_100()
    # loop_func1()
    # loop_func2()
    # loop_func3()
    loop_func4()