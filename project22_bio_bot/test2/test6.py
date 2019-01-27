import smtplib

# ПРОСТОЕ СООБЩЕНИЕ НА ПОЧТУ

class SendMessage:
    email_id = 'kfu.anatomy.2018@gmail.com'
    email_pwd = 'z31aedc170f8'

    def send_message(self, receiver, message):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(self.email_id, self.email_pwd)
        s.sendmail(self.email_id, receiver, message)
        s.quit()


def main():
    s = SendMessage()

    message = 'Hello\nThat\'s my testing message for you.\nHow are you doing?!'
    receiver = 'Apashanskiy@gmail.com'

    s.send_message(receiver, message)


if __name__ == '__main__':
    main()
