import requests
from requests.auth import HTTPBasicAuth

# Set your Aircall API credentials
api_id = 'Your_Aircall_API_ID'
api_token = 'Your_Aircall_API_Token'

# Authentication using Basic Auth
auth = HTTPBasicAuth(api_id, api_token)

# Phone number to call
phone_number = '+1234567890'  # Replace with the target number

# API endpoint URL for initiating a call
url = 'https://api.aircall.io/v1/calls'

# Request payload to start the call
data = {
    'number': phone_number,
    'from': '+10000000000',  # Replace with your Aircall number
    'audio_url': 'https://yourdomain.com/audio.mp3',  # Replace with a valid public audio URL
    'user_id': 'Your_User_ID'  # Replace with the user ID that will be assigned to the call
}

# Send the POST request to initiate the call
response = requests.post(url, auth=auth, json=data)

# Check the response
if response.status_code == 201:
    print('Call successfully initiated.')
else:
    print(f'Failed to initiate the call: {response.status_code}, {response.text}')

