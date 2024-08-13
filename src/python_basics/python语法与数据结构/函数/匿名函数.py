""""
匿名函数

匿名函数是指没有名字的函数，应用在需要一个函数，但是又不想费神去命名这个函数的场合。

在通常情况下，这样的函数只使用一次。

在 Python 中使用 lambda 表达式创建匿名函数:
 lambda 表达式可用于任何需要函数对象的地方。
 在语法上，匿名函数只能是单个表达式。
 在语义上，它只是常规函数定义的语法糖。
 lambda 表达式中不能使用 if、for-in、while、return 等语句, 但可以使用三目运算符

lambda 表达式格式：
 result = lambda [arg1 [, arg2, .... , argn]]: expression
 result：用于保存 lambda 表达式的引用
 [arg1 [, arg2, .... , argn]]:：可选，指定要传递的参数列表，多个参数间使用英文的逗号 ， 进行分隔。
 expression：必选，指定一个实现具体功能的表达式。如果有参数，那么在该表达式中将应用这些参数。
"""

# 示例：
# def add(n1, n2):
#     return n1 + n2
#
#
# result = add(1, 2)
# print(result)
#
# add = lambda x, y: x + y
# result = add(2, 3)
# print(result)
#
# func = lambda x: x ** 2 if x > 3 else x ** 3
# print(func(3))


# 待排序的数据
# students = [
#     {'name': 'Alice', 'id': '1001', 'class': 'Class1'},
#     {'name': 'Eve', 'id': '1005', 'class': 'Class2'},
#     {'name': 'Charlie', 'id': '1003', 'class': 'Class1'},
#     {'name': 'David', 'id': '1004', 'class': 'Class2'},
#     {'name': 'Bob', 'id': '1002', 'class': 'Class1'},
#     {'name': 'Frank', 'id': '1006', 'class': 'Class2'}
# ]
# TypeError: '<' not supported between instances of 'dict' and 'dict'
# students.sort()

# 以名字排序
# students.sort(key=lambda stu: stu["name"])
# for s in students:
#     print(s)
#
# 以ID降序排序
# students.sort(key=lambda stu: stu["id"], reverse=True)
# for s in students:
#     print(s)

# sorted函数排序
# newData = sorted(students, key=lambda stu: stu['name'], reverse=True)
# for student in newData:
#     print(student)

# nums = [7, 2, 3, 10, 5, 6, 1, 8, 9, 4]
# nums.sort(reverse=True)
# print(nums)

# strings = ['c', 'f', 'a', 'd', 'e', 'z', 'g', 'h', 'q', 'j']
# strings.sort()
# print(strings)

# 待排序的数据
students = [
    {'name': 'Alice', 'id': '1001', 'class': 'Class1'},
    {'name': 'Eve', 'id': '1005', 'class': 'Class2'},
    {'name': 'Charlie', 'id': '1003', 'class': 'Class1'},
    {'name': 'David', 'id': '1004', 'class': 'Class2'},
    {'name': 'Bob', 'id': '1002', 'class': 'Class1'},
    {'name': 'Frank', 'id': '1006', 'class': 'Class2'}
]

nums = [7, 2, 3, 10, 5, 6, 1, 8, 9, 4]

strings = ['c', 'f', 'a', 'd', 'e', 'z', 'g', 'h', 'q', 'j']


# sorted() 函数实现
def mySorted(obj, key=None, reverse=False):
    # 先定义一个空列表，用来保存排序后的结果，并返回
    newData = []
    # 遍历传入的数据
    for i in obj:
        for j in newData:
            # 判断调用者，是否传入排序的规则，如果有，就使用规则，没有就使用默认比较方式
            if key:
                if key(i) < key(j):
                    index = newData.index(j)
                    newData.insert(index, i)
                    break
            else:
                if i < j:
                    index = newData.index(j)
                    newData.insert(index, i)
                    break
        else:
            newData.append(i)
    # 想要实现逆序效果，使用切片将返回数据处理一下就可以了
    return newData[::-1] if reverse else newData


# result = sorted(nums)
# result = mySorted(nums)
# result = sorted(strings)
# result = mySorted(strings)
# result = sorted(students, key=lambda x: x["name"])
result = mySorted(students, key=lambda x: x["name"], reverse=True)

for r in result:
    print(r)
