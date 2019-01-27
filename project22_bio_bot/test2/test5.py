import imaplib
import email

# ЧТЕНИЕ СООБЩЕНИЕ С ПОЧТЫ

def main():
    my_login = 'kfu.anatomy.2018@gmail.com'
    my_pwd = 'z31aedc170f8'
    imap_host = 'imap.gmail.com'

    imap = imaplib.IMAP4_SSL(imap_host)

    imap.login(my_login, my_pwd)

    imap.select('INBOX')

    rv, data = imap.search(None, 'ALL')

    num = data[0].split()

    for i in num:
        rv, data = imap.fetch(i, '(RFC822)')
        email_message = email.message_from_bytes(data[0][1])
        print('-------- '+ email_message['From'] + ' --------')
        print(email_message['Date'])
        print(email_message['Subject'])
        print('-------- End of message --------')

    imap.close()

if __name__ == '__main__':
    main()
