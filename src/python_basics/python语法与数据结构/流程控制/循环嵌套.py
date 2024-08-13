# 循环嵌套
def loop_info():
    data = [
        [1, 2, 3, 4, 5, 6, 7],
        ["a", "b", "c", "d", "e", "f", "g"],
        ["Hello", "World", "Python", "Hogwarts"]
    ]

    # 嵌套形式一
    # for item in data:
    #     for result in item:
    #         print(result, end=" ")
    #     print()

    # 嵌套形式二
    # i = 0
    # while i < len(data):
    #     j = 0
    #     while j < len(data[i]):
    #         print(data[i][j], end=" ")
    #         j += 1
    #     i += 1
    #     print()

    # 示例一：输出一个九九乘法表
    for i in range(1, 10):
        for j in range(1, 10):
            # print(j, "*", i, "=", i*j, end="  ")
            print(f"{j}*{i}={i*j:<3}", end=" ")  # :< 左对齐
            if i == j:
                break
        print()


if __name__ == '__main__':
    loop_info()