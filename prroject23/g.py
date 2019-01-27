from .. import main


class Note:
    def sum(self, a, b):
        return a+b

    def run(self):
        print(main.MAIN)


note = Note()
note.run()
