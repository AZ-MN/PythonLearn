"""
多任务进程编程
简介
一个正在运行的程序或者软件就是一个进程，它是操作系统进行资源分配的基本单位，也就是说每启动一个进程，操作系统都会给其分配一定的运行资源(内存资源)保证进程的运行。

比如：现实生活中的公司可以理解成是一个进程，公司提供办公资源(电脑、办公桌椅等)，而公司下属的分公司，可以理解为子进程。

Python 中使用 multiprocessing 模块实现进程多任务编程。
"""

import multiprocessing

"""
创建进程
multiprocessing 模块使用 Process 类创建进程实例对象，实现进程任务的创建。

Process([group [, target [, name [, args [, kwargs]]]]])

参数说明：
group：指定进程组，目前只能使用 None
target：执行的目标任务名
name：进程名字
args：以元组方式给执行任务传参
kwargs：以字典方式给执行任务传参
"""

import time
import os


# 跳舞任务
# def dance():
#     for i in range(5):
#         print("跳舞中...")
#         time.sleep(0.2)
#
#
# # 唱歌任务
# def sing():
#     for i in range(5):
#         print("唱歌中...")
#         time.sleep(0.2)
#
#
# if __name__ == '__main__':
#     p1 = multiprocessing.Process(target=dance, name="myProcess1")
#     p2 = multiprocessing.Process(target=sing)
#
#     # 启动进程
#     # 进程对象创建成功后，需要启动进程才会开始执行。
#     p1.start()
#     p2.start()


# 获取当前进程
# multiprocessing.current_process() 可以获取当前进程。
# def task1():
#     for i in range(5):
#         print(multiprocessing.current_process())
#         # 获取进程名, 进程对象的name属性可以获取进程的名称。
#         print(multiprocessing.current_process().name)
#         time.sleep(0.2)
#
#
# def task2():
#     for i in range(5):
#         print(multiprocessing.current_process())
#         # 获取进程名, 进程对象的name属性可以获取进程的名称。
#         print(multiprocessing.current_process().name)
#         time.sleep(0.2)
#
#
# def task3():
#     print(f'{multiprocessing.current_process().name}_ID', os.getpid())
#     print(f'{multiprocessing.current_process().name}_Parent_ID', os.getppid())
#
#
# def task4():
#     print(f'{multiprocessing.current_process().name}_ID', os.getpid())
#     print(f'{multiprocessing.current_process().name}_Parent_ID', os.getppid())
#
#
# if __name__ == '__main__':
# 获取进程名, 进程对象的name属性可以获取进程的名称。
# print(multiprocessing.current_process().name)
# p1 = multiprocessing.Process(target=task1, name='myProcess1')
# p2 = multiprocessing.Process(target=task2)

# 获取进程ID, 每一个进程产生时，操作系统都分为进程分配一个ID编号，可以通过os模块中的方法获取进程的ID。
# os.getpid()获取当前进程ID
# os.getppid()获取当前进程的父进程的ID
# print(f'{multiprocessing.current_process().name}_ID', os.getpid())
# print(f'{multiprocessing.current_process().name}_Parent_ID', os.getppid())
# p1 = multiprocessing.Process(target=task3, name="myProcess1")
# p2 = multiprocessing.Process(target=task4)
# p1.start()
# p2.start()


# 进程任务函数传参
# 在创建进程对象的时候，为进程任务函数传递参数，可以使用两种方式为任务函数传参。
# args: 使用可变位置参数形式传参
# kwargs: 使用可变关键字参数形式传参

def task(n, msg):
    for i in range(n):
        print(multiprocessing.current_process().name, f'第{i}次打印 {msg}')
        time.sleep(0.2)


# if __name__ == '__main__':
#     # 使用可变位置参数传参
#     p1 = multiprocessing.Process(target=task, name='p1', args=(5, "Hello World"))
#     # 使用可变关键字参数传参
#     p2 = multiprocessing.Process(target=task, name='p2', kwargs={"msg": "Python", "n": 5})
# 进程同步
# join() 方法用来将子进程添加到当前进程之前执行，直到子进程执行结束后，当前进程才会继续向下执行。
# 多个进程间的代码在运行时是交替执行的，如果使用 join() 方法后，当前进程会进入到阻塞状态，等待子进程结束后，解除阻塞状态，继续执行当前进程。
# 使用 join() 方法后，可使多进程的 异步执行 变成 同步执行, 过多使用会使程序效率变低。
# p1.start()
# p1.join()
# print("main run...", p1.exitcode)
# p2.start()
# p2.join()
# print(p2.exitcode)

# 守护进程
# 多进程在执行时，父进程会等待子进程执行结束才会结束。
# 如果需要子进程在父进程执行结束后就结束执行，无论子进程是否执行完毕，可以将子进程设置为守护进程。
# 比如：只有开启企业微信后，才可以使用企业微信的会议功能，当企业微信退出时，会议也会随之退出。
# 设置守护进程方式有两种：
# 使用 子进程对象.daemon = True 在子进程启动前将子进程设置为守护进程。
# 使用 子进程对象.terminate() 在主进程退出前手动将子进程结束。

# 设置子进程为守护进程
# p1.daemon = True
# p1.start()
# p2.start()
# time.sleep(0.5)
# print("main")
# print(p1.is_alive())

# 手动杀死子进程
# p1.start()
# p2.start()
# time.sleep(0.5)
# p1.terminate()
# print("main")


# 进程间不共享全局变量
# 因为进程是程序执行的最小资源分配单位，当一个子进程被创建时，子进程会复制父进程的资源，形成一个独立的空间，所以多个进程之间的数据是独立不共享的。
# 定义全局变量
g_list = list()


# 添加数据的任务
def add_data():
    for i in range(5):
        g_list.append(i)
        print("add:", i)
        time.sleep(0.2)
    print("add_data:", g_list)


def read_data():
    print("read_data:", g_list)


if __name__ == '__main__':
    add_data_process = multiprocessing.Process(target=add_data, name='add_data_process')
    read_data_process = multiprocessing.Process(target=read_data, name='read_data_process')
    add_data_process.start()
    add_data_process.join()
    read_data_process.start()

    print("main:", g_list)
