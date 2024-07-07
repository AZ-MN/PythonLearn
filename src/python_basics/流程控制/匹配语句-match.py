# 匹配语句-match
# 基础语法结构
"""
match 匹配值:
    case 匹配值1:
        处理逻辑1
    case 匹配值2:
        处理逻辑2
    ...
"""
# 示例1：HTTP网络码匹配
def match_code():
    http_code = input("请输入HTTP网络码：")
    match http_code:
        # case "101":
        #     print("切换协议")
        # case "200":
        #     print("请求成功")
        # case "305":
        #     print("使用代理")
        # case "404":
        #     print("请求资源不存在")
        # case "503":
        #     print("服务不可用")
        # case _:
        #     print("未知网络码")
# 组合多个匹配值
        case "100" | "101":
            print("切换协议")
        case "200" | "202" | "203":
            print("请求成功")
        case "300" | "305" | "306":
            print("使用代理")
        case "404" | "407" | "410":
            print("请求资源不存在")
        case "503" | "504" | "505":
            print("服务不可用")
        case _:
            print("未知网络码")

# 匹配模式绑定变量
# 示例2：输入一个坐标，输出该坐标点的范围
# point is an (x,y) tuple
def match_range():
    x = int(input("请输入x坐标："))
    y = int(input("请输入y坐标："))
    point = (x, y)
    # point = 1 # 报错，因为point是元组类型
    match point:
        case (0, 0):
            print("坐标在原点上")
        case (0, y):
            print("坐标在y轴上")
        case (x, 0):
            print("坐标在x轴上")
        case (x, y):
            print(f"X= {x}, Y= {y}")
        case c:
            # raise ValueError("坐标不在平面直角坐标系上")
            print("没有这个坐标点")

# 只能有一个变量
#     match 1:
#         case x:
#             print("XXX")
#         case _:
#             print("没有这个值")

if __name__ == '__main__':
    while True:
        # match_code()
        match_range()
