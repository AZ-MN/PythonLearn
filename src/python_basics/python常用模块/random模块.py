"""
random 模块
简介
random 是 Python 内置的用于生成随机数的模块。
它提供了多种随机数生成函数，用于各种不同的随机数需求。
"""

# random 常用方法
# random.random()：生成一个 [0,1) 范围内的随机浮点数。
import random

print(random.random())

# random.randint(a,b)：生成一个 [a,b] 范围内的随机整数。

print(random.randint(1, 3))

# random.uniform(a,b)：生成一个 [a,b] 范围内的随机浮点数。

print(random.uniform(1, 3))

# random.choice(seq)：从序列 seq 中随机选择一个元素。seq 是自定义的序列。

seq = (1, 2, 3, "Tom", "Jack", "Sally")
print(random.choice(seq))

print("*" * 20)
# random.shuffle(lst)：随机打乱列表 lst 的元素顺序。

lst = list(seq)

for i in range(3):
    random.shuffle(lst)
    rdm = random.choice(lst)
    lst.remove(rdm)
    print(rdm)
