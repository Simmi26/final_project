import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
 
smtp_server = "smtp.gmail.com"
smtp_port = 587                                
from_address = "simranjain24941@gmail.com"         
from_password = "simmi9214924941" 
to_address = "missnehasharmaa@gmail.com"        
subject = "personal mail"               
mail_body = "someone is attaching usb"
attachment_1 = r"/home/user/simran/usb.txt"       
attachment_2 = r"/home/user/Desktop/faces/user/1.jpg"
 
msg = MIMEMultipart()
msg['Subject'] =  subject
msg['To'] = to_address
msg.attach(MIMEText(mail_body))
 
files = []
files.append(attachment_1)
files.append(attachment_2)
for file in files:
    part = MIMEBase('application', "octet-stream")
    part.set_payload(open(file, "rb").read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(file)))
    msg.attach(part)
 
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(from_address, from_password)
server.sendmail(from_address, to_address, msg.as_string())
server.quit()

