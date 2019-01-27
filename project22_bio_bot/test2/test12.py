import threading
import imaplib
import email


class BiologyTest:
    threads = []
    login = 'kfu.anatomy.2018@gmail.com'
    pwd = 'z31aedc170f8'
    imap_host = 'imap.gmail.com'

    def run(self):
        mail_thread = threading.Thread(target=self.mails(), name='Mail_thread')
        self.threads.append(mail_thread)
        mail_thread.run()

    def mails(self):
        while True:
            self.mails_check()

    def check(self):
        pass

    def mails_check(self):
        imap = imaplib.IMAP4_SSL(self.imap_host)
        imap.login(self.login, self.pwd)
        imap.select('INBOX')
        rv, data = imap.search(None, 'ALL')

        num = data[0].split()

        for i in num:
            rv, data = imap.fetch(i, '(RFC822)')
            email_message = email.message_from_bytes(data[0][1])
            return email_message

def main():
    return


if __name__ == '__main__':
    main()
