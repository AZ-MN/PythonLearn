"""
datetime 模块
简介
datetime 是 Python 标准库中用于处理日期和时间的模块。
它提供了多种类和函数，用于处理日期、时间、时间间隔等操作，使得日期和时间的处理更加方便和灵活。

应用场景
作为日志信息的内容输出
计算某个功能的执行时间
用日期命名一个日志文件的名称
生成随机数（时间是不会重复的）
"""

from datetime import datetime, timedelta

# 获取当前日期时间
# current_datetime = datetime.now()
# print(current_datetime)
# print(type(current_datetime))
#
# # 格式化日期和时间
# result = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
# print(result)
# result = current_datetime.strftime('%Y-%m-%d')
# print(result)
# result = current_datetime.strftime('%H:%M:%S')
# print(result)
# result = current_datetime.strftime('%Y/%m/%d')
# print(result)
# result = current_datetime.strftime('%Y年%m月%d日')
# print(result)
#
# # 解析日期和时间
# # 使用 strptime() 函数可以将字符串解析为 datetime 对象
# date = "2023-08-08 15:30:00"
# date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
# print(date)
# print(type(date))

# 计算日期间隔
# 使用 timedelta 类可以进行日期间隔的计算
# date1 = datetime(2020, 1, 1)
# date2 = datetime(2023, 7, 7)
# date_diff = date2 - date1
# print("Date Difference:", date_diff)
#
# current_datetime = datetime.now()
# # 使用 timedelta 计算未来的日期
# future_date = current_datetime + timedelta(days=30)
# print("Future Date:", future_date)

# 比较日期
# 可以直接比较 datetime 对象来判断日期的先后关系。
# date1 = datetime(2024, 1, 1)
# date2 = datetime(2024, 3, 22)
# if date1 < date2:
#     print("date1 is earlier than date2")
# elif date1 > date2:
#     print("date1 is later than date2")
# else:
#     print("date1 and date2 are the same")

# 获取日期和时间的部分信息
# 可以使用 year 、month 、day、hour 、minute 、 second 等属性获取日期和时间的部分信息。
date = datetime.now()
print(date)
year = date.year
month = date.month
day = date.day
hour = date.hour
minute = date.minute
second = date.second
print(f'year: {year}, month: {month}, day: {day}')
print(f'hour: {hour}, minute: {minute}, second: {second}')