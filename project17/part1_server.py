import socket


def main():

    print("SERVER:", "lets start this shit bitches")

    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(10)

    conn, addr = sock.accept()

    print(addr, "connected")

    while True:
        data = conn.recv(1024)
        print("USER", addr, data.decode())
        if not data:
            break
        conn.send("Hello bitch, you are welcome, motherfucker".encode())


if __name__ == "__main__":
    main()
