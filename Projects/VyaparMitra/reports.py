import csv
import os
from datetime import datetime

from database import run_query


def row_generator(rows):
    for row in rows:
        yield row


def sales_report():
    """Display sales grouped by date."""

    query = """
        SELECT
            DATE(sale_date) AS sale_day,
            COUNT(*) AS bills,
            COALESCE(SUM(subtotal), 0) AS subtotal,
            COALESCE(SUM(discount), 0) AS discounts,
            COALESCE(SUM(total), 0) AS revenue
        FROM sales
        GROUP BY DATE(sale_date)
        ORDER BY sale_day DESC
    """

    rows = run_query(query, fetch=True)

    print("\n" + "=" * 85)
    print("                         VYAPARMITRA - SALES REPORT")
    print("=" * 85)

    if rows is None:
        print("Could not retrieve sales records. Check your database.")
        return

    if not rows:
        print("No actual sales records were found in the sales table.")
        print("Activity log entries are not sales records.")
        print("=" * 85)
        return

    print(
        f"{'Date':<15}"
        f"{'Bills':>8}"
        f"{'Subtotal (Rs.)':>20}"
        f"{'Discount (Rs.)':>20}"
        f"{'Revenue (Rs.)':>20}"
    )

    print("-" * 85)

    for row in row_generator(rows):
        print(
            f"{str(row['sale_day']):<15}"
            f"{row['bills']:>8}"
            f"{float(row['subtotal']):>20.2f}"
            f"{float(row['discounts']):>20.2f}"
            f"{float(row['revenue']):>20.2f}"
        )

    print("=" * 85)


def profit_report():
    """Display estimated product-wise gross profit."""

    query = """
        SELECT
            si.product_id,
            p.name,
            SUM(si.quantity) AS units_sold,
            SUM(si.line_total) AS sales_value,
            SUM(si.quantity * si.unit_cost) AS cost_value,
            SUM(
                si.line_total - (si.quantity * si.unit_cost)
            ) AS gross_profit
        FROM sale_items AS si
        INNER JOIN products AS p
            ON p.product_id = si.product_id
        GROUP BY si.product_id, p.name
        ORDER BY gross_profit DESC
    """

    rows = run_query(query, fetch=True)

    print("\n" + "=" * 95)
    print("                    VYAPARMITRA - PRODUCT-WISE GROSS PROFIT")
    print("=" * 95)

    if rows is None:
        print("Could not retrieve profit data. Check your database.")
        return

    if not rows:
        print("No sold product items were found in the sale_items table.")
        print("=" * 95)
        return

    print(
        f"{'Product':<25}"
        f"{'Units':>9}"
        f"{'Sales (Rs.)':>20}"
        f"{'Cost (Rs.)':>20}"
        f"{'Profit (Rs.)':>20}"
    )

    print("-" * 95)

    for row in rows:
        print(
            f"{str(row['name']):<25.25}"
            f"{row['units_sold']:>9}"
            f"{float(row['sales_value']):>20.2f}"
            f"{float(row['cost_value']):>20.2f}"
            f"{float(row['gross_profit']):>20.2f}"
        )

    print("=" * 95)
    print("Gross profit is calculated using recorded selling prices and item costs.")


def export_sales_report():
    """Export actual sales-table records to a CSV file."""

    query = """
        SELECT
            sale_id,
            sale_date,
            subtotal,
            discount,
            total
        FROM sales
        ORDER BY sale_id DESC
    """

    rows = run_query(query, fetch=True)

    if rows is None:
        print("Could not retrieve sales records. Export cancelled.")
        return

    os.makedirs("logs", exist_ok=True)

    filename = os.path.join(
        "logs",
        f"sales_report_{datetime.now():%Y%m%d_%H%M%S}.csv"
    )

    fieldnames = [
        "sale_id",
        "sale_date",
        "subtotal",
        "discount",
        "total"
    ]

    try:
        with open(
            filename,
            mode="w",
            newline="",
            encoding="utf-8-sig"
        ) as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for row in rows:
                writer.writerow({
                    "sale_id": row["sale_id"],
                    "sale_date": row["sale_date"],
                    "subtotal": row["subtotal"],
                    "discount": row["discount"],
                    "total": row["total"]
                })

        print("\n" + "=" * 60)
        print("              SALES CSV EXPORT")
        print("=" * 60)
        print(f"File location: {os.path.abspath(filename)}")
        print(f"Sales records exported: {len(rows)}")

        if not rows:
            print(
                "The CSV contains only column headings because "
                "the sales table returned no records."
            )
        else:
            print("Sales data exported successfully.")

        print("=" * 60)

    except (OSError, csv.Error, KeyError) as error:
        print(f"CSV export failed: {error}")