import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email_address = ""
email_password = ""

smtp_server = "smtp-mail.outlook.com"
smtp_port = 587
sender_email = email_address
recipient_email = ""
subject = "HTML Email Example"

html_content = """

"""

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = recipient_email
msg['Subject'] = subject

msg.attach(MIMEText(html_content, 'html'))

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(email_address, email_password)


    server.sendmail(sender_email, recipient_email, msg.as_string())

    print("HTML Email sent successfully!")

except Exception as e:
    print("Error sending HTML email:", str(e))

finally:
    server.quit()