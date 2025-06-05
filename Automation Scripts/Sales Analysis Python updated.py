import csv

def analyze_sales(file_path):
    total_sales = 0
    sales_by_category = {}
    top_product = ("", 0)

    with open(file_path, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            amount = int(row["Amount"])
            category = row["Category"]
            product = row["Product"]

            total_sales += amount

            if category in sales_by_category:
                sales_by_category[category] += amount
            else:
                sales_by_category[category] = amount

            if amount > top_product[1]:
                top_product = (product, amount)

    sorted_categories = sorted(sales_by_category.items(), key=lambda x: x[1], reverse=True)

    # Console output
    print(f"Total Sales: ${total_sales}")
    print("\nSales by Category (sorted):")
    for category, total in sorted_categories:
        print(f"  {category}: ${total}")

    print("\nCategory Percentage Breakdown:")
    for category, total in sorted_categories:
        percentage = (total / total_sales) * 100
        print(f"  {category}: {percentage:.2f}%")

    print(f"\nTop-Selling Product: {top_product[0]} (${top_product[1]})")

    # Export to .txt file
    with open("sales_summary.txt", "w") as summary:
        summary.write(f"Total Sales: ${total_sales}\n\n")
        summary.write("Sales by Category (sorted):\n")
        for category, total in sorted_categories:
            summary.write(f"  {category}: ${total}\n")

        summary.write("\nCategory Percentage Breakdown:\n")
        for category, total in sorted_categories:
            percentage = (total / total_sales) * 100
            summary.write(f"  {category}: {percentage:.2f}%\n")

        summary.write(f"\nTop-Selling Product: {top_product[0]} (${top_product[1]})\n")

# Run the function with your CSV file path
analyze_sales("sales.csv")
