# 多态是在继承的基础上才有会具体的表现
class Animal:
    def speak(self):
        pass


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Duck(Animal):
    def speak(self):
        print("嘎嘎嘎")


# 定义一个函数调用通过不同的对象，speak方法
def animal_speak(animal):
    # 当对象不一样的时候调用的方法也会不一样
    animal.speak()


# 创建狗和猫对象
cat = Cat()
dog = Dog()
duck = Duck()
animal_speak(cat)
animal_speak(dog)
animal_speak(duck)
