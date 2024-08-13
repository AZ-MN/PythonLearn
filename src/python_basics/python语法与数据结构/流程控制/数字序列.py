# range函数的使用
def range_info():
    # range(start, stop, step)
    # range函数不会直接返回一个数列
    nums = range(0, 10)
    print(nums)  # range(1, 10)

    # 获得 0-10 范围的数组（前闭后开），转换成数组打印
    nums = list(range(0, 10))
    print(nums)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 使用默认开始值，默认步长
    nums = list(range(10))
    print(nums)

    # 确定开始值和步长
    nums = list(range(0, 10, 2))
    print(nums)

    # 使用负步长
    nums = list(range(10, 0, -3))
    print(nums)

    # for-in结合range()函数可实现计次循环
    for num in range(10):
        print(num)

    # 计算1-100的整数和
    result = 0
    for sum in range(1, 101, 1):
        result += sum
        # 冗余代码
        # if sum == 100:
        #     print(result)
    print(result)


# 随机数
# 导入随机数函数
from random import randint


def random_info():
    num = randint(0, 10)  # 前后都可取，闭集
    print(num)


# 实战练习：骰子游戏，比较大小，点数大者胜
def dice_game():
    # 定义变量记录胜场数
    # player_win_count = 0
    # bot_win_count = 0
    # while player_win_count != 3 and bot_win_count != 3:
    #     player_num = randint(1, 6)
    #     bot_num = randint(1, 6)
    #     if player_num == bot_num:
    #         # print("玩家点数:", player_num, "\n电脑点数:", bot_num, "\n平局！")
    #         # print(f"玩家点数:{player_num}, \n电脑点数:{bot_num} \n平局！")
    #         player_win_count = player_win_count
    #         bot_win_count = bot_win_count
    #     elif player_num > bot_num:
    #         # print("玩家点数:", player_num, "\n电脑点数:", bot_num, "\n玩家胜！")
    #         # print(f"玩家点数:{player_num}\n电脑点数:{bot_num}\n玩家胜！")
    #         player_win_count += 1
    #     else:
    #         # print("玩家点数:", player_num, "\n电脑点数:", bot_num, "\n电脑胜！")
    #         # print(f"玩家点数:{player_num}\n电脑点数:{bot_num}\n电脑胜！")
    #         bot_win_count += 1
    # if player_win_count == 3:
    #     print(f"玩家胜场数:{player_win_count}\n电脑胜场数:{bot_win_count}\nPlayer win!")
    # else:
    #     print(f"玩家胜场数:{player_win_count}\n电脑胜场数:{bot_win_count}\nBot win!")

    # 使用range函数实现三局两胜
    player_win_count = 0
    bot_win_count = 0
    for num in range(3):
        player_num = randint(1, 6)
        bot_num = randint(1, 6)
        if (player_win_count == 2 and bot_win_count == 0) or (player_win_count == 0 and bot_win_count == 2):
            break
        if player_num == bot_num:
            # print("玩家点数:", player_num, "\n电脑点数:", bot_num, "\n平局！")
            # print(f"玩家点数:{player_num}, \n电脑点数:{bot_num} \n平局！")
            player_win_count = player_win_count
            bot_win_count = player_win_count
        elif player_num > bot_num:
            # print("玩家点数:", player_num, "\n电脑点数:", bot_num, "\n玩家胜！")
            # print(f"玩家点数:{player_num}\n电脑点数:{bot_num}\n玩家胜！")
            player_win_count += 1
        else:
            # print("玩家点数:", player_num, "\n电脑点数:", bot_num, "\n电脑胜！")
            # print(f"玩家点数:{player_num}\n电脑点数:{bot_num}\n电脑胜！")
            bot_win_count += 1
    if player_win_count > bot_win_count:
        print(f"玩家胜场数:{player_win_count}\n电脑胜场数:{bot_win_count}\nPlayer win!")
    elif player_win_count < bot_win_count:
        print(f"玩家胜场数:{player_win_count}\n电脑胜场数:{bot_win_count}\nBot win!")
    else:
        print(f"玩家胜场数:{player_win_count}\n电脑胜场数:{bot_win_count} \ndraw!")



if __name__ == '__main__':
    # range_info()
    # random_info()
    dice_game()
