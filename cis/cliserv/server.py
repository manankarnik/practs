import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 3333))
s.listen(5)
print(f"Server running on ({socket.gethostname()}, 3333)")

while True:
    c, addr, = s.accept()
    message = c.recv(1024)
    print(message)
    c.close()
