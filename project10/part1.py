from tkinter import *

def generateArray(value):
    a = []
    for i in range(1, value+1):
        a.append(i)
    return a

def bottonCommand():
    entry = myEntry.get()
    if entry == "":
        mainLabel.config(text="Warning!\nВведите параметр!")
        return
    mainLabel.config(str(mySum(generateArray(int(entry)))))
    return

def mySum(L):
    if not L:
        return 0
    else:
        return L[0] + mySum(L[1:])

a = []
for i in range(1, 41):
    a.append(i)

root = Tk()

myEntry = Entry()
myEntry.pack()

mainLabel = Label(text="Введите параметр...")
mainLabel.pack(padx=10, pady=5)

myBotton = Button(text="Посчитать", command=bottonCommand)
myBotton.pack(pady=5)

myEntry.focus()

root.mainloop()