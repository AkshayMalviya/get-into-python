import smtplib

sender = 'akshay.malviya@XXXXXXX.com'
receivers = ['aayush.jain@XXXXXXX.com']

message = """From: From Person <akshay.malviya@XXXXXXX.com>
To: To Person <aayush.jain@XXXXXXX.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('192.168.0.0',25,'localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except Exception:
   print ("Error: unable to send email")