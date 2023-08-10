# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['AC21de4d14551de24b359aa63385103704']
auth_token = os.environ['62c4c7e811c28848c28520583fe96d96']
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+18148697158',
         to='+15875329229'
     )

print(message.sid)
