import time
import threading
import random


class WellBooby:

    def __init__(self):
        self.threads = {}
        t = threading.Thread(target=self.mainloop, daemon=True, name='mainloop')
        self.threads['mainloop'] = t
        self.threads['mainloop'].run()

    def mainloop(self):
        while True:
            var = random.randint(1, 5)
            print(var)
            if var == 1:
                t = threading.Thread(target=self.fun_1, name='fun_1')
                self.threads['fun_1'] = t
                self.threads['fun_1'].run()
            elif var == 4:
                t = threading.Thread(target=self.fun_2, name='fun_2')
                self.threads['fun_2'] = t
                self.threads['fun_2'].run()
            time.sleep(1)

    def fun_1(self):
        print('\nHello. Your random number was 1\n')
        return

    def fun_2(self):
        print('\nHello. Your random number was 4\n')
        return


def main():
    subj = WellBooby()


if __name__ == '__main__':
    main()
