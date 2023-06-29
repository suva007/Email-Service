from email.message import EmailMessage
import ssl
import smtplib

def send_email (to_email: str, subject: str, text: str):
    # Set up the email's recipient, sender, and subject
    # to_email = 'suvansharora07@gmail.com'
    from_email = 'noreply.taskscheduler@gmail.com'
    email_password = '*************'

    # Create the email message
    message = 'Subject: {0}\n\n{1}'.format(subject, text)

    # Connect to the Gmail server
    email = EmailMessage()
    email['From'] =  from_email
    email['To'] = to_email
    email['Subject'] = subject
    email.set_content(text)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(from_email, email_password)
        smtp.sendmail(from_email, to_email, email.as_string())
