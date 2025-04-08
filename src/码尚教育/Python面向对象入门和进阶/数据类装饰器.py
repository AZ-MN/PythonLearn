import dataclasses


@dataclasses.dataclass
class Girl:
    # 定义数据类的实例属性必须指定数据类型
    name: str
    age: int
    is_single: bool

    def show(self):
        print(f"个人身份信息: \n 姓名: {self.name} \n 年龄: {self.age} \n 是否单身: {self.is_single}")


g = Girl("刘亦菲", 18, False)
g.show()
print(type(g.age))

