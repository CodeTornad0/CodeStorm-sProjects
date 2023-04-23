import smtplib, ssl
from email.message import EmailMessage
subject = "Email From Python"
body = "This is a test email from Python! Hi sjajajrj! AJ"
senderEmail = "dumbcodingstuff@gmail.com"
receiverEmail = "dumbcodingstuff@gmail.com"
password = input("Enter a password: ")
message = EmailMessage()
message["From"] = senderEmail
message["To"] = receiverEmail
message["Subject"] = subject
html = f"""
<html>
    <body>
        <h1>{subject}</h1>
        <p>{body}</p>
    </body>
</html>
"""
message.add_alternative(html, subtype="html")
context = ssl.create_default_context()
print("Sending Email!")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(senderEmail, password)
    server.sendmail(senderEmail, receiverEmail, message.as_string())
print("Success")