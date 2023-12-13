import socket
socket_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_c.connect(("127.0.0.1",4466))

msg = socket_c.recv()
print(msg.decode())

socket_c.close()