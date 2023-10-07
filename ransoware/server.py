from cryptography.fernet import Fernet
import socket

key = Fernet.generate_key()
print ("La clé est : ", key)

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 4321))
s.listen(5)  

conn, addr = s.accept()
print(addr, " connecté")

msg = conn.recv(2048).decode()
if msg == "key":
    conn.send(key)
    print("Clé Envoyée ! ")