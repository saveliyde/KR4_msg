import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 9090

s.bind(('', port))
s.listen(1)

conn, addr = s.accept()

print('connected:', addr)

Flag = True

while Flag:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data.upper())