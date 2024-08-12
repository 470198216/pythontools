import socket

# 创建一个socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定到本地地址和端口
server_ip = '0.0.0.0'  # 本地IP地址
server_port = 60060       # 本地端口号

# 绑定socket
server_socket.bind((server_ip, server_port))

print(f"UDP server up and listening on {server_ip}:{server_port}")

try:
    while True:
        # 接收客户端数据
        data, client_address = server_socket.recvfrom(1024)  # 缓冲区大小为1024字节
        print(f"Received message from {client_address}: {data.decode()}")
        
        # 响应客户端
        response = "Hello, UDP Client!"
        server_socket.sendto(response.encode(), client_address)

except KeyboardInterrupt:
    print("UDP server is shutting down.")

finally:
    # 关闭socket连接
    server_socket.close()