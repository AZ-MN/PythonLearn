class Student(object):
    # 实现构造方法-用来在创建对象时，进行绑定对象的属性
    def __init__(self, name):
        self.name = name
        self.course = []

    # 实例方法-选课
    def select_course(self, c_name):
        self.course.append(c_name)

    # 实例方法-显示所有选择课程
    def show_course_list(self):
        print(f"{self.name}选课如下：")
        for c in self.course:
            print(c, end="、")

    # 对象描述方法
    def __str__(self):
        s = f"{self.name}选课如下：\n"
        c = "、".join(self.course)
        s += c
        return s


if __name__ == '__main__':
    Tom = Student('Tom')
    Rose = Student('Rose')

    Tom.select_course('Python')
    Tom.select_course('C++')
    Tom.select_course('Java')

    # Tom.show_course_list()

    print(Tom)
