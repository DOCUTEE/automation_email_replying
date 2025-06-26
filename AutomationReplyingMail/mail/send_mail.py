from email.message import EmailMessage
from smtplib import SMTP_SSL


def send_email_to(smtp: SMTP_SSL, sender_email,receiver_email,subject,content):
    mail = EmailMessage()
    mail['Subject'] = subject
    mail['From'] = sender_email
    mail['To'] = receiver_email
    mail.set_content(content)    
    smtp.send_message(mail)


