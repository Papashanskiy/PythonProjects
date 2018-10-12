from tkinter import *

def btn_cmnd():
    if entr.get() == "":
        lbl.config(text="Warning!\nEntry is empty...\nInput something in it...")
    else:
        str = entr.get()
        lbl.config(text=str)

root = Tk()
root.title("First window")
root.geometry("360x240")

top = Toplevel()
top.title("Second window")
top.geometry("360x240")

entr = Entry(top)
entr.pack()

btn = Button(top, command=btn_cmnd, text="Enter")
btn.pack()

lbl = Label(root, text="Hello, input something in the second window...")
lbl.pack()

root.mainloop()