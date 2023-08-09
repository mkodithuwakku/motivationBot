from twilio.rest import Client
accountSid = "AC45bb309f20425417b2f45166e56af60b"
accountToken = "5bf50255ee87356bdb5ea5b6935c3bcc"

client = new.client(accountSid, accountToken)

message = client.messages.create(
    messagingServiceSid = 'MG25da3c8338307f74082c5903bf0392d7', 
    body = 'Test'
    media_url = 'https://64.media.tumblr.com/10257a358c5c81c682d54fd431bf7af8/d88a932034cb7b97-af/s640x960/f245ce46266324f55a7c0fc1fa3e04e320df4fe3.jpg'
    to = '+15875329229'
)

print(message.sid)
