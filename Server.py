import socket
socket_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_s.bind(("127.0.0.1",4466))
socket_s.listen(2)
sock_a, addr = socket_s.accept()

mdg = "Welcom"
socket_s.send(msg.encode())

sock_a.close()