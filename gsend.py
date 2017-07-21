import smtplib

def send(mymsg):
	fromaddr = 'xxx@gmail.com'
	toaddrs  = 'xxx@gmail.com'
	username = 'xxx@gmail.com'
	password = 'xxxyyyyzzzz'
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(username,password)
	msg = "\r\n".join([
  "From: xxx@gmail.com",
  "To: xxx@gmail.com",
  "Subject: Twitter Ripper Bot",
  "",
  "%s" % mymsg
  ])
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()
