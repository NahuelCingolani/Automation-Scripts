import requests
import base64

# Aircall API credentials
API_ID = 'your_api_id'
API_TOKEN = 'your_api_token'
audio_url = 'https://your-audio-link.com/sample-audio.mp3'  # Replace with a valid public audio URL

# Function to make a call using Aircall API
def make_call(phone_number):
    url = 'https://api.aircall.io/v1'
    auth_string = f"{API_ID}:{API_TOKEN}"
    auth_encoded = base64.b64encode(auth_string.encode()).decode()
    
    headers = {
        'Authorization': f'Basic {auth_encoded}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        "to": phone_number,
        "from": "+123456789",  # Your Aircall registered number
        "user_id": "your_user_email@company.com",  # Aircall user identifier
        "direction": "outbound",
        "audio_url": audio_url  # URL of the audio message to play
    }
    
    response = requests.post(url, headers=headers, json=payload)
    
    # Output status and content for debugging
    print(f'Status Code: {response.status_code}')
    print(f'Response Content: {response.content}')
    
    return response.json()

# Make a test call
make_call("+12345678901")

