import socket, random


def accept_enter(data):
    return random.randint(0, 1)


sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

print("connected", addr)

while True:
    data = conn.recv(1024)
    print(data)
    if not data:
        break
    conn.send(str(accept_enter(data)).encode())

conn.close()
