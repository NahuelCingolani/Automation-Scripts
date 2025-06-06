import csv
import glob
import os

def analyze_multiple_files(folder_path):
    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
    global_total = 0
    category_totals = {}

    for file in csv_files:
        with open(file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    amount = int(row["Amount"])
                    category = row["Category"]
                    global_total += amount

                    if category in category_totals:
                        category_totals[category] += amount
                    else:
                        category_totals[category] = amount

                except Exception as e:
                    print(f"Error in file {file}: {e}")

    # Generate summary file
    summary_path = os.path.join(folder_path, "summary_report.txt")
    with open(summary_path, "w") as summary:
        summary.write(f"Total sales (all files): ${global_total}\n\n")
        summary.write("Sales by category:\n")
        for category, total in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
            percentage = (total / global_total) * 100
            summary.write(f"  {category}: ${total} ({percentage:.2f}%)\n")

    print(f"Summary generated at: {summary_path}")

# Run analysis
analyze_multiple_files("C:/Path/To/Your/Folder/with_csv_files")
