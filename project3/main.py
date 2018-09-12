from tkinter import *

def buttonCommand():
    for i in labelList:
        i.config(text="ТОБI ПIЗДА!", bg="red")
        root.config(bg="black")
        b.config(bg="red", fg="black", font="Courier 16")

root = Tk()
root.geometry()

labelList = []

i = 0
while i < 3:
    l = Label(text=i, font="Courier 20")
    labelList.append(l)
    i += 1

for i in labelList:
    i.pack(padx=5, pady=20, side=LEFT)

b = Button(bg="black", text="НАТИСНИ НА МЕНЕ, КЛЯТИЙ МОСКАЛЯКА!", fg="white", command=buttonCommand, height=20, width=50)
b.pack(padx=5, pady=20, side=LEFT)

root.mainloop()