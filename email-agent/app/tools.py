import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv()

GMAIL_ADDRESS = os.getenv("GMAIL_ADDRESS")
GMAIL_PASSWORD = os.getenv("GMAIL_APP_PASSWORD")

def send_email(to: str, subject: str, body: str) -> str:
    if not GMAIL_ADDRESS:
        raise ValueError("GMAIL_ADDRESS is not configured")

    if not GMAIL_PASSWORD:
        raise ValueError("GMAIL_APP_PASSWORD is not configured")

    #Create email
    message = EmailMessage()

    message["From"] = GMAIL_ADDRESS
    message["To"] = to
    message["Subject"] = subject

    message.set_content(body)

    #Connect to Gmail SMTP
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:

        # Upgrade connection to TLS
        smtp.starttls()

        # Authenticate
        smtp.login(GMAIL_ADDRESS, GMAIL_PASSWORD)

        # Send email
        smtp.send_message(message)
    return f"Email send successfully to {to}"