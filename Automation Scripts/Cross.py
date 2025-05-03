import pandas as pd

# File paths
file1_path = r"path_to_first_file.xlsx"
file2_path = r"path_to_second_file.xlsx"
output_path = r"path_to_output_file.xlsx"

# Load Excel files
df1 = pd.read_excel(file1_path, engine='openpyxl')
df2 = pd.read_excel(file2_path, engine='openpyxl')

# Check column names
print("Columns in the first file:", df1.columns)
print("Columns in the second file:", df2.columns)

# Normalize column names to avoid errors due to spaces or casing
df1.columns = df1.columns.str.strip()
df2.columns = df2.columns.str.strip()

# Ensure "Contacto Reference Id" exists in both files
if "Contacto Reference Id" in df1.columns and "Contacto Reference Id" in df2.columns:
    df1["Contacto Reference Id"] = df1["Contacto Reference Id"].astype(str)
    df2["Contacto Reference Id"] = df2["Contacto Reference Id"].astype(str)
else:
    print("Warning: 'Contacto Reference Id' not found in one of the files.")

# Ensure TicketId is treated as string
df1["TicketId"] = df1["TicketId"].astype(str)
df2["TicketId"] = df2["TicketId"].astype(str)

# Add apostrophe to force Excel to treat TicketId as text
df1["TicketId"] = df1["TicketId"].apply(lambda x: "'" + x)
df2["TicketId"] = df2["TicketId"].apply(lambda x: "'" + x)

# Merge both DataFrames on TicketId
merged_df = pd.merge(df1, df2, on='TicketId', how='inner')

# Save the resulting file
with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
    merged_df.to_excel(writer, index=False)

print(f"✅ Combined file saved at: {output_path}")


