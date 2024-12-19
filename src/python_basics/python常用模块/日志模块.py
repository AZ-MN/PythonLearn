"""
日志模块
简介
日志是用于记录应用程序运行时的信息，通过日志可以帮助开发者诊断问题，跟踪应用程序的状态以及记录重要的事件。
Python 中可以使用 logging 模块 实现日志的记录。
logging 模块提供了丰富的配置选项和灵活性，可以将日志信息输出到不同的位置，设置不同的日志级别等。

logging模块的四大组件
logger：日志器，提供程序可使用的接口。
handler：处理器，用于写入日志文件并输出到指定位置，如文件、控制台或网络等。
filter：过滤器，用于输出符合指定条件的日志记录。
formatter：格式器，决定日志记录的输出格式。

日志等级
级别	        用法
DEBUG	    最低级别的日志，用于调试和记录详细信息，通常用于开发和调试阶段
INFO	    信息性信息，用于调试和记录详细信息，通常用于开发和调试阶段,确认程序按预期运行。
WARNING	    表示警告，用于指示应用程序已经或即将发生的意外（例如：磁盘空间不足）。程序仍按预期进行。
ERROR	    表示错误，由于严重的问题，程序的某些功能已经不能正常执行
CRITICAL	最高级别的日志，表示严重错误，表明程序已不能继续执行
"""

"""
logging.basicConfig() 函数
logging.basicConfig() 是Python中提供一个用来配置日志管理的函数。

格式说明：logging.basicConfig(filename, filemode, format, level)
filename：指定将日志记录到文件中，如果不指定，则默认将日志输出到控制台。
filemode：指定文件打开模式，默认为'a'（追加模式）。
format：指定日志记录的格式。
level：指定记录的最低级别，默认为logging.WARNING。

format格式说明:
%(asctime)s 打印日志的时间
%(filename)s 打印当前模块名
%(lineno)s 打印日志当前的行号
%(levelname)s 打印日志级别名称
%(message)s 打印日志信息
"""


# 导入日志模块
import logging

# 设置日志输出格式
fmt = "%(asctime)s - %(filename)s [line:%(lineno)d] - %(levelname)s - %(message)s"
# 配置日志
logging.basicConfig(filename="myLog.log", filemode="a", format=fmt, level=logging.NOTSET, encoding="utf-8")
# 调用日志器触发日志信息
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
