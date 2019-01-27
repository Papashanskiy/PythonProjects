from tkinter import *
import random
import time
import threading
import sys


class MyThread:

    root = ''

    def __init__(self, import_root):
        self.root = import_root
        self.root.geometry('500x300')
        self.root.title('Thread application')
        self.root.config(bg='black')
        self.root.resizable(0, 0)

        self.lb_1 = Label(self.root, text='first', font='Helvetica 12 bold', fg='blue', bg='black', width=10)
        self.lb_2 = Label(self.root, text='second', font='Helvetica 12 bold', fg='green', bg='black', width=10)
        self.lb_3 = Label(self.root, text='third', font='Helvetica 12 bold', fg='orange', bg='black', width=10)

        self.lb_1.pack(side=LEFT, padx=20)
        self.lb_2.pack(side=LEFT, padx=20)
        self.lb_3.pack(side=LEFT, padx=20)

        self.exit_btn = Button(self.root, text='Stop!', bg='red', fg='white', command=self.exit_btn_cmd)
        self.exit_btn.pack(side=BOTTOM, pady=15)

        self.run()

    def run(self):
        self.threads = []
        for i in range(3):
            thread = threading.Thread(target=self.processing, args=(i,), daemon=True)
            self.threads.append(thread)
            self.threads[i].start()

    def processing(self, step):

        counter = [0, 0, 0]

        if step == 0:
            while True:
                self.lb_1.config(text=counter[0])
                counter[0] += 1
                time.sleep(0.01)
        elif step == 1:
            while True:
                self.lb_2.config(text=counter[1])
                counter[1] += 1
                time.sleep(0.25)
        elif step == 2:
            while True:
                self.lb_3.config(text=counter[2])
                counter[2] += 1
                time.sleep(1)
        else:
            sys.exit()

    def exit_btn_cmd(self):
        sys.exit()


def main():
    root = Tk()
    MyThread(root)
    root.mainloop()


if __name__ == '__main__':
    main()
