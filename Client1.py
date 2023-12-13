import socket
socket_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_c.bind(("127.0.0.1",4466))
socket_c.listen(2)
sock_a, addr = socket_c.accept()

msg = sock_a.recv()
print(msg.decode())

sock_a.close()