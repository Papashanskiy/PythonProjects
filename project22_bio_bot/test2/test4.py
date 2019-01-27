import imaplib
import pprint
import email


def main():
    imap_urnm = 'Kfu.anatomy.2018@gmail.com'
    imap_pwd = 'z31aedc170f8'
    imap_host = 'imap.gmail.com'

    imap = imaplib.IMAP4_SSL(imap_host)

    imap.login(imap_urnm, imap_pwd)

    imap.select('INBOX')

    rv, data = imap.search(None, 'ALL')

    print('--------------- pprint.pprint(data) ---------------')
    pprint.pprint(data)

    num = data[0].split()[-1]
    print('--------------- num = data[0].split()[0] ---------------\n', num)

    print('--------------- rv, data = imap.fetch(None, \'(RFC822)\') ---------------')
    rv, data = imap.fetch(num, '(RFC822)')

    email_string = data[0][1]

    print('--------------- pprint.pprint(result) ---------------')
    pprint.pprint(email_string.decode())

    email_message = email.message_from_bytes(email_string)

    print(email_message['Subject'])
    print(email_message['Date'])
    print(email_message['From'])

    imap.close()

if __name__ == '__main__':
    main()
