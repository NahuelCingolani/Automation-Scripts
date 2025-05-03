import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from tqdm import tqdm  # Progress bar

# 🛠 Zoho Desk Configuration
AUTH_TOKEN = "Bearer your_access_token_here"  # Make sure to include "Bearer" at the start
BASE_URL = "https://desk.zoho.com/api/v1/tickets"  # Base URL for ticket data

# Input and output Excel files
INPUT_FILE = r"path_to_input_file.xlsx"  # Excel file with Ticket IDs
OUTPUT_FILE = r"path_to_output_file_cleaned.xlsx"  # Output file to store cleaned data

# Read the Excel file with Ticket IDs as strings
tickets_df = pd.read_excel(INPUT_FILE, dtype={"TicketId": str})

# Function to clean the email content
def clean_content(content):
    if not content or content == "N/A":
        return "N/A"

    # Remove HTML tags using BeautifulSoup
    soup = BeautifulSoup(content, "html.parser")
    text = soup.get_text()

    # Remove control characters and extra whitespace
    text = re.sub(r"\s+", " ", text).strip()

    # Optional: Remove signatures or irrelevant phrases
    text = re.sub(r"(Sent from my iPhone|Este mensaje fue enviado desde|Atte\.)", "", text, flags=re.IGNORECASE)

    # Optional: Limit content length if necessary
    return text[:5000]  # Trim to 5000 characters if too long

# List to store final results
results = []

# Iterate through each Ticket ID using tqdm for progress display
for index, row in tqdm(tickets_df.iterrows(), total=tickets_df.shape[0], desc="Processing tickets"):
    ticket_id = row["TicketId"]  # Read ID from column "TicketId"

    # Get ticket threads
    threads_url = f"{BASE_URL}/{ticket_id}/threads"
    headers = {
        "Authorization": AUTH_TOKEN
    }
    threads_response = requests.get(threads_url, headers=headers)

    if threads_response.status_code == 200:
        threads_data = threads_response.json().get("data", [])

        # Process each thread to get email content
        for thread in threads_data:
            thread_id = thread.get("id", "N/A")
            thread_created_time = thread.get("createdTime", "N/A")

            # Fetch the full thread content
            thread_content_url = f"{BASE_URL}/{ticket_id}/threads/{thread_id}"
            thread_content_response = requests.get(thread_content_url, headers=headers)

            if thread_content_response.status_code == 200:
                thread_json = thread_content_response.json()
                raw_content = thread_json.get("content", "N/A")
                cleaned_content = clean_content(raw_content)
            else:
                print(f"❌ Error retrieving thread content {thread_id}: {thread_content_response.status_code}")
                cleaned_content = "N/A"

            # Append processed data
            results.append({
                "TicketId": ticket_id,
                "Subject": row.get("Subject", "N/A"),
                "ThreadId": thread_id,
                "Created Time": thread_created_time,
                "Thread Content (Cleaned)": cleaned_content
            })
    else:
        print(
            f"❌ Error retrieving threads for Ticket ID {ticket_id}: {threads_response.status_code} - {threads_response.text}"
        )

# Create DataFrame from results
output_df = pd.DataFrame(results)
output_df["TicketId"] = output_df["TicketId"].astype(str)

# Save DataFrame to Excel
output_df.to_excel(OUTPUT_FILE, index=False)

# Adjust column widths in the Excel file
wb = load_workbook(OUTPUT_FILE)
ws = wb.active

column_widths = {
    "A": 15,   # TicketId
    "B": 30,   # Subject
    "C": 20,   # ThreadId
    "D": 20,   # Created Time
    "E": 150   # Thread Content (Cleaned)
}

for col, width in column_widths.items():
    ws.column_dimensions[col].width = width

# Save the final formatted Excel file
wb.save(OUTPUT_FILE)

print(f"✅ Process completed. Results saved in '{OUTPUT_FILE}' with cleaned content.")






