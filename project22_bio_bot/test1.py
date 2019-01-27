import imaplib
import sys
import email


EMAIL_ACCOUNT = 'kfu.anatomy.2018@gmail.com'
EMAIL_PSW = 'z31aedc170f8'


def process_mailbox(conn):
    rv, data = conn.search(None, 'ALL')
    if rv != 'OK':
        print('No message found!')
        return

    for num in data[0].split():
        rv, data = conn.fetch(num, '(RFC822)')
        if rv != 'OK':
            print('ERROR gating message', num)
            return

        msg = email.message_from_bytes(data[0][1])
        hdr = email.header.make_header(email.header.decode_header(msg['Subject']))
        subject = str(hdr)
        print(f'Message {num}: {subject}')
        print(f'Test of message: {msg}')
        print('Raw date: ', msg['Date'])



def main():
    conn = imaplib.IMAP4_SSL('imap.gmail.com')

    try:
        rv, data = conn.login(EMAIL_ACCOUNT, EMAIL_PSW)
    except imaplib.IMAP4.error:
        print('Login failed!!')
        return sys.exit(1)

    print(rv, data)

    rv, mailboxes = conn.list()
    if rv == 'OK':
        print('Mailboxes:')
        print(mailboxes)

    rv, data = conn.select('INBOX')
    if rv == "OK":
        print('processing mailbox...\n', rv)
        process_mailbox(conn)
        conn.close()
    else:
        print('ERROR: Unable to open mailbox ', rv)

    conn.logout()

if __name__ == '__main__':
    main()
