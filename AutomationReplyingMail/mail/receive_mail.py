from imaplib import IMAP4_SSL
import email
from email.header  import decode_header

def receive_mail_from_user(imap: IMAP4_SSL, sender_email):
    query = f'(UNSEEN FROM "{sender_email}")'
    status, messages = imap.search(None, query)
    
    mail_ids = messages[0].split()

    emails = []
    for mail_id in mail_ids:
        status, message_data = imap.fetch(mail_id, "(RFC822)")
        if status != "OK":
            print(f"Could not fetch email ID {mail_id}")
            continue
        
        raw_email = message_data[0][1]
        mail = email.message_from_bytes(raw_email)

        # Decode subject
        subject, encoding = decode_header(mail["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding or "utf-8", errors="ignore")

        content = ''

        # Get plain text body
        body = ""
        if mail.is_multipart():
            for part in mail.walk():
                if part.get_content_type() == "text/plain" and "attachment" not in str(part.get("Content-Disposition", "")):
                    try:
                        body = part.get_payload(decode=True).decode(errors="ignore")
                        break
                    except:
                        body = "(❗ Could not decode body)"
        else:
            try:
                body = mail.get_payload(decode=True).decode(errors="ignore")
            except:
                body = "(Could not decode body)"
        
        emails.append(
            {
                "subject": subject,
                "content": body.strip()
            }
        )

    return emails