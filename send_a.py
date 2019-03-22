import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
try:   
	fromaddr = "cocoousha@gmail.com"
	toaddr = "ushakotha412@gmail.com"
	msg = MIMEMultipart()
	msg['from'] = fromaddr 
	msg['To'] = toaddr   
	msg['Subject'] = "python files"
	body = "refer to the above given attachement"
	msg.attach(MIMEText(body, 'plain'))  
	filename = "errordefine.py"
	attachment = open("/home/al310/python/errordefine.py", "rb") 
	p = MIMEBase('application', 'octet-stream') 
	p.set_payload((attachment).read())  
	encoders.encode_base64(p)    
	p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
	msg.attach(p) 
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls()  
	s.login(fromaddr, "vanaja412") 
	text = msg.as_string() 
	s.sendmail(fromaddr, toaddr, text) 
except:
	print('error')
else:
	print('msg sent')
s.quit()
	
