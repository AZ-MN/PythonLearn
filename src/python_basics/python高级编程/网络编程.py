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
import socket

# 1.创建服务器套接字对象
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.设置端口复用，让程序退出端口号后立即释放
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

# 3.给服务器绑定ip地址和端口号
server.bind(('127.0.0.1', 9999))

# 4.设置服务器监听
server.listen(128)
print('Server listening on 127.0.0.1:9999...')
# 等待客户端建立连接的请求，只有客户端合服务器建立连接成功，代码才会解阻塞，代码才能继续往下执行
# 专门和客户端通信的套接字：client_socket
# 客户端的ip地址和端口号：ip_port
client_socket, ip_port = server.accept()
print('Client connected...')
# 接收客户端发送的数据, 这次接收数据的最大字节数是1024
recv_data = client_socket.recv(1024).decode('utf-8')
# 获取数据的长度
recv_data_len = len(recv_data)
print(f'Receive data is: {recv_data}')
print(f'Receive data len: {recv_data_len}')

# 5.发送数据
send_data = f'你好,{ip_port[0]}'.encode('utf-8')
client_socket.send(send_data)

# 关闭服务与客户端的套接字，终止和客户端通信的服务
client_socket.close()
# 关闭服务器的套接字，终止和客户端提供建立连接请求的服务
server.close()

