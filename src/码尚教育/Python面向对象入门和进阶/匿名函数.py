# 调用格式：
# 把匿名函数当做一个整体使用（）进行调用传递实参
# 有参数就需要传递实参
# 不需要使用return也有返回值

# 定义匿名函数使用lambda关键字
print((lambda x, y: x + y)(1, 2))

# 将匿名函数的引用进行传递, 并调用匿名函数
func = lambda x, y: x + y
print(func(33, 66))
print(type(func))
