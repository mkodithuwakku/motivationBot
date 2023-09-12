import random
import time
from twilio.rest import Client

# Your Twilio Account SID and Auth Token
account_sid = 'AC45bb309f20425417b2f45166e56af60b'
auth_token = '62c4c7e811c28848c28520583fe96d96'

# Your Twilio phone number and the recipient's phone number
twilio_phone_number = '+18148697158'
recipient_phone_number = '+15875329229'

# List of random messages
random_messages = [
    'The more you do, the less you wait',
    'Hey, blow out the candles, make a wish, what is a life if you never take a risk? Aint a place to far aint a dream too big',
    'You make your mistakes, your mistakes never make you',
    'It aint your money till you make it, till then its just a conversation',
    'You miss every shot you dont take',
]

# Function to send a random message
def send_random_message():
    client = Client(account_sid, auth_token)
    message = random.choice(random_messages)
    client.messages.create(
        body=message,
        from_=twilio_phone_number,
        to=recipient_phone_number
    )
    print(f"Message sent: '{message}'")

# Main loop to send messages at random times
while True:
    send_random_message()
    # Sleep for a random time between 4 to 6 hours 
    sleep_time = random.randint(14400, 21600)
    print(f"Next message will be sent in {sleep_time} seconds...")
    time.sleep(sleep_time)
