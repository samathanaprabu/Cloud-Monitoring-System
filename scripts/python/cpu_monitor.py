import psutil
import smtplib
from email.mime.text import MIMEText

CPU_THRESHOLD = 80

def send_email(subject, body):
    sender = "monitor@cloud.com"
    receiver = "admin@company.com"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP_SSL('smtp.office365.com', 465) as server:
        server.login(sender, 'YOUR_EMAIL_PASSWORD_OR_TOKEN')
        server.send_message(msg)

cpu = psutil.cpu_percent(interval=1)
if cpu > CPU_THRESHOLD:
    message = f"🚨 High CPU Usage Alert: {cpu}%"
    print(message)
    send_email("High CPU Usage Alert", message)
    print("Alert email sent.")
else:
    print(f"CPU usage is normal: {cpu}%")   
    