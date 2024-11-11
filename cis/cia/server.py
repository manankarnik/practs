import socket
from cryptography.fernet import Fernet
from hashlib import sha256

key = b"n8aGE9BkWSAS2reguQG8dXNvWoHOcsrfcq25RcX6wA4="
f = Fernet(key)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host, port = socket.gethostname(), 8080
s.bind((host, port))

s.listen(5)
print(f"Server running on {host}:{port}")

while True:
    c = i = a = False
    cs, addr = s.accept()
    data = cs.recv(1024)
    a = True
    encrypted, digest = data.split(b"|")
    message = f.decrypt(encrypted)
    c = True
    calculated_digest = sha256(message).hexdigest()
    if (calculated_digest == digest.decode()): i = True
    print("Message:", message.decode())
    print("Digest:", digest.decode())
    if (c and i and a): print("CIA verified")
    else: print("CIA not verified")
    cs.close()

