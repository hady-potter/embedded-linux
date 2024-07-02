import socket

# create socket
fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
print('ip:', ip)
# connect to server
fd.connect(("127.0.0.1", 3000))

# chatting

  # send msg
msg = str(input('\nmsg: '))
fd.send(msg.encode())

# recv msg
msg = fd.recv(1024).decode()
print('[server]', msg, end='')

fd.close()
