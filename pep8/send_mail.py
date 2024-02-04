from email_class import Email

if __name__ == '__main__':

    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    login_gmail = 'login@gmail.com'
    password = 'qwerty'

    subject = 'Subject'
    recipient_message = ['vasya@email.com', 'petya@email.com']
    body_message = 'Message'
    header = None
    mail_box = 'inbox'

    gmail = Email(login_gmail, password)

    print(gmail.send_message(
        GMAIL_SMTP,
        587,
        recipient_message,
        subject,
        body_message
    ))

    print(gmail.receive(GMAIL_IMAP, mail_box))
