"""
多任务线程编程
简介
线程是指在一个程序中执行的一段指令流。
在操作系统中，线程是调度执行的最小单位，它可以独立运行，并共享线程的资源，如内存空间、文件句柄等。

线程有以下几个特点：
轻量级：相对于进程来说，线程的创建、切换和销毁的开销较小。
共享资源：线程可以共享线程的资源，包括内存空间、文件句柄等。这使得线程之间可以方便地进行数据共享和通信。
并发执行：线程可以并发执行，即多个线程可以在同一时间内执行不同的任务。线程的并发执行可以提高程序的性能和响应性。
线程安全：线程安全是指多个线程同时访问共享数据时，不会出现数据不一致或异常的情况。在多线程编程中，需要采取一些措施（如锁、互斥量等）来保证线程安全性。
线程必须依附于进程中，线程不能单独存在。

比如:现实生活中的公司可以理解成是一个进程，公司提供办公资源(电脑、办公桌椅等)，真正干活的是员工，员工可以理解成线程。
"""
# Python 中使用 threading 模块实现线程多任务编程。

# 创建线程
# threading 模块使用 Thread 类创建线程实例对象，实现线程任务的创建
# Thread([group [, target [, name [, args [, kwargs [, daemon]]]]]])

# 参数说明：
# group：指定线程组，目前只能使用 None
# target：执行的目标任务名
# name：线程名字
# args：以元组方式给执行任务传参
# kwargs：以字典方式给执行任务传参
# daemon：设置线程对象为守护线程

import threading
import time


# def task1():
#     while True:
#         print("跳舞中...")
#         time.sleep(1)
#
#
# def task2():
#     while True:
#         print("唱歌中...")
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=task1, name='task1')
#     t2 = threading.Thread(target=task2)
#     # 启动线程
#     t1.start()
#     t2.start()


# 获取当前线程，threading.current_thread() 可以获取当前线程
# def task1():
#     for i in range(5):
#         print(threading.current_thread())
#         time.sleep(1)
#
#
# def task2():
#     for i in range(5):
#         print(threading.current_thread())
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=task1, name='myThread1')
#     t2 = threading.Thread(target=task2)
#     t1.start()
#     t2.start()


# 获取线程名，threading.current_thread().name 可以获取线程名
# def task1():
#     for i in range(5):
#         print(threading.current_thread().name)
#         time.sleep(1)
#
#
# def task2():
#     for i in range(5):
#         print(threading.current_thread().name)
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=task1, name='myThread1')
#     t2 = threading.Thread(target=task2)
#     t1.start()
#     t2.start()


# 线程无序性
# 线程执行时是无序的。它是由 CPU 调度决定的 ，CPU 调度哪个线程，哪个线程就先执行，没有调度的线程不能执行。
# def task():
#     for i in range(5):
#         time.sleep(1)
#         print("当前线程：", threading.current_thread())
#
#
# if __name__ == '__main__':
#     for _ in range(5):
#         t1 = threading.Thread(target=task, name='myThread')
#         t1.start()


# 线程任务函数传参
# 在创建线程任务时，可以通过 args 和 kwargs 参数传递参数给任务函数。
# def task(n, msg):
#     for i in range(n):
#         print("第", i, "次打印：", msg)
#         time.sleep(1)
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=task, args=(5, "hello"), name='myThread')
#     t2 = threading.Thread(target=task, kwargs={'n': 5, 'msg': 'world'}, name='myThread2')
#     t1.start()
#     t2.start()


# 线程同步
# join() 方法用来将子线程添加到当前线程之前执行，直到子线程执行结束后，当前线程才会继续向下执行。
# 多个线程间的代码在运行时是交替执行的，如果使用 join() 方法后，当前线程会进入到阻塞状态，等待子线程结束后，解除阻塞状态，继续执行当前线程。
# 使用 join() 方法后，可使多线程的异步执行变成同步执行, 过多使用会使程序效率变低。
# def task(n, msg):
#     for i in range(n):
#         print(threading.current_thread().name, "第", i, "次打印：", msg)
#         time.sleep(0.2)
#
#
# if __name__ == '__main__':
#     # 使用可变位置参数传参
#     t1 = threading.Thread(target=task, args=(5, "hello"), name='myThread')
#     # 使用可变关键字参数传参
#     t2 = threading.Thread(target=task, kwargs={'n': 5, 'msg': 'world'})
#     t3 = threading.Thread(target=task, kwargs={'msg': 'test', 'n': 5})
#     t1.start()
#     t1.join()
#     print("主线程 running")
#     t2.start()
#     t2.join()
#     t3.start()


# 守护线程
# 多线程在执行时，父线程会等待子线程执行结束才会结束。
# 如果需要子线程在父线程执行结束后就结束执行，无论子线程是否执行完毕，可以将子线程设置为守护线程。
#
# 比如：在使用下载软件进行下载多个视频时，每个下载任务都是一个线程，如果下载软件退出，则下载任务也会停止并退出。
#
# 设置守护线程方式有两种：
# 使用 daemon = True 参数在子线程对象创建时将子线程设置为守护线程。
# 使用 子线程对象.daemon = True 属性在子线程对象启动前将子线程对象设置为守护线程。
# 设置子线程为守护线程，主线程退出，子线程也会随之退出。
# def task(n, msg):
#     for i in range(n):
#         print(threading.current_thread().name, "第", i+1, "次打印：", msg)
#         time.sleep(0.5)
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=task, args=(5, "hello"), daemon=True)
#     t2 = threading.Thread(target=task, kwargs={'n': 5, 'msg': 'world'})
#     t2.daemon = True
#     t1.start()
#     t2.start()
#     time.sleep(1)
#     print("主线程 running")


# 线程间共享全局变量
# 线程间共享全局变量，即所有线程都可以访问该变量，并且对该变量的修改会影响其他线程。
# 这种情况一般用于线程间通信，例如：一个线程负责写入数据，另一个线程负责读取数据。

# 定义全局变量
# g_list = list()


# 添加数据的任务
# def add_data():
#     for i in range(5):
#         g_list.append(i)
#         print("添加数据：", i)
#         time.sleep(1)
#
#     print("添加数据完成:", g_list)
#
#
# def read_data():
#     print("读取数据：", g_list)
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=add_data)
#     t2 = threading.Thread(target=read_data)
#     t1.start()
#     t1.join()
#     t2.start()
#
#     print("主线程:", g_list)


# 线程安全问题
# 线程安全问题是指多个线程同时操作同一资源时，不会出现数据混乱或错误的问题。
# 线程安全问题通常出现在多线程环境下，如网络编程、文件操作等。

# 注意
# 线程安全问题并不是绝对的，只是相对来说比较容易发生。
# 解决线程安全问题的办法就是在操作共享资源时加锁，保证只有一个线程能操作该资源，从而避免了冲突。
# 加锁的方式有多种，最简单的就是使用互斥锁，即 Lock 类。
# Python 3.9 版本解释器之前，线程安全问题非常明显
# Python 3.10 版本后，引入了新的 GIL2.0 版本的锁，有效的提升了线程安全问题，但某些时刻还需要使用互斥锁保证线程安全。

# 示例： 使用多个线程对象，分别对共享全局变量 sum 做一百万次加 1 操作，查看计算结果。
# 定义全局变量
# sum = 0
#
#
# # 循环一次给全局变量加 1
# def add_one():
#     global sum
#     for i in range(1000000):
#         sum += 1
#
#     print(threading.current_thread().name, ":", sum)
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=add_one)
#     t2 = threading.Thread(target=add_one)
#     t3 = threading.Thread(target=add_one)
#     t1.start()
#     t2.start()
#     t3.start()
#     time.sleep(3)
#     print(threading.current_thread().name, " : ", sum)

"""
错误分析:
多个线程线程对象 t1，t2，t3 都要对全局变量 sum （默认是0）进行加 1 运算，但是由于是多线程同时操作，有可能出现下面情况：
- 在 sum=0 时，线程对象 t1 取得 sum=0。
- 此时系统把线程对象 t1 调度为 sleeping 状态
- 把线程对象 t2 转换为 running 状态，t2 也获得 sum=0
- 然后线程对象 t2 对得到的值进行加 1 并赋给 sum，使得 sum=1
- 然后系统又把线程对象 t2 调度为 sleeping
- 再把线程对象 t1 转为 running 状态
- 线程对象 t1 又把它之前得到的 0 加 1 后赋值给 sum，结果为 sum=1
- 三个线程对象都会在执行过程中出现这种情况
- 这样导致虽然线程对象 t1，t2，t3 都对 sum 加 1，但结果却是产生了无效的计算过程
"""

# 互斥锁
# 在 Python 中，可以使用互斥锁（Mutex）来保护共享资源，避免多个线程同时对共享资源进行写操作，从而避免竞争条件和数据不一致的问题。
# 使用 threading.Lock() 获取互斥锁对象。
# lock = threading.Lock()
# 互斥锁操作：
# 加锁操作： lock.acquire()
# 解锁操作： lock.release()
# 使用互斥锁解决 Python3.9 版本线程间数据安全问题。

# 定义全局变量
# sum = 0
#
# lock = threading.Lock()
#
#
# # 方式一
# def add_one():
#     global sum
#     # 只需要加、解锁三次
#     lock.acquire()
#     for i in range(1000000):
#         sum += 1
#     lock.release()
#     print(threading.current_thread().name , " : ", sum)

# 方式二
# def add_one():
#     global sum
#     for i in range(1000000):
#         # 此方法对比上面的方法，要加锁、解锁三百万次，上面方法只用加锁、解锁一次，造成资源浪费、性能差
#         lock.acquire()
#         sum += 1
#         lock.release()
#     print(threading.current_thread().name, " : ", sum)


# if __name__ == '__main__':
#     # 创建两个线程
#     t1 = threading.Thread(target=add_one)
#     t2 = threading.Thread(target=add_one)
#     t3 = threading.Thread(target=add_one)
#
#     # 启动线程
#     t1.start()
#     t2.start()
#     t3.start()
#     time.sleep(5)
#     print(threading.current_thread().name, " : ", sum)


# 死锁
# 虽然使用互斥锁可以解决线程间数据安全问题，但是，如果互斥锁使用不当，会出现死锁现象。
# 死锁是指一个线程获取锁权限后，并未释放锁，导致其它线程无法获取互斥锁的使用权，持续进行等待的过程。

# 创建互斥锁
# lock = threading.Lock()
#
# numbers = [3, 6, 8, 1, 9]
#
#
# # 根据下标去取值，保证同一时刻只能有一个线程去取值
# def get_value(index):
#     # 上锁
#     lock.acquire()
#     # 判断下标是否越界
#     if index >= len(numbers):
#         print(threading.current_thread().name, f"下标 {index} 越界")
#         # 如果下标越界，会直接return跳出函数，不释放锁，造成死锁
#         return
#     value = numbers[index]
#     print(threading.current_thread().name, "取值为：", value)
#
#     time.sleep(2)
#     # 释放锁
#     lock.release()
#
#
# if __name__ == '__main__':
#     # 模拟大量线程执行取值操作
#     for i in range(10):
#         sub_thread = threading.Thread(target=get_value, args=(i,))
#         sub_thread.start()


# 避免死锁
# 程序开发过程中，应该避免死锁的发生。
# 可以在程序的合适位置，将锁释放掉，让其它线程对象有能获取到互斥锁的机会。

# 创建互斥锁
lock = threading.Lock()

numbers = [3, 6, 8, 1, 9]


# 根据下标去取值，保证同一时刻只能有一个线程去取值
def get_value(index):
    # 上锁
    lock.acquire()
    # 判断下标是否越界
    if index >= len(numbers):
        print(threading.current_thread().name, f"下标 {index} 越界")
        # 现在可以判断，如果越界也释放锁，就可以避免死锁
        lock.release()
        return
    value = numbers[index]
    print(threading.current_thread().name, "取值为：", value)

    time.sleep(2)
    # 释放锁
    lock.release()


if __name__ == '__main__':
    # 模拟大量线程执行取值操作
    for i in range(10):
        sub_thread = threading.Thread(target=get_value, args=(i,))
        sub_thread.start()


"""
进程与线程对比
1.关系对比
 线程是依附在进程里面的，没有进程就没有线程。
 一个进程默认提供一条线程，进程可以创建多个线程。
 
2.区别对比
 进程之间不共享全局变量
 线程之间共享全局变量，但是要注意资源竞争的问题，解决办法: 互斥锁或者线程同步
 创建进程的资源开销要比创建线程的资源开销要大
 进程是操作系统资源分配的基本单位，线程是CPU调度的基本单位
 线程不能够独立执行，必须依存在进程中
 多进程开发比单进程多线程开发稳定性要强
 
3.优缺点对比
 进程优缺点: - 优点：可以用多核 - 缺点：资源开销大
 线程优缺点: - 优点：资源开销小 - 缺点：不能使用多核（3.10版本后有改善）
"""

