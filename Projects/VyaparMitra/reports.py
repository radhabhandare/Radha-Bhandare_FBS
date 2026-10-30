import csv
import os
from database import run_query
from operations import print_table
def sales_report():
    rows = run_query(
        """
        SELECT sale_id, subtotal, discount, total, created_at
        FROM sales
        WHERE DATE(created_at) = CURDATE()
        ORDER BY sale_id
        """,
        fetchall=True,
    )

    print("\n--- TODAY'S SALES REPORT ---")

    if rows is None:
        print("Could not retrieve the sales report.")
        return

    if not rows:
        print("No sales recorded today.")
        return

    table_rows = []
    total_sales = 0.0

    for row in rows:
        total_sales += float(row["total"])

        table_rows.append([
            row["sale_id"],
            f'{float(row["subtotal"]):.2f}',
            f'{float(row["discount"]):.2f}',
            f'{float(row["total"]):.2f}',
            row["created_at"].strftime("%Y-%m-%d %H:%M:%S"),
        ])

    print_table(
        ["Bill ID", "Subtotal (Rs.)", "Discount (Rs.)",
         "Total (Rs.)", "Date and time"],
        table_rows,
    )

    print(f"\nNumber of bills: {len(rows)}")
    print(f"Total sales today: Rs. {total_sales:.2f}")


def export_sales_csv():
    rows = run_query(
        """
        SELECT sale_id, created_at, customer_id,
               subtotal, discount, total
        FROM sales
        ORDER BY created_at, sale_id
        """,
        fetchall=True,
    )

    if rows is None:
        print("Could not retrieve sales for export.")
        return

    os.makedirs("exports", exist_ok=True)
    path = os.path.join("exports", "sales.csv")

    headers = [
        "Bill ID",
        "Date and Time",
        "Customer ID",
        "Subtotal",
        "Discount",
        "Total",
    ]

    with open(path, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for row in rows:
            writer.writerow([
                row["sale_id"],
                row["created_at"].strftime("%Y-%m-%d %H:%M:%S"),
                row["customer_id"] if row["customer_id"] is not None else "",
                f'{float(row["subtotal"]):.2f}',
                f'{float(row["discount"]):.2f}',
                f'{float(row["total"]):.2f}',
            ])

    print(f"Sales CSV exported successfully: {path}")
    print(f"Records exported: {len(rows)}")
