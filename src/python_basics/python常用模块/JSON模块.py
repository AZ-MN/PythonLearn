"""
JSON 模块
简介
JSON（JavaScript Object Notation, JS对象简谱）是一种轻量级的数据交换格式，用于在不同应用程序之间传输和存储数据。
它以文本形式表示结构化数据，易于理解和编写，同时也易于计算机解析和生成。

JSON 的结构规则
对象：用花括号 {} 包裹,包含一系列键值对，每个键值对之间用逗号 , 分隔。
数组：用方括号 [] 包裹，包含一系列值，每个值之间用逗号 , 分隔。
键值对：键和值之间使用冒号 : 分隔，键必须是字符串，值可以是字符串、数字、布尔值、对象、数组、或null
"""

# JSON数据的最外层只能是数组或对象
# JSON中的字符串，必须使用双引号包含
"""
{
    "name": "John",
    "age": 30,
    "is_student": false,
    "address": {
        "city": "New York",
        "zip": "10001"
    },
    "hobbies": ["reading", "swimming", "traveling"]
}
"""

# Python 与 JSON 数据类型对应
"""
Python	    JSON
dict	        object
list, tuple	array
str	        string
int, float	number
True	        true
Flase	        false
None	        null
"""

# JSON 序列化与反序列化
# JSON 的序列化指的是将 Python 对象转换为 JSON 格式的字符串。
# 通过序列化，Python 对象可以被编码为符合 JSON 规范的字符串，从而可以在不同的应用程序、平台或语言之间进行数据交换。
# json.dumps()：可以完成序列化的操作。这个函数将 Python 的数据结构转换为 JSON 格式的字符串。
# import json

# 定义一个Python字典
# data = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }

# 将Python字典序列化为JSON格式的字符串
# json_str = json.dumps(data)
# print(json_str)


# data = {
#     "code": 200,
#     "message": "OK",
#     "data": [
#         {
#             "id": "0001",
#             "name": "iPhone",
#             "price": 8999,
#             "is_sale": True
#         },
#         {
#             "id": "0002",
#             "name": "Mac",
#             "price": 21999,
#             "is_sale": True
#         },
#         {
#             "id": "0003",
#             "name": "Watch",
#             "price": 6999,
#             "is_sale": True
#         },
#
#     ]
# }


# 将Python字典序列化为JSON格式的字符串
# json_str = json.dumps(data)
# print(json_str)
# 序列化后的data
json_str = '{"code": 200, "message": "OK", "data": [{"id": "0001", "name": "iPhone", "price": 8999, "is_sale": true},{"id": "0002", "name": "Mac", "price": 21999, "is_sale": true},{"id": "0003", "name": "Watch", "price": 6999, "is_sale": true}]}'


# json.loads()：用于将 JSON 格式的字符串解码为 Python 对象。
# python_obj = json.loads(json_str)
# print(python_obj)

# JSON 文件的写入和读取
# with open(file_path, mode, encoding) as file
# file_path：要打开的文件路径
# mode：打开文件的模式，如 r (只读)、w (写入)、a(追加) 等
# encoding(可选)：文件的编码方式，默认为 None，表示使用系统默认编码
# json.dump()：将 Python 对象序列转化为 JSON 格式并写入文件中。


import json

data = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

# 将数据写入JSON文件
with open("data.json", "w") as file:
    json.dump(json_str, file)  # 序列化，并且写入文件


# json.load：从文件中读取 JSON 格式的数据并解码为 Python 对象。
# 从JSON文件中读取数据
with open("data.json", "r") as file:
    data = json.load(file)

print(data)

new_data = json.loads(json_str)
print(new_data)
print(type(data))
print(new_data["code"])
print(new_data["message"])
print(new_data["data"][2]["name"])
