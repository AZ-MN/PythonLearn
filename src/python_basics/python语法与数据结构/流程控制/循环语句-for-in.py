# 循环语句 for in


# 遍历字符串
def loop_for_in_str(s):
    for i in s:
        print(i, "-->", ord(i))


# 遍历元组
def loop_for_in_tuple(t):
    for n in t:
        print(n, "-->", n ** 2)


# 遍历列表
def loop_for_in_list(l):
    for i in l:
        print(i, "-->", i.upper())


# 遍历字典
def loop_for_in_set():
    request_methods = {
        "get": "用于获取服务器上的资源，通过在URL中传递参数来发送请求。",
        "post": "用于向服务器提交数据-般用于创建新的资源或进行修改操作。",
        "put": "用于更新服务器上的资源，一般用于修改已存在的资源的全部内容。",
        "delete": "用于删除服务器上的资源。"
    }
    # 默认遍历方法
    # for methods in request_methods.keys():
    #     print(methods, "-->", request_methods[methods])

    # 获取字典中的key进行遍历
    # for k in request_methods.keys():
    #     print(k, "-->", request_methods[k])

    # 获取字典中的value进行遍历
    # for v in request_methods.values():
    #     print(v)

    # 获取字典中所有的键值对
    # for item in request_methods.items():
    #     print(item)

    # for item in request_methods.items():
    #     print(item[0], ":", item[1])

    for k, v in request_methods.items():
        print(k, "-->", v)


if __name__ == '__main__':
    # loop_for_in_str('Hogwarts!')
    # loop_for_in_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9))
    # loop_for_in_list(["get", "post", "put", "delete", "patch", "header"])
    loop_for_in_set()
