import smtplib
import date_time

my_email = "apoorv.python@gmail.com"
password = "JUSTdance@96"
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="apoorv.python@gmail.com",
#         msg="Subject:Hello\n\nThis is the body")


# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()
print(date_time.select_quote())
# Authentication
s.login(my_email, password)
# message to be sent
message = "Message_you_need_to_send"
# sending the mail
s.sendmail(my_email, "apoorv.python@yahoo.com", date_time.select_quote())
# terminating the session
s.quit()
