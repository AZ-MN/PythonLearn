"""
多态
简介
多态是面向对象编程中三大概念之三，它允许不同的对象对同一个消息作出不同的响应。
简单来说，多态是指同一个方法或操作符在不同的对象实例上可以有不同的行为。这意味着可以通过一个共同的接口或基类引用不同的子类对象，并根据实际的对象类型来调用相应的方法。

多态性在实际应用中提供了很多好处，包括：
简化代码：通过以相同的方式处理不同的对象，并使用统一的接口进行编程，可以降低代码的复杂性和重复性。
可维护性：多态可以提高代码的可维护性。当需要新增一种子类时，不需要修改已有的代码，只需要创建一个新的子类并继承父类，就能够在原有的代码基础上实现新的功能。
扩展性：由于多态允许在不修改已有的代码的情况下新增功能，因此可以更容易地对系统进行扩展和适应需求的变化。

多态性的实现通常通过继承和方法重写来实现。在继承关系中，子类可以重写父类的方法，在父类引用子类对象时，调用的实际上是子类重写后的方法。
"""

# 中医
# class Father:
#     def cure(self):
#         print("使用中医方法进行治疗。。。")
#
#
# # 西医
# class Son(Father):
#     def cure(self):
#         print("使用西医方法进行治疗。。。")
#
#
# class Teacher:
#     def teach(self):
#         print("特级地理教师")
#
#
# # 患者
# class Patient:
#     def needDoctor(self, doctor):
#         doctor.cure()
#
#
# if __name__ == '__main__':
#     oldDoctor = Father()
#     littleDoctor = Son()
#
#     # teacher = Teacher()
#
#     patient = Patient()
#
#     patient.needDoctor(oldDoctor)
#     patient.needDoctor(littleDoctor)
#     # patient.needDoctor(teacher)


"""
鸭子类型
鸭子类型（Duck Typing）是一种动态类型的概念，它源自于 走路像鸭子、叫声像鸭子、看起来像鸭子，那么它就是鸭子 的观念。
在鸭子类型中，一个对象的适用性不是由它的类或接口决定，而是由它的方法和属性是否与所需的方法和属性匹配来决定。换句话说，只要一个对象具有特定方法和属性，我们就可以将其视为具有相同类型。
举个例子，如果我们需要一个能 叫 的对象，并且某个对象有一个名为 quack() 的方法，那么我们可以将该对象视为一个 鸭子，不管它实际上是什么类的对象。
换句话说，我们关注的是对象的行为而不是其类型。
鸭子类型在动态语言中特别常见，比如 Python。在 Python 中，不需要显式地继承或实现接口，只要一个对象具有必需的方法和属性，它就可以被认为是某种类型。这使得 Python 具有灵活性和简洁性，可以更自由地处理不同类型的对象。
"""


# 中医
class Father:
    def cure(self):
        print("使用中医方法进行治疗。。。")


# 西医
class Son(Father):
    def cure(self):
        print("使用西医方法进行治疗。。。")


# 兽医
class AnimalDoctor:
    def cure(self):
        print("使用兽医方法进行治疗。。。")


# 教师
class Teacher:
    def teach(self):
        print("优秀特级教师")

    def cure(self):
        print("使用自己重病十年经验治疗")


# 患者
class Patient:
    # 使用判断实例的 isinstance() 方法判断 obj 对象是否是 Type 指定类型或其父类类型的实例
    # def needDoctor(self, doctor):
    #     if isinstance(doctor, Father):
    #         doctor.cure()
    #     else:
    #         print("此医生的治疗方法不适合我")

    # 使用 issubclass() 方法来检查类的继承关系
    def needDoctor(self, doctor):
        if issubclass(doctor.__class__, Father):
            doctor.cure()
        else:
            print("此大夫医疗方法不适用病人。。。")


#
#

# 鸭子类型通常是动态语言的特性，相比于静态类型语言，它在编译时没有类型检查。
# 这意味着无法在编译阶段对类型不匹配或缺失方法和属性进行检测，可能会导致运行时错误。


# 类型检查
# Python 中提供了 isinstance() 和 issubclass() 两个函数，用来对数据进行检查判断。
# isinstance()
# Python 中使用 isinstance() 来检查一个实例的类型
# 格式： isinstance(obj, type)
# 判断 obj 对象是否是 Type 指定类型或其父类类型的实例。


if __name__ == '__main__':
    oldDoctor = Father()
    littleDoctor = Son()
    animalDoctor = AnimalDoctor()
    teacher = Teacher()

    patient = Patient()

    patient.needDoctor(oldDoctor)
    patient.needDoctor(littleDoctor)
    patient.needDoctor(animalDoctor)
    patient.needDoctor(teacher)

    print(isinstance(littleDoctor, Father))
    print(isinstance(littleDoctor, Son))
    print(isinstance(littleDoctor, AnimalDoctor))
    print(isinstance(littleDoctor, Teacher))

    print("*" * 20)

    print(issubclass(Father, Father))
    print(issubclass(Son, Father))
    print(issubclass(AnimalDoctor, Father))
    print(issubclass(Teacher, Father))


    print("*" * 20)

    # __class__ 是一个魔法属性，用来获取当前实例对象的类
    print(oldDoctor.__class__)
    print(littleDoctor.__class__)
    print(animalDoctor.__class__)
    print(teacher.__class__)