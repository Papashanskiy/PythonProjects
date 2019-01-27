from threading import *
import time, sqlite3, random, string, os
from sqlite3 import Error

# РАБОТА С БАЗОЙ ДАННЫХ И РАНДОМАЙЗЕР

class MyClass:
    MY_DOMENS = ['@gmail.com',
                 '@mail.ru',
                 '@yandex.ru',
                 '@yahoo.com']
    MY_COLORS = ['red',
                 'blue',
                 'black',
                 'orange',
                 'green',
                 'white']
    MY_VOWELS = 'aieou'
    DB_NAME = os.getcwd() + '\my_db.db'

    def steal_db(self):
        conn, c = self.connect_db()

        a = c.execute('SELECT * FROM users')
        a = a.fetchall()
        counter = 1
        for i in a:
            print(counter, i)
            counter += 1

    def insert_one_user(self, username, email, age, fav_color):
        conn, c = self.connect_db()
        params = (username, email, age, fav_color)
        try:
            c.execute('INSERT INTO users VALUES (?, ?, ?, ?)', params)
            conn.commit()
        except sqlite3.Error as err:
            print(err)


    def my_function(self):
        conn, c = self.connect_db()

        for i in range(1000):
            n, e, a, color = self.my_randomizer()
            params = (n, e, a, color)
            try:
                c.execute('INSERT INTO users VALUES (?, ?, ?, ?)', params)
                conn.commit()
            except Error as err:
                print(err)

    def my_randomizer(self):
        username = ''
        email = ''
        for _ in range(random.randint(2, 5)):
            username += username.join(random.choice(string.ascii_lowercase))
            username += username.join(random.choice(self.MY_VOWELS))

        email += username + random.choice(self.MY_DOMENS)

        age = random.randint(16, 65)

        favorite_color = random.choice(self.MY_COLORS)
        return username.capitalize(), email.capitalize(), age, favorite_color

    def connect_db(self):
        try:
            conn = sqlite3.connect(self.DB_NAME)
            c = conn.cursor()
        except sqlite3.Error as err:
            print(err)
        return conn, c


def main():
    my_subject = MyClass()

    my_subject.insert_one_user('Charlz', 'Charlz@yahoo.com', 25, 'red')

    my_subject.steal_db()


if __name__ == '__main__':
    main()
