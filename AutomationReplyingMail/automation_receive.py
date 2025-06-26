import time
import receive_mail as rc
import os

TARGET_EMAIL = os.getenv("TARGET_EMAIL", "")
TIMEOUT = int(os.getenv("TIMEOUT", 10))  # Get timeout from environment variable or use default

def receive_email_automation():
    while True:
        print("Checking for new emails...")
        try:
            rc.receive_mail(TARGET_EMAIL)
        except Exception as e:
            print(f"Error receiving email: {e}")
        print(f"Sleeping for timeout period of {TIMEOUT} seconds...")
        time.sleep(TIMEOUT)  # Wait for the specified timeout before checking again

if __name__ == "__main__":
    print("Starting email automation...")
    receive_email_automation()