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
        parent.resizable(0, 0)

        url = os.getcwd() + '\\icon.ico'
        parent.iconbitmap(url)

        self.menu()

    # -------------------------------- Pages --------------------------------

    def menu(self):
        self.root.title("Menu")

        self.menu_lbl = Label(self.root, text="Menu:", font="helvetica 15")
        self.menu_lbl.grid(row=0, padx=20, sticky='W')

        poem_name = self.poem_names()

        self.geometry_controll(380, len(poem_name)) #    Добавление пространства эквивалентно количеству пунктов меню

        for i in range(len(poem_name)):
            b = Button(self.root, text=poem_name[i], command=lambda j=i: self.choice_poem(j),
                       borderwidth=2, relief="groove")
            b.grid(row=i, column=1, padx=10, pady=10, sticky='W')
            self.btns.append(b)

        self.add_poem_btm = Button(self.root, text="Add poem", command=self.add_poem_cmd,
                                   borderwidth=2, relief="groove")
        self.add_poem_btm.grid(row=1, padx=15, sticky='W')

        self.remove_poem_btn = Button(self.root, text="Remove poem", command=self.remove_btn,
                                      borderwidth=2, relief="groove")
        self.remove_poem_btn.grid(row=2, padx=15, sticky='W')

    def page(self, index):
        names = self.poem_names()

        self.root.title(names[index])

        self.page_lbl = Label(self.root, text=names[index], font="helvetica 15")
        self.page_lbl.pack()

        text = self.poem_text(index + 1)

        self.geometry_controll(500, self.count_lines(text) / 2)

        self.page_text = Label(self.root, text=text, font="helvetica 11")
        self.page_text.pack()


        self.page_button = Button(self.root, text="Back to menu <<<", command=self.page_btn_cmd,
                                  borderwidth=2, relief="groove")
        self.page_button.pack(side=BOTTOM, pady=15)

    def add_poem(self):
        self.root.title("Add poem")

        self.add_lbl = Label(self.root, text="Add poem", font="helvetica 15")
        self.add_lbl.grid(row=0, padx=10, pady=10)

        self.add_lbl_name = Label(self.root, text="Poem name", font="helvetica 10")
        self.add_lbl_name.grid(row=1, pady=10, padx=10, sticky='NW')

        self.add_entry = Entry(self.root, width=67, borderwidth=2, relief="groove")
        self.add_entry.grid(row=1, column=1, sticky='W')

        self.add_lbl_text = Label(self.root, text="Poem text", font="helvetica 10")
        self.add_lbl_text.grid(row=2, padx=10, pady=10, sticky='NW')

        self.add_scroll = Scrollbar(self.root)
        self.add_text = Text(self.root, height=16, width=50, borderwidth=2, relief="groove")
        self.add_text.grid(row=2, column=1, pady=10, sticky='W')
        self.add_scroll.grid(row=2, column=1, sticky='E')
        self.add_scroll.config(command=self.add_text.yview)
        self.add_text.config(yscrollcommand=self.add_scroll.set)

        self.add_btm = Button(self.root, text="Add poem", command=self.add_btm_cmd, borderwidth=2, relief="groove")
        self.add_btm.grid(row=3, column=1, pady=10, sticky='E')

        self.add_btm_back = Button(self.root, text="Back to menu", command=self.add_back_cmd,
                                   borderwidth=2, relief="groove")
        self.add_btm_back.grid(row=4, column=1, pady=10, sticky='E')

        self.root.geometry("540x470")

    def remove_poem(self):
        self.root.title("Remove poem")

        self.remove_frame = Frame(self.root)
        self.remove_frame.grid()

        self.del_main_lbl = Label(self.remove_frame, text="Remove:", font="helvetica 15")
        self.del_main_lbl.grid(row=0, pady=15, padx=10, sticky='W')

        text = 'Select which poem \nyou want to delete:'

        del_lbl_info = Label(self.remove_frame, text=text)
        del_lbl_info.grid(row=1, padx=10)

        del_back_btn = Button(self.remove_frame, text="Back to menu", borderwidth=2, relief="groove",
                              command=self.del_back_cmd)
        del_back_btn.grid(row=2, padx=10, sticky='W')

        poem_name = self.poem_names()

        self.geometry_controll(400, len(poem_name))  # Добавление пространства эквивалентно количеству пунктов меню

        for i in range(len(poem_name)):
            b = Button(self.remove_frame, text=poem_name[i], command=lambda j=i: self.del_poem_cmd(j),
                       borderwidth=2, relief="groove")
            b.grid(row=i, column=1, padx=10, pady=10, sticky='W')
            self.btns.append(b)

    # -------------------------------- Help functions --------------------------------

    def geometry_controll(self, x, y):
        space = y * 35 + 100
        self.root.geometry('%dx%d' % (x, space))
        pass

    def count_lines(self, str):
        lines = re.findall('\n', str)
        count = 0
        for _ in lines:
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

    # -------------------------------- Help for commands --------------------------------

    def remove_menu_w(self):
        self.menu_lbl.grid_forget()
        for i in range(len(self.btns)):
            self.btns[i].grid_forget()
        self.add_poem_btm.grid_forget()
        self.remove_poem_btn.grid_forget()

    def remove_page_w(self):
        self.page_text.pack_forget()
        self.page_lbl.pack_forget()
        self.page_button.pack_forget()

    def remove_add_w(self):
        self.add_entry.grid_forget()
        self.add_text.grid_forget()
        self.add_lbl_text.grid_forget()
        self.add_btm.grid_forget()
        self.add_scroll.grid_forget()
        self.add_lbl_name.grid_forget()
        self.add_lbl.grid_forget()
        self.add_btm_back.grid_forget()

    # -------------------------------- Button commands --------------------------------

    def choice_poem(self, index):
        self.remove_menu_w()
        self.page(index)

    def page_btn_cmd(self):
        self.remove_page_w()
        self.menu()

    def add_poem_cmd(self):
        self.remove_menu_w()
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

        self.remove_add_w()

        self.menu()

    def add_back_cmd(self):
        self.remove_add_w()
        self.menu()

    def remove_btn(self):
        self.remove_menu_w()
        self.remove_poem()

    def del_poem_cmd(self, i):
        self.remove_frame.grid_forget()
        self.menu()

    def del_back_cmd(self):
        self.remove_frame.grid_forget()
        self.menu()

# -------------------------------- End of class --------------------------------

def main():
    root = Tk()
    Application(root)
    root.mainloop()

if __name__ == '__main__':
    main()