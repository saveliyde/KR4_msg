import socket

s = socket.socket()
s.connect(('localhost', 9090))
s.send('hello, world!'.encode('utf-8'))

data = s.recv(1024)
s.close()

print(data)