import os
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta

BACKUP_LOG = "C:/Backup/last_backup.txt"  # update path
TIME_LIMIT = datetime.now() - timedelta(days=1)

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

if os.path.exists(BACKUP_LOG):
    with open(BACKUP_LOG, 'r') as f:
        last_backup = datetime.fromisoformat(f.read().strip())
    if last_backup < TIME_LIMIT:
        message = "🚨 Backup Failure: No successful backup in last 24 hours"
        print(message)
        send_email("Backup Status Alert", message)
else:
    message = "🚨 Backup Log Missing: Backup may not be running"
    print(message)
    send_email("Backup Status Alert", message)
