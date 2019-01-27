import sqlite3
from sqlite3 import Error
from threading import *
import imaplib


# questions (id int, question text, answer_1 text, answer_2 text, answer_3 text, answer_4 text, right_answer tinyint)'


class MyImport:

    ORG_EMAIL = '@gmail.com'
    FROM_EMAIL = 'KFU.Anatomy.2018' + ORG_EMAIL
    FROM_PWD = 'z31aedc170f8'
    SMTP_SERVER = 'imap.gmail.com'
    SMTP_PORT = 993

    def __init__(self):


    def login(self):
        mail = imaplib.IMAP4_SSL(self.SMTP_SERVER)
        mail.login(self.FROM_EMAIL, self.FROM_PWD)
        return mail

    def read(self):
        mail = self.login()
        mail.select('inbox')

        type, data = mail.search(None, 'ALL')
        mail_ids = data[0]
        id_list = mail_ids.split()

        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

    def run(self):
        pass


class TestCheck:
    full_name = ''
    answers = []
    variant = 1
    db = 'q.db'

    def __init__(self, full_name, answers, variant):
        self.full_name = full_name
        self.answers = answers
        self.variant = variant

    def load_db(self):
        return

    def save_result(self):
        return

    def check(self):
        return

    def create_connection(self, db_file):
        try:
            conn = sqlite3.connect('db_file')
            return conn
        except Error as e:
            print(e)

        return None


def main():
    threads = []



if __name__ == '__main__':
    main()
