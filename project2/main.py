from tkinter import *

counter = 0
def counter_label(label):
    def count():
        global counter
        counter += 1
        label.config(text=counter)
        label.after(1000, count)
    count()

def space():
    l.config(fg="blue")

root = Tk()
root.title("Counting seconds")
root.configure(bg="black")
root.bind('<space>', space)

l = Label(root, fg="green", font="Courier 100", bg="black")
l.pack()
counter_label(l)

button2 = Button(root, bg="green", fg="white", text="Стоп!", width=40, command=root.destroy)
button2.pack()

root.mainloop()