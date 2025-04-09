# 装饰器的基本使用和定义
# 用户进行账号的注册
# 原来函数定义的功能没有对账号进行验证，现在需要增加额外的功能验证账号长度符合6-12位字符
# 定义一个装饰器来完成账号长度的验证
def check_account(func):
    def wrapper(*args, **kwargs):
        account = args[0]
        if len(account) < 6 or len(account) > 12:
            print("账号长度不符合要求")
            return
        func(*args, **kwargs)

    return wrapper


def register(account):
    print("注册成功")


register = check_account(register)  # 绑定函数 register = wrapper
register("123456")  # wrapper("123456")
register("1234567890123456")
register("1234")


# 案例：去购物，没有登录之前无法进行将商品添加到购物车操作
# 正常购物流程需要先登录后添加商品到购物车，目前没有登录可以直接添加，添加登录功能之后再购物
def check_login(func):
    def wrapper(*args, **kwargs):
        is_login = args[0]
        if not is_login:
            print("请先登录")
            return
        func(*args, **kwargs)

    return wrapper


@check_login  # check_login(add_to_cart)
def add_to_cart(*args, **kwargs):
    print("成功添加商品到购物车")


add_to_cart(True)  # 使用装饰器相当于绑定了函数，相当于add_to_cart = check_login(add_to_cart) --> add_to_cart = wrapper


# add_to_cart = check_login(add_to_cart)
# add_to_cart(True)

