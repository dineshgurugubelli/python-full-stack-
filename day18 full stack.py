'''#sigi lxae ldrq gwgr

import smtplib
#import ssl
from email.message import EmailMessage
sender = "dineshdinu3026@gmail.com"
passkey = "sigilxaeldrqgwgr"
receiver = "manojsai2710@gmail.com"
message = EmailMessage()
message["from"]=sender
message["to"]=receiver
message["subject"]= "welcome to inbox"
message.set_content("have a look on me")
#context = ssl.create_default_context()
try:
    smtp=smtplib.SMTP("smtp.gamil.com",port=587)
    #smtp.ehlo()
    smtp.starttls()
    #smtp.ehlo()
    smtp.login(sender,passkey)
    smtp.send_message(message)
    print("12345678")
except Exception as e:
    print("Error:",e)
finally:
    smtp.quit()

 SMTP Module
email.message
'''
import smtplib
import ssl
from email.message import EmailMessage
sender_email ="dineshdinu3026@gmail.com"
password="sigilxaeldrqgwgr"

receiver_email ="bankabhanu29@gmail.com"
message = EmailMessage()
message["From"]=sender_email
message["To"]=receiver_email
message["Subject"]="Welcome Mail"
message.set_content(" knsknsk10")

context = ssl.create_default_context()

with smtplib.SMTP("smtp.gmail.com",port=587)as smtp:
    smtp.ehlo()
    smtp.starttls(context=context)
    smtp.ehlo()
    smtp.login(sender_email,password)
    smtp.send_message(message)

    
