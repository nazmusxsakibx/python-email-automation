import smtplib
from email.mime.text import MIMEText

test = "This is a super text"

sender = "xxxxx@xxxxx.com"
receiver = "xxxxx@xxxxx.com"
password = "xxxx xxxx xxxx xxxx"

msg = MIMEText(test)
msg["Subject"] = "Python Email Test"
msg["From"] = sender
msg["To"] = receiver

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, msg.as_string())

print("Email sent successfully!")