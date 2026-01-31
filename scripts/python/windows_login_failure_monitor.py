import win32evtlog
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta

TIME_WINDOW = datetime.now() - timedelta(minutes=10)

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

server = 'localhost'
log_type = 'Security'
hand = win32evtlog.OpenEventLog(server, log_type)
flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
total = 0

events = True
while events:
    events = win32evtlog.ReadEventLog(hand, flags, 0)
    if events:
        for ev_obj in events:
            if ev_obj.EventID == 4625 and ev_obj.TimeGenerated > TIME_WINDOW:
                total += 1

if total > 5:
    message = f"🚨 Security Alert: {total} failed login attempts detected"
    print(message)
    send_email("Login Failure Alert", message)
    print("Alert email sent.")
else:
    print(f"Login attempts are normal: {total} failed attempts in the last 10 minutes") 