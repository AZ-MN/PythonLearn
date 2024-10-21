# n1 = int(input("请输入第一个数："))
# n2 = int(input("请输入第二个数："))
# result = 0
#
# try:
#     result = n1 / n2
# except Exception:
#     print("出现错误")
#
# print(result)

# file = open("data.txt", "r")
# try:
#     # 写入数据时可能会有问题
#     file.write("写入的数据")
# except IOError as err:
#     print("文件不能写入", err)
#
# print("main run")
# file.close()
# print("main over")


# file = open("data.txt", "r")
# try:
#     # 写入数据时可能会有问题
#     # file.write("写入的数据")
#     # print(a)
#     print(3 / 0)
#     # print([][10])
#     # print("hello" + 100)
# except IOError as err:
#     print("文件不能写入", err)
# except NameError as err:
#     print("标识符没有定义", err)
# except ZeroDivisionError as err:
#     print("除数不能为0", err)
# except IndexError as err:
#     print("下标越界了", err)
# except Exception as err:
#     print("程序运行出错，请检查代码", err)
# file.close()


# else 操作
# Python 使用 else 在处理在代码无异常时的后续操作。
# try:
#     n = input("请输入一个数字:")
#     num = int(n)
# except Exception as err:
#     print("元素无法转换为数字", err)
# else:
#     print("转换后成功", num)
#     for i in range(num):
#         print("Hogwarts")


# finally 操作
# Python 使用 finally 处理无论异常是否发异，都要执行的代码，一般用来完成清理工作。
try:
   file = open("data.txt", "r")
   file.write("A")
except Exception as err:
    print("文件操作报错", err)
finally:
    file.close()
    print("文件已关闭")
