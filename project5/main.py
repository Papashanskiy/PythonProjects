from math import sqrt
from tkinter import *
from tkinter import ttk

def converting(some):
    if some == '':
        return 0
    try:
        var = float(some)
    except ValueError:
        return "None"
    return var


def equation(a, b, c):
    answer = "Ответ: "
    if a == 0 and b == 0 and c == 0:
        return "Не были введены коэффициенты!"
    elif a == 0 and b == 0:
        return str(c) + " не равно 0!"
    elif a == 0:
        answer += str(-c / b)
        return answer
    else:
        d = b*b - 4*a*c
        if d > 0:
            x = [round((-b + sqrt(d)) / (2 * a), 5), round((-b - sqrt(d)) / (2 * a), 5)]
            answer += str(x[0]) + ", " + str(x[1])
            return answer
        elif d == 0:
            answer += str(round(-b / 2*a, 5))
            return answer
        else:
            answer += "Нет корней"
            return answer

def buttonCommand():
    a = converting(aEntry.get())
    b = converting(bEntry.get())
    c = converting(cEntry.get())
    x = equation(a, b, c)
    answerLabel.config(text=x)

root = Tk()

root.title("Квадратное уравнение")
root.resizable(0, 0)

topFrame = Frame()
topFrame.pack()
bottomFrame = Frame()
bottomFrame.pack(side=BOTTOM)

description = '''Данная программа предназначена для решения квадратного уравнения.
Введите в поля a, b и c желаемые коэффициенты:'''
lDescription = Label(topFrame, text=description, padx=15, pady=10)
lDescription.pack()

space = Frame(topFrame, width=90)
space.pack(side=LEFT)
aEntry = ttk.Entry(topFrame, width=10)
aEntry.pack(side=LEFT)
doubleXLabel = Label(topFrame, text="x^2 +")
doubleXLabel.pack(side=LEFT)

bEntry = ttk.Entry(topFrame, width=10)
bEntry.pack(side=LEFT)
xLabel = Label(topFrame, text="x +")
xLabel.pack(side=LEFT)

cEntry = ttk.Entry(topFrame, width=10)
cEntry.pack(side=LEFT)
zeroLabel = Label(topFrame, text=" = 0")
zeroLabel.pack(side=LEFT)

answerLabel = Label(bottomFrame, text="")
answerLabel.pack(pady=10)
buttomSpace = Frame(bottomFrame, width=300)
buttomSpace.pack(side=LEFT, pady=10)
submit = ttk.Button(bottomFrame, text="Решить уравнение", command=buttonCommand)
submit.pack(pady=10)

aEntry.focus()

root.mainloop()