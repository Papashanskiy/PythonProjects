import socket


def main():
    sock = socket.socket()      # Стандарно, как для клиента, так и для сервера
    sock.bind(('', 9090))       # Связываем хост и порт с сокетом
    sock.listen(1)              # Запускаем режим прослушивания с параметром, который отвечает за количество подключений
    conn, addr = sock.accept()   # Принимаем подключение

    print("connected: ", addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.send(data.upper())

    conn.close()


if __name__ == "__main__":
    main()
