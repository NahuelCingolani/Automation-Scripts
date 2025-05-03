# 🔧 Automation Scripts Portfolio (Python)

This repository contains a series of Python scripts developed to automate data handling and platform integration tasks using APIs (e.g., Twilio, Zoho, Aircall), Excel files, and WhatsApp messaging.

## 📂 Script Overview
| File | Description | Libraries Used |
|------|-------------|----------------|
| `Script summary zoho.py` | Cleans and summarizes HTML content from Zoho tickets stored in Excel files. Outputs a cleaned version ready for analysis. | pandas, beautifulsoup4, openpyxl |
| `Twilio wpp prueba.py` | Sends WhatsApp messages via Twilio API for notification or reminder purposes. | twilio |
| `Script Aircall.py` | Interacts with the Aircall API to fetch and process call records, exporting them to Excel. | requests, pandas, openpyxl |
| `Api Zoho.py` | Connects to the Zoho Desk API to extract and structure ticket data or comments. | requests, json, pandas |
| `Cruce.py` | Performs cross-referencing between multiple Excel files to reconcile or validate information. | pandas, openpyxl |
| `Script ordenamiento.py` | Sorts and structures raw datasets into cleaned, organized Excel outputs for reporting purposes. | pandas, openpyxl |
| `Aircall prueba.py` | Testing script for Aircall API integration and data export validation. | requests, pandas |
| `ApiRequestNahuel.py` | Base template for handling authenticated API requests with headers. | requests, json |
| `import requests.py` | Initial script likely used to test HTTP request logic using the requests library. | requests |

## ⚙️ Setup
To use these scripts, install the required libraries:
```bash
pip install pandas openpyxl beautifulsoup4 twilio requests
```

Modify each script with your credentials and file paths as needed.

---
For questions or contributions, feel free to open an issue or submit a pull request.
