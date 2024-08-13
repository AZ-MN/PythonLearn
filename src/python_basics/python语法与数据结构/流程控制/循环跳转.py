# 死循环
# 示例一：
# while True:
#     print("Hello World")

# 示例二：从键盘持续输入数据，每输入一次，将数据添加到列表中保存
# data = []
# while True:
#     s = input("请输入数据添加到库中：")
#     data.append(s)
#     print(data)


# break语句
# 示例三：优化上面代码
# data = []
# while True:
#     s = input("请输入数据添加到库中：")
#     if s == "bye":
#         break
#     data.append(s)
#     print(data)

# 示例四：break 语句出现在多层循环中时，所处在哪个循环的循环体内，就跳出哪个循环，更外层的循环不受影响
# for i in range(1, 4):
#     print(i)
#     for j in range(1, 6):
#         if j == 2:
#             break
#         print(j)


# continue语句
# 示例五：
# for i in range(1, 4):
#     print(i)
#     for j in range(1, 4):
#         if j == 2:
#             continue
#         print(j)

# 示例六：大多数情况下，可以通过改变条件的方式，避免 continue 的使用，而使代码更简洁
# for i in range(1, 4):
#     print(i)
#     for j in range(1, 4):
#         if j != 2:
#             print(j)


# loop-else语句
# 在Python中,不只if语句可以使用else,循环语句也可以使用else
# 当一个循环没有被break中断而正常循环结束,就会执行else后的代码块
# 示例七：
# for i in range(5):
#     print(i)
# else:
#     print("Over")

# 示例八：如果循环被中断,则不会执行else后的语句
# for i in range(5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("Over")

# 示例九：查询学生信息
stu = [
    {"name": "Rose", "age": 18},
    {"name": "Bob", "age": 23},
    {"name": "Alice", "age": 48},
    {"name": "Jack", "age": 16},
    {"name": "Jim", "age": 7},
]
name = input("请输入你想要查询人员姓名：")

# 不使用else形式
# is_exist = False
# for s in stu:
#     if name == s["name"]:
#         is_exist = True
#         print(s)
#         break
# if not is_exist:
#     print("没有此人！！！")

# 使用else形式
for s in stu:
    if name == s["name"]:
        print(s)
        break
else:
    print("没有此人！！！")

