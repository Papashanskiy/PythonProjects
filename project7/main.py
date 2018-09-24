from tkinter import *
import random
import time

times = 12

def listToStr(list):
    stre = ""
    for i in range(len(list)):
        stre += str(list[i]) + ", "
    return stre

def sort(quantity):
    item = [random.randint(-1000, 1000) for i in range(quantity)]
    arrayText = listToStr(item)
    for i in range(quantity):
        for j in range(i+1, quantity):
            if item[i] > item[j]:
                tmp = item[i]
                item[i] = item[j]
                item[j] = tmp
    arrayText += "  ======>  " + listToStr(item)
    array.config(text=item)
    pass


def restart():
    button.config(text="Restart", command=restart, bg="blue")
    sort(times)

root = Tk()
root.title("Sort")
root.geometry("500x100")

array = Label(root, font="40")
array.pack()

button = Button(root, text="Start", command=restart, bg='green', width=20, height=3, font="5")
button.pack(pady=10, padx=10)

sort(times)

button.focus()

root.mainloop()