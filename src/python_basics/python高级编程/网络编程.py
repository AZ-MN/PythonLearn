# 实现 socket 客户端
# import socket
#
# # 1.创建TCP套接字对象
# socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # 2.和服务器建立连接
# socket_client.connect(('127.0.0.1', 9999))
#
# # 3.想服务器发送数据
# send_data = "Hello World!"
# socket_client.send(send_data.encode('utf-8'))
#
# # 4.从服务器接受数据
# recv_data = socket_client.recv(1024).decode('utf-8')
# print(recv_data)
#
# # 5.关闭连接
# socket_client.close()


# 实现基于TCP的socket服务器
# import socket
#
# # 1.创建服务器套接字对象
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # 2.设置端口复用，让程序退出端口号后立即释放
# server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
#
# # 3.给服务器绑定ip地址和端口号
# server.bind(('127.0.0.1', 9999))
#
# # 4.设置服务器监听
# server.listen(128)
# print('Server listening on 127.0.0.1:9999...')
# # 等待客户端建立连接的请求，只有客户端合服务器建立连接成功，代码才会解阻塞，代码才能继续往下执行
# # 专门和客户端通信的套接字：client_socket
# # 客户端的ip地址和端口号：ip_port
# client_socket, ip_port = server.accept()
# print('Client connected...')
# # 接收客户端发送的数据, 这次接收数据的最大字节数是1024
# recv_data = client_socket.recv(1024).decode('utf-8')
# # 获取数据的长度
# recv_data_len = len(recv_data)
# print(f'Receive data is: {recv_data}')
# print(f'Receive data len: {recv_data_len}')
#
# # 5.发送数据
# send_data = f'你好,{ip_port[0]}:{ip_port[1]}'.encode('utf-8')
# client_socket.send(send_data)
#
# # 关闭服务与客户端的套接字，终止和客户端通信的服务
# client_socket.close()
# # 关闭服务器的套接字，终止和客户端提供建立连接请求的服务
# server.close()


# 实现多任务TCP服务器
import socket
import threading


class MultiTaskTCPServer(object):
    # 在初始化方法中对服务器socket进行初始化操作
    def __init__(self, ip="", port=8888):
        try:
            # 创建tcp服务器套接字
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # 设置端口号复用，让程序退出端口号立刻释放
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # 绑定ip和port
            self.server.bind((ip, port))
            # 设置监听，listen后的套接字是被动套接字，只负责接收客户端的连接请求
            self.server.listen(128)
            # 设置服务器已启动状态
            print("服务器等待连接...")
        except Exception as e:
            print(f"服务器初始化失败: {e}")
            raise

    # 启动服务器方法，实现多任务接收处理客户端连接请求
    def run(self):
        # 循环等待接收客户端的连接请求
        while True:
            try:
                client, address = self.server.accept()
                print("客户端连接成功", "client: ", client, "address: ", address)
                # 当客户端和服务器成功建立连接以后，需要创建一个子线程，不同子线程负责接收不同客户端的消息
                sub_thread = threading.Thread(target=self.handle_client_request, args=(client, address))
                # 设置守护主线程
                sub_thread.setDaemon(True)
                # 启动子线程
                sub_thread.start()
            except Exception as e:
                print(f"接收客户端连接时发生错误：{e}")

    # 处理客户端的请求操作
    @staticmethod
    def handle_client_request(client, address):
        try:
            recv_data = client.recv(1024).decode('utf-8')
            if not recv_data:
                print(f"客户端下线了：{address}")
                return

            print(f'已接收到客户端 {client} 数据：{recv_data} 字节长度：{len(recv_data)}')

            send_data = "Connect Succeed!!!".upper().encode('utf-8')
            client.send(send_data)
        except ConnectionResetError as e:
            print(f"客户端连接重置：{e}")
        except Exception as e:
            print(f"处理客户端请求时发生错误：{e}")
        finally:
            client.close()


if __name__ == '__main__':
    # 创建服务器对象
    server = MultiTaskTCPServer()
    # 启动服务器
    server.run()
