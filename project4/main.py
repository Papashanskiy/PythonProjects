from tkinter import *
from tkinter import ttk
import tkinter.messagebox

def check(str):
    count = 0
    for i in str:
        count += 1
    if count == 0:
        return FALSE
    else:
        return TRUE

def myLogin():
    userName = U.get()
    if check(userName) == FALSE:
        tkinter.messagebox.showinfo("Warning!", "Username or password ain't entered!")
        return
    password = P.get()
    if check(password) == FALSE:
        tkinter.messagebox.showinfo("Warning!", "Username or password ain't entered!")
        return
    print("Login: ", userName, "\nPassword: ", password)

root = Tk()
root.title("My application client")
root.geometry("320x240")
root.iconbitmap(default="tree.ico")

F = Frame(padx=25, pady=25)
F.pack()

LU = Label(F, text="Enter your username:")
LU.pack()

U = ttk.Entry(F, width=50, font="30")
U.pack(pady=10)

LP = Label(F, text="Enter your password:")
LP.pack()

P = ttk.Entry(F, show="*", width=50, font="30")
P.pack(pady=10)

B = ttk.Button(F, text="Log on", width=15, command=myLogin)
B.pack()

root.mainloop()