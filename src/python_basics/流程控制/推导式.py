# 元组推导式
"""
格式: (out_exp_res for item in Sequence) 或 (out_exp_res for item in Sequence if conditional)
    out_exp_res：生成元素表达式，可以是有返回值的函数。
    for out_exp in Sequence：迭代 Sequence 将 out_exp 传入到 out_exp_res 表达式中。
    if condition：条件语句，可以过滤 Sequence 中不符合条件的值。
"""
# 示例:
# 简单的元组推导式
t1 = (x for x in range(1, 10))
# for out_exp in t1:
#     print(out_exp)

# 生成128位ASCII码元组
t2 = ((chr(x), x) for x in range(129))
# for out_exp in t2:
#     print(out_exp)

# 生成100以内能被7整除所有数字的元组
t3 = (x for x in range(100) if x % 7 == 0)
# for out_exp in t3:
#     print(out_exp)

# 生成99乘法表结果元组
t4 = (x*y for x in range(1, 10) for y in range(1, x+1))
# for out_exp in t4:
#     print(out_exp)

# 将元组中的字符串转换为大写
words = ("apple", "banana", "cherry")
upper_words = (word.upper() for word in words)
# for out_exp in upper_words:
#     print(out_exp)


# 列表推导式
"""
列表推导式与元组推导式的区别: 格式上外部由圆括号包裹的表达式改为中括号
格式：[out_exp_res for item in Sequence] 或 [out_exp_res for item in Sequence if conditional]
"""
# 简单的元组推导式
l1 = [x for x in range(1, 10)]
# for out_exp in l1:
#     print(out_exp)
# print("*" * 10)

# 生成128位ASCII码元组
l2 = [chr(x) for x in range(128)]
# for out_exp in l2:
#     print(out_exp)
# print("*" * 10)

# 生成100以内能被7整除所有数字的元组
l3 = [x for x in range(100) if x % 7 == 0]
# for out_exp in l3:
#     print(out_exp)
# print("*" * 10)

# 生成99乘法表结果元组
l4 = [x*y for x in range(1, 10) for y in range(1, x+1)]
# for out_exp in l4:
#     print(out_exp)
# print("*" * 10)

# 将列表中的字符串转换为大写
words = ["apple", "banana", "cherry"]
upper_Words = [word.upper() for word in words]
# for out_exp in upper_Words:
#     print(out_exp)


# 字典推导式
"""
字典推导式与前两种推导式的区别: 
推导式使用花括号包裹;
结果表达式需要使用 key-value 形式。
格式：{key_expr: value_expr for value in collection} 或 {key_expr: value_expr for value in collection if condition}
"""
# 将列表中各字符串值为键，各字符串的长度为值，组成键值对
names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_dict = {name: len(name) for name in names}
# for item in new_dict.items():
#     print(item)
# for k, v in new_dict.items():
#     print(k, v)


# 集合推导式
# 集合推导式与字典推导式的区别在于结果表达式是单一结果，不是 key-value 形式
"""
格式: {expression for item in Sequence} 或 {expression for item in Sequence if conditional}
"""
# 筛选列表中的数字字符串
data = ['Bob', '123', 'Tom', 'ab123', 'alice', '123abc', 'Jerry', '456', 'Wendy', '554', 'Smith']
# 推导式写法
new_set = {n for n in data if n.isdigit()}
for i in new_set:
    print(i)

# 冗余写法
# d = []
# for x in data:
#     if x.isdigit():
#         d.append(x)
# for i in d:
#     print(i)
