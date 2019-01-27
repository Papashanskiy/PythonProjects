import imaplib
import email
import time

# ЧТЕНИЕ ПОСЛЕДНЕГО СООБЩЕНИЯ С ПОЧТЫ

class MyMail:
    MY_LOGIN = 'KFU.Anatomy.2018@gmail.com'
    MY_PSW = 'z31aedc170f8'

    def __init__(self):
        self.my_email = imaplib.IMAP4_SSL("imap.gmail.com", 993)
        self.my_email.login(self.MY_LOGIN, self.MY_PSW)
        self.my_email.select("INBOX")

    def loop(self):
        self.my_email.select("INBOX")
        n = 0
        typ, data = self.my_email.search(None, '(ALL)')
        if typ == "OK":
            for num in data[0].split():
                n += 1
                print(n)
                typ, data = self.my_email.fetch(num, '(RFC822)')
                for respone_part in data:
                    if isinstance(respone_part, tuple):
                        original = email.message_from_string(respone_part[1].decode('utf-8'))
                        print(original['From'])
                        data = original['Subject']
                        for i in data:
                            print(i)
                        typ, data = self.my_email.store(num, '+FLAGS', '\\Seen')
        print(n)
        time.sleep(1)


def main():
    my_email = MyMail()
    try:
        while True:
            my_email.loop()
    finally:
        print('Thanks!')


if __name__ == '__main__':
    main()
