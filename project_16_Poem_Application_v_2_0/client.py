import socket


def main():
    sock = socket.socket()
    sock.connect('localhost', 9090)
    sock.send('Hello world!')

    data = sock.recv(1024)
    sock.close()

    print(data)


if __name__ == "__main__":
    main()
