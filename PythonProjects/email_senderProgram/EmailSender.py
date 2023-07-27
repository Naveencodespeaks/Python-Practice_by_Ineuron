from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'sainaveen005@gmail.com'
email_password = 'bmefloybmsvqzgko'

email_reciver = 'fabovir800@24rumen.com'

subject = 'This is the first basic project of emailsender'

body = """ This the just a basic project of an emailsender using python code and this is my first basic project using python code"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_reciver
em['subject']= subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciver, em.as_string())


# to check this program is working or not, go to google search for ""temp mail""
# copy that mail and past in the email_reciver
# run the program

# you will se the email sendr, subject and body message over there