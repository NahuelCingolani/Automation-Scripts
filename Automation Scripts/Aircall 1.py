import requests
import pandas as pd
from flask import Flask, request, redirect

app = Flask(__name__)

# Credentials obtained from Aircall
client_id = 'your_client_id'
client_secret = 'your_client_secret'
redirect_uri = 'https://your-redirect-url.com/'

# Read the CSV file
file_path = r'C:\path\to\your\processed_rfq.csv'  # Adjust the path accordingly
df = pd.read_csv(file_path)

# Filter rows with valid phone numbers
filtered_df = df.dropna(subset=['Phone'])

# Step 1: Redirect user to Aircall for authorization
@app.route('/login')
def login():
    auth_url = f"https://api.aircall.io/v1/oauth/authorize?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}"
    return redirect(auth_url)

# Step 2: Handle redirect and obtain token
@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_url = "https://api.aircall.io/v1/oauth/token"
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': redirect_uri,
        'client_id': client_id,
        'client_secret': client_secret,
    }
    response = requests.post(token_url, data=data)
    token_info = response.json()
    access_token = token_info['access_token']
    
    # Make the calls
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    
    for index, row in filtered_df.iterrows():
        to_phone = row['Phone']
        message = row['Message']
        
        call_data = {
            "to": to_phone,
            "message": message
        }
        
        call_response = requests.post("https://api.aircall.io/v1/calls", headers=headers, json=call_data)
        print(f"Call made to {to_phone}, response: {call_response.json()}")
    
    return "Calls completed successfully"

if __name__ == '__main__':
    app.run(debug=True)
