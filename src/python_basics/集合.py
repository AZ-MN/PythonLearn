# 集合的使用
# 集合是一个无序的、不重复的数据集合
def set_info():
    # 创建集合
    s1 = set()
    s2 = {}
    print(s1, s2)
    print(type(s1), type(s2))

    # 集合添加元素
    s3 = {8, 2, 3, 4, 5, 5, 234, 33, 16}
    s3.add(6)
    s3.add(0)
    s3.add(24)
    s3.add("helloworld")
    print(s3)
    print(type(s3))

    # 集合唯一性元素的特性使用
    nums = [1, 2, 3, 4, 5, 5, 5, 5, 5]
    s4 = set(nums)
    print(s4)
    # 集合不支持索引，即不能通过下标获取元素
    # print(s4[0])
    nums = list(s4)
    print(nums)

    # 集合计数
    print(len(s4))

    # 集合更新
    s4.update([6, 7, 8])
    s4.update((8, 9, 10))
    print(s4)

    # 集合删除元素
    s4.remove(1)

# 运行程序
set_info()