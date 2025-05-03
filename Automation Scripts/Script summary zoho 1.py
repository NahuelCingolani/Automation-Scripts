import pandas as pd
from bs4 import BeautifulSoup

# Function to clean HTML content using BeautifulSoup
def clean_html_text(html):
    if isinstance(html, str):  # Ensure the input is a string
        soup = BeautifulSoup(html, 'html.parser')
        return soup.get_text(separator="\n").strip()
    return html  # Return as-is if not a string

# Load the Excel file
file_path = 'C:/Users/your_user/Downloads/TicketsZohoComments.xlsx'  # Update this with your actual file path
data = pd.read_excel(file_path)

# Clean the 'summary' column if it exists
if 'summary' in data.columns:
    data['summary'] = data['summary'].apply(clean_html_text)

# Save the cleaned data to a new Excel file
output_path = 'C:/Users/your_user/Downloads/cleaned_file.xlsx'  # Update this with your desired output path
data.to_excel(output_path, index=False)

print(f"Cleaned file saved to: {output_path}")
