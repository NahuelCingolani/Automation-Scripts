from twilio.rest import Client

# Configure your Twilio credentials
account_sid = 'your_account_sid_here'
auth_token = 'your_auth_token_here'
client = Client(account_sid, auth_token)

# List of phone numbers to send the WhatsApp message to
phone_numbers = [
    'whatsapp:+12345678901',
    # Add more numbers as needed
    # 'whatsapp:+19876543210',
    # 'whatsapp:+441234567890',
]

# Message body to be sent
message_body = (
    "Hello, this is an important notification from COMPANY.\n\n"
    "Your company has pending offers in open quotation processes.\n\n"
    "Please log in to the COMPANY portal to submit your offer and avoid missing business opportunities.\n\n"
    "More details were sent to your email.\n\n"
    "If you need help, contact us at support@email\n\n"
    "If you have already submitted your offers, you can ignore this message.\n\n"
    "Thank you."
)

# Send the message to each number in the list
for number in phone_numbers:
    message = client.messages.create(
        from_='whatsapp:+14155238886',  # This is Twilio’s sandbox number for WhatsApp
        body=message_body,
        to=number
    )
    print(f"Message sent to {number} with SID: {message.sid}")
