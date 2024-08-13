import copy

# 原始数据
originDate = [[1, 2], {"name": "Tom", "age": 23, "chars": ["a", "b"]}]

# 浅拷贝
# 浅拷贝只拷贝第一层，如果嵌套了列表，则只拷贝第一层
# 使用对象的copy()方法得到浅拷贝对象
shallowCopy1 = originDate.copy()
# 使用工厂方法获取浅拷贝对象
shallowCopy2 = list(originDate)
# 使用切片方式获取浅拷贝对象
shallowCopy3 = originDate[:]
# 使用copy模块中的copy()方法获取浅拷贝对象
shallowCopy4 = copy.copy(originDate)

# 浅拷贝成功的验证，内容相同，但地址不同
# 查看所有对象内容
print(originDate)
print(shallowCopy1)
print(shallowCopy2)
print(shallowCopy3)
print(shallowCopy4)
print(originDate == shallowCopy1 == shallowCopy2 == shallowCopy3 == shallowCopy4)  # True

# 查看所有对象的地址
print(id(originDate))
print(id(shallowCopy1))
print(id(shallowCopy2))
print(id(shallowCopy3))
print(id(shallowCopy4))
print(id(originDate) == id(shallowCopy1) == id(shallowCopy2) == id(shallowCopy3) == id(shallowCopy4))  # False

# 当修改任意对象后，所有对象的值都会发生改变
shallowCopy3[1]["chars"][1] = "bbb"

# 查看所有对象的值
print(originDate)
print(shallowCopy1)
print(shallowCopy2)
print(shallowCopy3)
print(shallowCopy4)

# 深拷贝
# 深拷贝会拷贝所有层，包括嵌套的列表
# 使用copy模块中的deepcopy()方法得到深拷贝对象
deepCopy1 = copy.deepcopy(originDate)

# 深拷贝成功的验证，内容相同，但地址不同
# 查看原始对象和深拷贝对象的内容
print("深拷贝")
print(originDate)
print(deepCopy1)

# 查看原始对象和深拷贝对象的地址
print(id(originDate))
print(id(deepCopy1))

# 当修改任意对象后，其他对象的值不会发生改变
deepCopy1[0][1] = 3
deepCopy1[1]["chars"][0] = "aaa"

print(originDate)
print(deepCopy1)

stu = [
    {"name": "Tom", "age": 23},
    {"name": "Jack", "age": 38},
    {"name": "Alice", "age": 21},
    {"name": "Jams", "age": 65},
    {"name": "Rose", "age": 19}
]
stu.sort(key=lambda x: x["name"])
print(stu)
stu.sort(key=lambda x: x["age"])
print(stu)

print(sorted(stu, key=lambda x: x["name"]))


# 实现一个自己的sorted方法
def my_sorted(data, key=None):
    data_copy = copy.deepcopy(data)
    data_copy.sort(key=key)
    return data_copy


print(my_sorted(stu, key=lambda x: x["age"]))
