from twilio.rest import Client
account_sid = 'AC0b5d6c1327a51949d6526de658c29380'
auth_token = 'ad038cd2758aa18e8bb5b7323ead1c7f'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     from_='whatsapp:+19708185942',
                     body='Your appointment is coming up on July 21 at 3PM',
                     to='whatsapp:+919130264614'
                 )

print(message.sid)