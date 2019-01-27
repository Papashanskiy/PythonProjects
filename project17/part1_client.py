import socket


def main():

    for i in range(3):
        sock = socket.socket()
        sock.connect(('localhost', 9090))
        sock.send("You are bitch nigger!".encode())

        answer = sock.recv(1024)
        sock.close()

        print("SERVER:", answer.decode())


if __name__ == "__main__":
    main()
