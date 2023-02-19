import os
from twilio.rest import Client

account_sid = 'ACfe31166cf23c89f3cc55d6af4d24ee63'
auth_token = '2f769db6d43ef22df3573a354e24fdb0'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
    from_='+16507191660',
    to='+918840981096'
)

print(message.status)
