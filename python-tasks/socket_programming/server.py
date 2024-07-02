import socket
import threading

def clintHandeller(clintFd, address):
  # 5) recv data
  msg = clintFd.recv(1024).decode()
  print(f'[clint]: {address[0]} says: ', msg)

  # 6) send data
  msg = input('msg: ')
  clintFd.send(msg.encode())

  clintFd.close()




def run_srever(): 
  try:
    # 1) create socket  
    serverFd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2) bind socket
    serverFd.bind(('127.0.0.1', 3000))

    # 3) listen to req
    serverFd.listen(5)
    print(f'Server is up and running on 127.0.0.1:{3000}')

    # 4) accept that req
    while True:
      clintFd, address=serverFd.accept() 
      print(f'clint with address:{address} connected')

      t1 = threading.Thread(target=clintHandeller, args=(clintFd, address))
      t1.start()

  except Exception as e:
    print(e)
    serverFd.close()


run_srever()