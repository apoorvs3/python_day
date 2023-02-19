from twilio.rest import Client

account_sid = 'ACfe31166cf23c89f3cc55d6af4d24ee63'
auth_token = '64eeaa31b27ee9e3439e2796470afd38'
client = Client(account_sid, auth_token)


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, msg_body):
        message = client.messages \
            .create(
            body=msg_body,
            from_='+16507191660',
            to='+918840981096'
        )
        print(message.status)
