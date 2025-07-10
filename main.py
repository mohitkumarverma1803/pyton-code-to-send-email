import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# senders email credentials
sender_email = "mohit7232001202@gmail.com"
app_password = "app_password"  # App Password, NOT your regular Gmail password

# Receiver's email
receiver_email = "mohitkumarverma1803@gmail.com"

# Email subject and body
subject = "Test Email from Python"
body = "Hello,\n\nThis is a test email sent using Python code"

# Create the email
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject

# Attach the body to the email
message.attach(MIMEText(body, 'plain'))

# Connect to Gmail's SMTP server and send the email
try:
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, app_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("✅ Email sent successfully!")
except Exception as e:
    print("❌ Failed to send email.")
    print("Error:", e)
