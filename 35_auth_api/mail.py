import smtplib

server =smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()
server.login('apoorv.linux.mail@gmail.com', 'JUSTdance@96')
server.sendmail('apoorv.linux.mail@gmail.com', 'apoorvlifeok@gmail.com', 'Some sample text')

