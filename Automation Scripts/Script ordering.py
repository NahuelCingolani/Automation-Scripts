import pandas as pd  # Using pandas for data processing

# Define input and output file paths
input_path = "C:/Users/your_user/Downloads/Cases__1.csv"
output_path = "C:/Users/your_user/Downloads/Cases__1_ordered.csv"

# Read the CSV file (comma-separated, first row as header)
df = pd.read_csv(input_path, encoding="utf-8", delimiter=",", low_memory=False)

# Skip the second row if it doesn't contain valid data
df_cleaned = df.iloc[1:].reset_index(drop=True)

# List of columns in the desired order
column_order = [
    "ID", "Department", "Contact ID", "Email", "Phone", "Subject", "Description", "Status", "Product ID", "Ticket Owner",
    "Created By", "Modified By", "Created Time", "Modified Time", "Request Id", "Resolution", "To Address",
    "Customer Response Time", "Number of Threads", "Account ID", "Due Date", "Priority", "Channel", "Category",
    "Sub Category", "Ticket Closed Time", "Is Escalated", "Classifications", "Status updated time", "Request reopen time",
    "Assigned time", "First assigned time", "Happiness Rating", "Agent Responded Time", "Number of Comments",
    "Time to Respond", "SLA Name", "SLA Violation Type", "Team Id", "Tags", "Ticket On Hold Time", "Sentiment",
    "Layout", "Language", "User Type", "Client", "Resolution Group", "Module", "Requirement", "Requester ID",
    "Nature", "Action", "Item Number", "Amount Paid", "Payment Date", "Related Invoices", "Currency", "Cataloger",
    "Child Ticket Count", "Chat Classification"
]

# Filter only existing columns in the original dataset
column_order = [col for col in column_order if col in df_cleaned.columns]

# Reorder the columns based on the defined structure
df_ordered = df_cleaned[column_order]

# Save the reordered file using semicolon as separator for consistent formatting
df_ordered.to_csv(output_path, index=False, encoding="utf-8", sep=";", quoting=1)

print(f"Ordered file saved to: {output_path}")



