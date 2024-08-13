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
    s4.update(s3)
    print(s4)

    # 集合删除pop()
    s = {23, 3423, 83, 1, 2, 7, 3}
    print(s)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s)

    # 集合删除remove()
    s = {23, 3423, 83, 1, 2, 7, 3}
    print(s)
    res = s.remove(3)
    print(res)
    print(s)

    # 集合删除discard()
    res = s.discard(23)
    print(s)
    res = s.discard(23)
    print(s)
    res = s.discard(23)
    print(s)
    res = s.discard(23)
    print(s)

    # 集合删除clear()
    s = {23, 3423, 83, 1, 2, 7, 3}
    print(s)
    res = s.clear()
    print(s)
    print(res)
    print("*" * 10)

    # 判断两个集合是否不相交
    s = {1, 2, 3}
    print(s.isdisjoint({3, 4, 5}))
    print(s.isdisjoint({7, 8, 9}))
    print("*" * 10)

    # 判断一个集合是否是另一个集合的子集
    s = {1, 2, 3}
    print(s.issubset({1, 2}))
    print(s.issubset({1, 2, 3}))
    print(s.issubset({1, 2, 3, 4}))
    print(s.issuperset({3, 4, 5}))
    print("*" * 10)

    # 也可以通过关系运算符判断
    s = {1, 2, 3}
    print(s <= {1, 2})
    print(s <= {1, 2, 3})
    print(s <= {1, 2, 3, 4})
    print(s <= {3, 4, 5})
    print("*" * 10)

    # 判断是否为真子集
    s = {1, 2, 3}
    print(s < {1, 2})
    print(s < {1, 2, 3})
    print(s < {1, 2, 3, 4})
    print(s < {3, 4, 5})
    print("*" * 10)

    # 判断集合是否是另一个集合的超集
    s = {1, 2, 3}
    print(s.issuperset({1, 2}))
    print(s.issuperset({1, 2, 3}))
    print(s.issuperset({1, 2, 3, 4}))
    print(s.issuperset({3, 4, 5}))
    print("*" * 10)
    # 也可以通过运算符 >= 判断
    s = {1, 2, 3}
    print(s >= {1, 2})
    print(s >= {1, 2, 3})
    print(s >= {1, 2, 3, 4})
    print(s >= {3, 4, 5})
    print("*" * 10)
    # 判断是否为真超集
    s = {1, 2, 3}
    print(s > {1, 2})
    print(s > {1, 2, 3})
    print(s > {1, 2, 3, 4})
    print(s > {3, 4, 5})
    print("*" * 10)

    # 集合的并集
    print("并集")
    s1 = {1, 2, 3}
    s2 = {4, 5, 6}
    s3 = {6, 7, 8}
    print(s1.union(s2))
    print(s1.union(s2, s3))
    # 也可以通过运算符 | 运算
    print(s1 | s2)
    print(s1 | s2 | s3)

    # 集合的交集
    print("交集")
    s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    s2 = {4, 5, 6}
    s3 = {6, 7, 8}
    s4 = {10}
    print(s1.intersection(s2))
    print(s1.intersection(s2, s3))
    print(s1.intersection(s2, s3, s4))
    # 也可以通过运算符 & 运算
    print(s1 & s2)
    print(s1 & s2 & s3)
    print(s1 & s2 & s4)

    # 集合的差集
    print("差集")
    s1 = {1, 2, 3, 4, 5, 6}
    s2 = {4, 5, 6}
    s3 = {6, 7, 8}
    print(s1.difference(s2))
    print(s1.difference(s2, s3))
    print(s1.difference(s3))
    # 也可以通过运算符 - 运算
    print(s1 - s2)
    print(s1 - s2 - s3)
    print(s1 - s3)

    # 集合的对称差集
    print("对称差集")
    s1 = {1, 2, 3, 4}
    s2 = {4, 5, 6, 7}
    print(s1.symmetric_difference(s2))
    # 也可以通过运算符 ^ 运算
    print(s1 ^ s2)


# 运行程序
set_info()
