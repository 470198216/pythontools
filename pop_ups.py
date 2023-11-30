import win32api
from socket import socket, AF_INET, SOCK_STREAM
def pop_ups(message):
    win32api.MessageBox(0, message, "tips")

def echo_handle(address, client_sock):
    print("Got connect from {}".format(address))
    while True:
        msg = client_sock.recv(8192)
        if not msg:
            break
        client_sock.sendall(msg)
        pop_ups(msg.decode('utf-8'))
    client_sock.close()

def echo_server(address, backlog=5):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(backlog)
    while True:
        client_sock, client_addr = sock.accept()
        echo_handle(client_addr, client_sock)

if __name__ == '__main__':
    echo_server(('', 20000))
