'''
多任务协程编程
简介
协程，又称微线程，纤程。英文名 Coroutine。

协程也是一种轻量级的多任务编程技术，它可以在同一个线程中实现多个任务的切换和调度。

协程通过任务的暂停和恢复，避免了线程切换的开销并减少了锁的使用。协程常用于异步编程场景，比如网络编程和IO密集型任务。

最大的优势就是协程极高的执行效率。因为函数切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。

第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。

比如：一个人在打印资料的等待过程中，又去接听了客户的电话，在接听电话的等待过程中，又整理了桌面。
'''

# Python 中可以使用第三方模块 gevent 实现进程多任务编程。
# 前提：pip install gevent
from gevent import monkey

monkey.patch_all()

import gevent
import random


# 创建协程
# gevent 模块使用 spawn 类创建协程实例对象，实现协程任务的创建。
# spawn(run [, args [, kwargs]])
# 参数说明：
# run：执行的目标任务名
# args：以元组方式给执行任务传参
# kwargs：以字典方式给执行任务传参


def task1():
    for i in range(1, 11):
        print(f'第 {i} 次 Run')


# 创建协程对象
def create_task1():
    g1 = gevent.spawn(task1)
    g2 = gevent.spawn(task1)
    g3 = gevent.spawn(task1)
    g1.join()
    g2.join()
    g3.join()


# 启动进程
# 协程对象创建成功后，需要使用 join() 方法启动协程才会开始执行。
# 该方法的作用是对当前线程进行阻塞，直到协程执行结束后，继续执行当前线程。
# if __name__ == '__main__':
#     create_task1()


# # 获取当前协程对象
# # gevent.getcurrent() 可以获取当前协程对象。
def task2():
    for i in range(1, 11):
        print(f'{gevent.getcurrent()} 第 {i} 次 Star')


def create_task2():
    g1 = gevent.spawn(task2)
    g2 = gevent.spawn(task2)
    g3 = gevent.spawn(task2)
    g1.join()
    g2.join()
    g3.join()


# if __name__ == '__main__':
#     create_task2()


# 协程组
# 在创建多个协程对象后，可以将多个协程对象放入一个元组或列表中，然后使用 gevent.joinall() 方法同时启动协程对象。
def task3():
    for i in range(1, 6):
        print(gevent.getcurrent(), i)


# 使用列表推导式，生成一个有5个协程对象的列表
def create_task3():
    gs = [gevent.spawn(task3) for i in range(3)]
    print(gs)  # [<Greenlet at 0x221ceb8acc0: task3>, <Greenlet at 0x221cec840e0: task3>, <Greenlet at 0x221cec84c20:
    # task3>]
    gevent.joinall(gs)


# if __name__ == '__main__':
#     create_task3()

# 协程切换
# 从前面的代码执行结果看，虽然可以执行多个协程任务，但是任务的执行过程依然是同步的。
# 可以通过在代码中添加 gevent.sleep() 方法模拟耗时操作，实现协程任务的切换。
# 注意： sleep() 方法是 gevent 模块中的，不是 time 模块中的。
def task4():
    for i in range(1, 6):
        print(gevent.getcurrent(), i)
        gevent.sleep(0.1)


# 使用列表推导式，生成一个有5个协程对象的列表
def create_task4():
    gs = [gevent.spawn(task4) for j in range(5)]
    gevent.joinall(gs)


# if __name__ == '__main__':
#     create_task4()


# 协程任务函数传参
# 在创建协程对象的时候，为协程任务函数传递参数，可以使用两种方式为任务函数传参。
# args: 使用可变位置参数形式传参
# kwargs: 使用可变关键字参数形式传参
# 协程的任务函数传参与进程和线程不同，协程可以和直接使用函数一样，在 spawn 方法中为任务函数传参。
def task5(n, msg):
    for i in range(1, n + 1):
        print(gevent.getcurrent(), f"第 {i} 次输出 {msg}")
        gevent.sleep(0.01)


def create_task5():
    g1 = gevent.spawn(task5, 5, "Python")
    g2 = gevent.spawn(task5, msg="Hogwarts", n=5)
    # g3 = gevent.spawn(task5, args=(5, "Hello"))  # 使用args传参，在这会报错，正常应该直接在逗号后面跟参数（即g1）
    g1.join()
    g2.join()
    # g3.join()


# if __name__ == '__main__':
#     create_task5()


# 协程异步 # 在 Python 中，Gevent 的 monkey patch 是指使用 Gevent 的模块 gevent.monkey 中的 patch_all() 等方法，来替换标准库中的一些阻塞式 I/O
# 操作，以实现非阻塞式的协程 I/O。
# 一般该方法写在程序的第一行。
def task6(n, msg):
    for i in range(1, n + 1):
        print(gevent.getcurrent(), f"第 {i} 次输出 {msg}")
        gevent.sleep(random.random())


def create_task6():
    g1 = gevent.spawn(task6, 5, "Python")
    g2 = gevent.spawn(task6, msg="Hogwarts", n=5)
    g3 = gevent.spawn(task6, n=5, msg="Hello")
    gevent.joinall((g1, g2, g3))


if __name__ == '__main__':
    create_task6()


# 在 Python3.10 版本中，Gevent 的 monkey patch 功能在某些情况下可能无效。
# 这是因为在 Python3.10 中引入了 asyncio 的新的事件循环机制，与 Gevent 的事件循环有所不同，导致 monkey patch 在有些情况下失效。
# Gevent 官方还没有正式发布兼容 Python3.10 版本的版本，因此在 Python3.10 中使用 monkey.patch_all() 方法可能无法正常实现非阻塞的协程 I/O。
# 为了解决这个问题，你可以考虑使用 Python3.10 引入的 asyncio 模块来进行异步编程。
# asyncio 提供了原生的协程和事件循环，可以实现高效的异步操作。
