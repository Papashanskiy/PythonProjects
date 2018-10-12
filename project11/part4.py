from tkinter import *
from tkinter import ttk

class Duo:

    root = Tk()
    btn = ttk.Button(root)
    lbl = Label(root, font="time 15")
    botn_text = Label(root, text="Stopping by Woods on a Snowy Evening\nby Robert Frost", font="time 10")

    def __init__(self):
        self.root.geometry("640x350")
        self.frst_disp()
        self.btn.pack(padx=15, pady=15)
        self.lbl.pack()
        self.botn_text.pack(side=BOTTOM, pady=15)

    def ml(self):
        self.root.mainloop()

    def frst_disp(self):
        self.root.title("First page")
        self.btn.config(text=">>>", command=lambda: self.sec_disp(),
                        width=150)
        str = self.file_open(1)
        self.lbl.config(text=str)

    def sec_disp(self):
        self.root.title("Second page")
        self.btn.config(text="<<<", command=lambda: self.frst_disp())
        str = self.file_open(2)
        self.lbl.config(text=str)

    def file_open(self, n):
        file_name = 'config_' + str(n) + '.txt'
        f = open(file_name, 'r')
        result = f.read()
        f.close()
        return result

d = Duo()



d.ml()