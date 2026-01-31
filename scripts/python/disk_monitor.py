import psutil
import smtplib
from email.mime.text import MIMEText

DISK_THRESHOLD = 15  # % free

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

for partition in psutil.disk_partitions():
    usage = psutil.disk_usage(partition.mountpoint)
    free_percent = 100 - usage.percent
    if free_percent < DISK_THRESHOLD:
        message = f"🚨 Low Disk Space Alert: {partition.device} {free_percent:.2f}% free"
        print(message)
        send_email("Low Disk Space Alert", message)
        print("Alert email sent.")
    else:
        print(f"Disk space is normal on {partition.device}: {free_percent:.2f}% free")      