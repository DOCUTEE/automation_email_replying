import imaplib
from mail.receive_mail import receive_mail_from_user
from mail.send_mail import send_email_to
import smtplib
import model
import model.model
import os

EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

def receive_mail(sender_email):
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(EMAIL, APP_PASSWORD)
    imap.select("inbox")  # Select the inbox folder
    mails = receive_mail_from_user(imap, sender_email)
    print(len(mails))
    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(EMAIL,APP_PASSWORD)
    for mail in mails:
        print(f"Subject: {mail['subject']}")
        print(f"Content: {mail['content']}")

        content_sending = model.model.replying_input("Replying this email: ",mail['content'])
        subject_sending = model.model.replying_input("Give the subject for this email. MUST be just 1 line. Only give me just name subject.",content_sending)
        subject_sending = subject_sending.replace("\n", " ").strip()
        send_email_to(
            smtp,
            sender_email=EMAIL,
            receiver_email=sender_email,
            subject=subject_sending,
            content=content_sending
        )
        print("Email sent successfully.")
    imap.logout()
    smtp.quit()

if __name__ == "__main__":
    sender_email = os.getenv("TARGET_EMAIL")
    receive_mail(sender_email)

