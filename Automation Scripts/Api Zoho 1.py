import requests
from urllib.parse import urlencode, parse_qs, urlparse

# Configuration
CLIENT_ID = 'your_client_id'  # Replace with your Zoho Client ID
CLIENT_SECRET = 'your_client_secret'  # Replace with your Zoho Client Secret
REDIRECT_URI = 'http://localhost/callback'  # Must match what's registered in Zoho
AUTHORIZATION_URL = 'https://accounts.zoho.com/oauth/v2/auth'
TOKEN_URL = 'https://accounts.zoho.com/oauth/v2/token'
API_URL = 'https://desk.zoho.com/api/v1/tickets'
ORG_ID = 'your_organization_id'  # Replace with your Zoho Desk organization ID
SCOPE = 'ZohoDesk.tickets.ALL,ZohoDesk.basic.READ'  # Adjust scopes as needed
ACCESS_TYPE = 'offline'  # To obtain a refresh token
STATE = 'random_state_value'  # Optional, for extra security

# Step 1: Generate the authorization URL
def get_authorization_url():
    params = {
        'scope': SCOPE,
        'client_id': CLIENT_ID,
        'response_type': 'code',
        'redirect_uri': REDIRECT_URI,
        'access_type': ACCESS_TYPE,
        'state': STATE,
    }
    url = f"{AUTHORIZATION_URL}?{urlencode(params)}"
    return url

# Step 2: Exchange the code for an access token
def get_access_token(auth_code):
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
        'code': auth_code,
        'grant_type': 'authorization_code',
    }
    response = requests.post(TOKEN_URL, data=data)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error retrieving the access token:", response.status_code, response.text)
        return None

# Step 3: Make API requests to Zoho Desk
def get_tickets(access_token):
    headers = {
        'Authorization': f'Zoho-oauthtoken {access_token}',
        'orgId': ORG_ID
    }
    response = requests.get(API_URL, headers=headers)
    if response.status_code == 200:
        return response.json().get("data", [])  # Return the list of tickets
    else:
        print("Error retrieving tickets:", response.status_code, response.text)
        return None

# Simulate redirect_uri for capturing the 'code' parameter (for local testing)
def simulate_redirect_uri():
    # Simulates a redirected URL with the "code" parameter
    redirected_url = input("Paste the redirected URL here (from your browser): ")
    parsed_url = urlparse(redirected_url)
    query_params = parse_qs(parsed_url.query)
    auth_code = query_params.get('code', [None])[0]
    return auth_code

# Start the flow
if __name__ == "__main__":
    print("1. Go to the following URL to get the authorization code:")
    print(get_authorization_url())
    print("\n2. Once you accept, you'll be redirected to the redirect_uri.")
    print("   Copy and paste the redirected URL here.")
    auth_code = simulate_redirect_uri()

    if auth_code:
        print(f"Authorization code obtained: {auth_code}")
        print("3. Exchanging authorization code for tokens...")
        token_response = get_access_token(auth_code)
        if token_response:
            print(f"Access Token: {token_response.get('access_token')}")
            print(f"Refresh Token: {token_response.get('refresh_token')}")
        else:
            print("Failed to obtain tokens.")
    else:
        print("Authorization code was not obtained.")



