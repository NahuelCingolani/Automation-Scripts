import requests

# === 1. Authorization Code Grant ===
# Exchange authorization code for access and refresh tokens
url = "https://accounts.zoho.com/oauth/v2/token"

data = {
    "grant_type": "authorization_code",
    "client_id": "your_client_id",
    "client_secret": "your_client_secret",
    "redirect_uri": "http://localhost/callback",
    "code": "your_authorization_code"
}

response = requests.post(url, data=data)
print(response.json())  # This will display the Access Token and Refresh Token


# === 2. Retrieve Tickets Using Access Token ===
"""
import requests

url = "https://desk.zoho.com/api/v1/tickets"
headers = {
    "Authorization": "Bearer your_access_token",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
print(response.json())  # Should return the list of tickets
"""


# === 3. Refresh Access Token Using Refresh Token ===
"""
import requests

refresh_token = "your_refresh_token"
client_id = "your_client_id"
client_secret = "your_client_secret"

response = requests.post(
    "https://accounts.zoho.com/oauth/v2/token",
    data={
        "refresh_token": refresh_token,
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "refresh_token"
    }
)

tokens = response.json()

print(tokens)

if "api_domain" in tokens:
    api_domain = tokens["api_domain"]
    print(f"✅ API domain: {api_domain}")
else:
    print("❌ 'api_domain' not found in the response.")
"""


# === 4. Get Specific Ticket Details ===
"""
import requests

AUTH_TOKEN = "Bearer your_access_token"
BASE_URL = "https://www.zohoapis.com/desk/v1"

ticket_id = "your_ticket_id"

headers = {
    "Authorization": AUTH_TOKEN
}

response = requests.get(f"{BASE_URL}/tickets/{ticket_id}", headers=headers)

print("Response Code:", response.status_code)
print("Response Content:", response.json())
"""


# === 5. Safe Request with JSON Error Handling ===
"""
import requests

AUTH_TOKEN = "Bearer your_access_token"
TICKET_ID = "your_ticket_id"
BASE_URL = "https://desk.zoho.com/api/v1/tickets"

headers = {
    "Authorization": AUTH_TOKEN
}

response = requests.get(BASE_URL, headers=headers)

print("Response Code:", response.status_code)
print("Headers:", response.headers)

try:
    print("Response Content:", response.json())
except requests.exceptions.JSONDecodeError:
    print("❌ Error: Response is not valid JSON. Raw content:")
    print(response.text)
"""





