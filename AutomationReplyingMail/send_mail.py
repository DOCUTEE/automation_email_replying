from mail.send_mail import send_email_to
import smtplib

EMAIL = "quangforwork1203@gmail.com"
APP_PASSWORD = "spqc krdl uqdc mavn"
RECEIVER = "phuongnganhbt25@gmail.com"



def send_mail(subject, content):
    try:
        smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        smtp.login(EMAIL,APP_PASSWORD)
        send_email_to(
            smtp,
            sender_email=EMAIL,
            receiver_email=RECEIVER,
            subject=subject,
            content=content
        )
        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email.", e)

if __name__ == "__main__":
    subject = "Hello"
    content = "Test"
    send_mail(subject, content)
