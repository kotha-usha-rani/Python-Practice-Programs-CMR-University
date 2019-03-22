import smtplib
try:
	s=smtplib.SMTP('smtp.gmail.com',587)
	s.starttls()
	sender='cocoousha@gmail.com'
	receiver='ushakotha412@gmail.com'
	msg='hey'
	s.login(sender,"vanaja412")
	s.sendmail(sender,receiver,msg)
except:
	print('error')
else:
	print('msg sent')
s.quit()