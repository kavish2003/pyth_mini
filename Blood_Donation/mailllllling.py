import smtplib
from email.mime.text import MIMEText
import register


body="My first Mail program from python"

#creteMIMEText class object with body text
msg=MIMEText(body)

#from which address the mail is sent
fromaddr="2021.kavish.punjabi@ves.ac.in"

# to which address the mail is sent
toaddr="2021.kavish.punjabi@ves.ac.in"

#store the address into msg object

msg['From']=fromaddr
msg['To']=toaddr
msg['subject']="Thank you for Registering"

#connect to gmail.com server using 587 port no.
server=smtplib.SMTP('smtp.gmail.com',587)

# starting TLS mode
server.starttls()
# logining into the mail
server.login(fromaddr,"9850834406@Kv")

server.send_message(msg)
print('Mail sent....')

server.quit()