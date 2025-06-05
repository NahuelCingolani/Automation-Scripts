# 🔧 Automation Scripts Portfolio (Python)

This repository contains a series of Python scripts developed to automate data handling and platform integration tasks using APIs (e.g., Twilio, Zoho, Aircall), Excel files, and WhatsApp messaging.

## 📂 Script Overview
| File | Description | Libraries Used |
|------|-------------|----------------|
| `Script summary zoho 1.py` | Cleans and summarizes HTML content from Zoho tickets stored in Excel files. Outputs a cleaned version ready for analysis. | pandas, beautifulsoup4, openpyxl |
| `Twilio whatsapp test.py` | Sends WhatsApp messages via Twilio API for notification or reminder purposes. | twilio |
| `Script Aircall 1.py` | Interacts with the Aircall API to fetch and process call records, exporting them to Excel. | requests, pandas, openpyxl |
| `Api Zoho 1.py` | Connects to the Zoho Desk API to extract and structure ticket data or comments. | requests, json, pandas |
| `Cross.py` | Performs cross-referencing between multiple Excel files to reconcile or validate information. | pandas, openpyxl |
| `Script ordering.py` | Sorts and structures raw datasets into cleaned, organized Excel outputs for reporting purposes. | pandas, openpyxl |
| `Aircall test.py` | Testing script for Aircall API integration and data export validation. | requests, pandas |
| `ApiRequestNahuel 1.py` | Base template for handling authenticated API requests with headers. | requests, json |
| `import requests 1.py` | Initial script likely used to test HTTP request logic using the requests library. | requests |
| `Aircall 1.py` | This script is a Python-based web application using Flask that automates outbound voice calls via the Aircall API. | requests, pandas, flask |
| `Sales Analysis Python updated.py` | Analyzes product sales from a CSV file, calculating total sales, revenue by category (sorted), top-selling product, and exportable summary. | csv |

## ⚙️ Setup
To use these scripts, install the required libraries:
```bash
pip install pandas openpyxl beautifulsoup4 twilio requests
```

Modify each script with your credentials and file paths as needed.

---
For questions or contributions, feel free to open an issue or submit a pull request.
