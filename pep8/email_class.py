import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Email:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def send_message(self, smtp_server, port, recipient_message, subject, message):
        message_object = MIMEMultipart()
        message_object['From'] = self.login
        message_object['To'] = ', '.join(recipient_message)
        message_object['Subject'] = subject
        message_object.attach(MIMEText(message))

        send_mail = smtplib.SMTP(smtp_server, port)
        send_mail.ehlo()
        send_mail.starttls()
        send_mail.ehlo()
        send_mail.login(self.login, self.password)

        results = send_mail.sendmail(self.login, send_mail, message_object.as_string())
        send_mail.quit()

        return results

    def receive(self, server, name_mail_box, header=None):
        receive_mail = imaplib.IMAP4_SSL(server)
        receive_mail.login(self.login, self.password)
        receive_mail.list()

        receive_mail.select(name_mail_box)
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = receive_mail.uid('search', header, criterion)

        assert data[0], 'There are no letters with current header'

        latest_email_uid = data[0].split()[-1]
        result, data = receive_mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]

        receive_email_message = email.message_from_string(raw_email)
        receive_mail.logout()

        return receive_email_message
