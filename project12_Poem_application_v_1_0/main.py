from tkinter import *
import re
import os
import glob

class Application:
    root = 0
    btns = []

    def __init__(self, parent):
        self.root = parent
        parent.title('Poems application')
        parent.geometry('%dx%d+%d+%d' % (360, 240, 0, 0))
        self.menu()

    def menu(self):
        self.menu_lbl = Label(self.root, text="Menu:", font="helvetica 15")
        self.menu_lbl.pack()

        poem_name = self.poem_names()

        for i in range(len(poem_name)):
            b = Button(self.root, text=poem_name[i], command=lambda j=i: self.choice_poem(j))
            b.pack(pady=5)
            self.btns.append(b)

    def page(self, index):
        names = self.poem_names()

        self.root.geometry("500x400+0+0")
        self.root.title(names[index])

        self.page_lbl = Label(self.root, text=names[index], font="helvetica 15")
        self.page_lbl.pack()

        self.page_text = Label(self.root, text=self.poem_text(index + 1))
        self.page_text.pack()

        self.page_button = Button(self.root, text="Назад к меню <<<", command=self.page_btn_cmd)
        self.page_button.pack(side=BOTTOM, pady=15)


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


    def choice_poem(self, index):
        self.menu_lbl.pack_forget()
        for i in range(len(self.btns)):
            self.btns[i].pack_forget()
        self.page(index)

    def page_btn_cmd(self):
        self.page_text.pack_forget()
        self.page_lbl.pack_forget()
        self.page_button.pack_forget()

        self.menu()



def main():
    root = Tk()
    Application(root)
    root.mainloop()

if __name__ == '__main__':
    main()