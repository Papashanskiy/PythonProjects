from tkinter import *
import socket


def send_to_server(data):

    data_str = ''

    data_str = data_str.join("<name>" + str(data[0]) + "</name>\n")
    data_str = data_str.join("<passw>" + str(data[1]) + "</passw>")

    print(data_str)

    sock = socket.socket()
    sock.connect(('localhost', 9090))
    sock.send(data_str.encode())

    answer = sock.recv(1024)
    sock.close()
    return answer


def subm_cmd(name, passw, lbl):
    pack_data = (name, passw)
    lbl.config(text=send_to_server(pack_data))


def main():
    root = Tk()

    lbl = Label(root)
    lbl.pack()

    name_e = Entry(root)
    pass_e = Entry(root)

    name_e.pack()
    pass_e.pack()

    subm = Button(root, text="enter", command=lambda: subm_cmd(name_e.get(), pass_e.get(), lbl))
    subm.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
