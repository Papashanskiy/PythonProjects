from tkinter import *
from tkinter import messagebox
import re
import os
import glob

class Application:
    root = 0
    btns = []

    def __init__(self, parent):
        self.root = parent
        parent.title('Poems application')
        parent.geometry('%dx%d+%d+%d' % (360, 100, 0, 0))
        self.menu()

    # -------------------------------- Pages --------------------------------

    def menu(self):
        self.menu_lbl = Label(self.root, text="Menu:", font="helvetica 15")
        self.menu_lbl.pack()

        poem_name = self.poem_names()

        self.geometry_controll(360, len(poem_name)) #    Добавление пространства эквивалентно количеству пунктов меню

        for i in range(len(poem_name)):
            b = Button(self.root, text=poem_name[i], command=lambda j=i: self.choice_poem(j))
            b.pack(pady=5)
            self.btns.append(b)

        self.add_poem_btm = Button(self.root, text="Add poem", command=self.add_poem_cmd)
        self.add_poem_btm.pack(side=BOTTOM, pady=15)

    def page(self, index):
        names = self.poem_names()

        self.root.title(names[index])

        self.page_lbl = Label(self.root, text=names[index], font="helvetica 15")
        self.page_lbl.pack()

        text = self.poem_text(index + 1)

        self.geometry_controll(500, self.count_lines(text) / 2)

        self.page_text = Label(self.root, text=text)
        self.page_text.pack()


        self.page_button = Button(self.root, text="Back to menu <<<", command=self.page_btn_cmd)
        self.page_button.pack(side=BOTTOM, pady=15)

    def add_poem(self):
        self.add_lbl = Label(self.root, text="Add poem", font="helvetica 15")
        self.add_lbl.pack()

        self.add_lbl_name = Label(self.root, text="Poem name", font="helvetica 10")
        self.add_lbl_name.pack(pady=10)

        self.add_entry = Entry(self.root, width=50)
        self.add_entry.pack()

        self.add_lbl_text = Label(self.root, text="Poem text", font="helvetica 10")
        self.add_lbl_text.pack(pady=10)

        self.add_scroll = Scrollbar(self.root)
        self.add_text = Text(self.root, height=16, width=40)
        self.add_scroll.pack(side=RIGHT, fill=Y)
        self.add_text.pack(side=LEFT, fill=BOTH, expand=1, padx=15, pady=10)
        self.add_scroll.config(command=self.add_text.yview)
        self.add_text.config(yscrollcommand=self.add_scroll.set)

        self.add_btm = Button(self.root, text="Add poem\nand back to menu", command=self.add_btm_cmd)
        self.add_btm.pack(side=BOTTOM, pady=20, padx=20)

        self.root.geometry("700x400")

    # -------------------------------- Help functions --------------------------------

    def geometry_controll(self, x, y):
        space = y * 35 + 100
        self.root.geometry('%dx%d' % (x, space))
        pass

    def count_lines(self, str):
        lines = re.findall('\n', str)
        count = 0
        for i in lines:
            count += 1
        return count

    def count_poems(self):
        counter = 0
        way = os.getcwd() + '\\poems\\*'
        url = glob.glob(way)
        for i in url:
            counter += 1
        return counter

    def poem_names(self):
        result = []
        way = os.getcwd() + '\\poems\\'
        url = glob.glob(way+'\\*')
        for i in url:
            f = open(i, 'r')
            str = f.read()
            find = re.findall(r'(?<=<author>)(.*)(?=</author>)', str)
            result.append(find[0])
            f.close()
        return result

    def poem_text(self, index):
        way = os.getcwd() + '\\poems\\'
        url = glob.glob(way+'poem_%d.txt' % index)
        f = open(url[0], 'r')
        str = f.read()
        find = re.findall(r'<text>(.*)</text>', str, flags=re.DOTALL)
        result = find[0]
        f.close()
        return result

    # -------------------------------- Button commands --------------------------------

    def choice_poem(self, index):
        self.menu_lbl.pack_forget()
        for i in range(len(self.btns)):
            self.btns[i].pack_forget()
        self.add_poem_btm.pack_forget()
        self.page(index)

    def page_btn_cmd(self):
        self.page_text.pack_forget()
        self.page_lbl.pack_forget()
        self.page_button.pack_forget()

        self.menu()

    def add_poem_cmd(self):
        self.menu_lbl.pack_forget()
        for i in range(len(self.btns)):
            self.btns[i].pack_forget()
        self.add_poem_btm.pack_forget()
        self.add_poem()

    def add_btm_cmd(self):
        name = self.add_entry.get()
        text = self.add_text.get("1.0", END)
        empty = re.match('^[A-Za-z0-9_-]*', text)
        if name == "" or empty.group() == "":
            messagebox.showinfo("Error!", "Enter title of poem and text poem!") # Момент под вопросом, так как
        else:                                                                   # поиск выдает результат построчно
            count = self.count_poems()                                          # и получаются несколько лишних ""
            file_name = 'poems\\poem_' + str(count + 1) + '.txt'

            result = "<author>" + str(name) + "</author>" + "\n\n"
            result += "<text>" + text + "</text>"

            f = open(file_name, 'w')
            f.write(result)
            f.close()

        self.add_entry.pack_forget()
        self.add_text.pack_forget()
        self.add_lbl_text.pack_forget()
        self.add_btm.pack_forget()
        self.add_scroll.pack_forget()
        self.add_lbl_name.pack_forget()
        self.add_lbl.pack_forget()

        self.menu()


# -------------------------------- End of class --------------------------------

def main():
    root = Tk()
    Application(root)
    root.mainloop()

if __name__ == '__main__':
    main()