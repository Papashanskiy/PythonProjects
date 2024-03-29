import socket


def main():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 9090))
        s.listen()
        conn, addr = s.accept()

        with conn:
            print('connected by <', addr, '>')
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data.upper())


if __name__ == '__main__':
    main()
