import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# НЕЗАКОНЧЕНО!


def main():
    fromaddr = 'kfu.anatomy.2018@gmail.com'
    toaddr = 'apashanskiy@gmail.com'

    msg = MIMEMultipart()

    msg['To'] = toaddr
    msg['From'] = fromaddr
    msg['Subject'] = 'Instance subject of the Mail'

    body = 'That\s students performance report'

    msg.attach(MIMEText(body, 'plain'))

    filename = 'my_db.db'
    attachment = open(filename, 'rb')

    p = MIMEBase('application', 'octet-stream')


if __name__ == '__main__':
    main()
