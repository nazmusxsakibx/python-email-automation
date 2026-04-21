import smtplib
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

SENDER   = "xxxxxxxxxxxx"
PASSWORD = "xxxxxxxxxxx"
RECEIVERS = [
    "xxxxxxxxxx"    
]
ATTACHMENT = r"e:\CyberSecurity\Project\Python_Email_Automation_Documentation.pdf"            
SEND_TIME  = "12:00"                   

def send_email():
    print(f"Sending emails...")

    for receiver in RECEIVERS:
        try:
            
            msg = MIMEMultipart()
            msg["Subject"] = "Python Automated Email"
            msg["From"]    = SENDER
            msg["To"]      = receiver

            body = "This is a super text — sent automatically via Python!"
            msg.attach(MIMEText(body, "plain"))

            if os.path.exists(ATTACHMENT):
                with open(ATTACHMENT, "rb") as f:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(f.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename={os.path.basename(ATTACHMENT)}"
                    )
                    msg.attach(part)

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(SENDER, PASSWORD)
                server.sendmail(SENDER, receiver, msg.as_string())

            print(f"✅ Sent to {receiver}")

        except Exception as e:
            print(f"❌ Failed to send to {receiver}: {e}")

schedule.every().day.at(SEND_TIME).do(send_email)
print(f"Scheduler started! Emails will be sent daily at {SEND_TIME}")

while True:
    schedule.run_pending()
    time.sleep(60)