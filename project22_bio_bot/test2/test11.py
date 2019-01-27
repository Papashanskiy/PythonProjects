import sqlite3
import random
import string

# db questions
# u (username text, var int, count_r_a int)
# q (question text, a_1 text, a_2 text, a_3 text, a_4 text, r_a int)
# v (username text, q_n text) q_v - question number (string: '[1, 2, 7, 8]')

class BioCheck:
    db_name = 'questions.db'
    MY_VOWELS = 'aieou'
    COUNT_VARIANTS = 0
    COUNT_QUESTIONS = 0

    def __init__(self, is_external=False):
        conn, c = self.db_connect()
        a = c.execute('SELECT * FROM q').fetchall()
        count = 0
        for _ in a:
            count += 1
        self.COUNT_QUESTIONS = count
        self.COUNT_VARIANTS = count / 20

    def db_connect(self):
        try:
            conn = sqlite3.connect(self.db_name)
            c = conn.cursor()
        except sqlite3.Error as e:
            print(e)
            print("Не удалось подключиться к базе данных!")
            exit(1)
        return conn, c

    def check(self, answers, variant):
        conn, c = self.db_connect()

    def create_table(self):
        conn, c = self.db_connect()
        c.execute('CREATE TABLE IF NOT EXISTS q (question text, a_1 text, a_2 text, a_3 text, a_4 text, r_a int)')
        conn.commit()
        for i in range(100):
            try:
                q, a_1, a_2, a_3, a_4, r_a = self.randomize()
                params = (q, a_1, a_2, a_3, a_4, r_a)
                c.execute('INSERT INTO q VALUES (?, ?, ?, ?, ?, ?)', params)
                conn.commit()
            except sqlite3.Error as e:
                print(e)
                print(f'Не удалось добавить данные в базу данных {self.db_name}')
                exit(1)

    def create_table_u(self):
        conn, c = self.db_connect()
        c.execute('CREATE TABLE IF NOT EXISTS u (username text, var int, count_r_a int)')
        conn.commit()

    def show_teble(self):
        conn, c = self.db_connect()
        a = c.execute('SELECT * FROM q').fetchall()
        count = 0
        for i in a:
            count += 1
        print(count)

    def randomize(self):
        q = ''.join(random.choice(string.ascii_lowercase + string.whitespace) for _ in range(random.randint(60, 90))).capitalize()
        a_1 = ''.join(random.choice(string.ascii_lowercase + string.whitespace) for _ in range(random.randint(30, 40))).capitalize()
        a_2 = ''.join(random.choice(string.ascii_lowercase + string.whitespace) for _ in range(random.randint(30, 40))).capitalize()
        a_3 = ''.join(random.choice(string.ascii_lowercase + string.whitespace) for _ in range(random.randint(30, 40))).capitalize()
        a_4 = ''.join(random.choice(string.ascii_lowercase + string.whitespace) for _ in range(random.randint(30, 40))).capitalize()
        r_a = random.randint(1, 4)
        return q, a_1, a_2, a_3, a_4, r_a

    def randomize_answers(self):
        username = ''
        for _ in range(random.randint(2, 5)):
            username += username.join(random.choice(string.ascii_lowercase))
            username += username.join(random.choice(self.MY_VOWELS))
        username = username.capitalize()
        username += ' '

        last_name = ''
        for _ in range(random.randint(2, 5)):
            last_name += last_name.join(random.choice(string.ascii_lowercase))
            last_name += last_name.join(random.choice(self.MY_VOWELS))
        last_name = last_name.capitalize()

        username += last_name

        variant = random.randint(1, self.COUNT_VARIANTS)

        answers = []
        for _ in range(20):
            answers.append(random.randint(1, 4))

        return username, variant, answers


class BioVariant:
    DB_NAME = 'variant.db'
    MY_VOWELS = 'aieou'

    def db_connect(self):
        try:
            conn = sqlite3.connect(self.DB_NAME)
            c = conn.cursor()
        except sqlite3.Error as e:
            print(e)
            print("Не удалось подключиться к базе данных!")
            exit(1)
        return conn, c

    def create_table_v(self):
        conn, c = self.db_connect()
        c.execute('CREATE TABLE IF NOT EXISTS v (username text, q_n text)')
        conn.commit()

    # Случайный вариант
    def add_info_v(self):
        conn, c = self.db_connect()
        bio = BioCheck()
        count_q = bio.COUNT_QUESTIONS

        username = ''
        answers = []
        answers_str = ''
        for _ in range(10):
            username = self.name()

            for i in range(20):
                answers.append(str(random.randint(1, count_q)))

            answers_str = ' '.join(answers)
            del answers[1:-1]

            params = [username, answers_str]

            try:
                c.execute('INSERT INTO v VALUES(?, ?)', params)
                conn.commit()
            except sqlite3.Error as e:
                print(e)
                print("Не удалось добавить данные в таблицу v")

    def look_into_v(self):
        conn, c = self.db_connect()
        try:
            a = c.execute('SELECT rowid, * FROM v').fetchall()
        except sqlite3.Error as e:
            print(e)
            print("Не удалось получить данные из таблицы v")

        for i in a:
            print(i[0], i[1])


    def name(self):
        username = ''
        for _ in range(random.randint(2, 5)):
            username += username.join(random.choice(string.ascii_lowercase))
            username += username.join(random.choice(self.MY_VOWELS))
        username = username.capitalize()
        username += ' '

        last_name = ''
        for _ in range(random.randint(2, 5)):
            last_name += last_name.join(random.choice(string.ascii_lowercase))
            last_name += last_name.join(random.choice(self.MY_VOWELS))
        last_name = last_name.capitalize()

        username += last_name
        return username

def main():
    conn = BioCheck()
    variant = BioVariant()
    variant.look_into_v()



if __name__ == '__main__':
    main()
