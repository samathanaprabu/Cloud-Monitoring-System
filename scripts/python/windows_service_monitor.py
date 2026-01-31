import psutil
import smtplib
from email.mime.text import MIMEText

SERVICES = ["W3SVC", "MSSQLSERVER"]  # Windows services to monitor

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

for service_name in SERVICES:
    try:
        service = psutil.win_service_get(service_name).as_dict()
        if service['status'] != 'running':
            message = f"🚨 Service Down Alert: {service_name} is not running"
            print(message)
            send_email("Service Down Alert", message)
    except Exception as e:
        print(f"Service {service_name} not found: {e}")
        message = f"🚨 Service Not Found Alert: {service_name} could not be found"  
        send_email("Service Not Found Alert", message)  