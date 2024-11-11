import socket
from cryptography.fernet import Fernet
from hashlib import sha256

key = b"n8aGE9BkWSAS2reguQG8dXNvWoHOcsrfcq25RcX6wA4="
f = Fernet(key)
message = input("Enter message: ")
digest = sha256(message.encode()).hexdigest().encode()
encrypted = f.encrypt(message.encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 8080))
s.send(encrypted + b"|" + digest)
s.close()
