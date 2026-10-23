from database import run_query
from threading import Thread
from datetime import datetime

def row_generator(rows):
    
    for row in rows:
        yield row

def sales_report():
    rows = run_query(
        """SELECT DATE(sale_date) AS sale_day, COUNT(*) AS bills,
                  SUM(subtotal) AS subtotal, SUM(discount) AS discounts, SUM(total) AS revenue
           FROM sales GROUP BY DATE(sale_date) ORDER BY sale_day DESC""",
        fetch=True
    )
    if not rows:
        print("No sales recorded yet.")
        return
    print("\nDate | Bills | Subtotal | Discount | Revenue")
    for row in row_generator(rows):
        print(f'{row["sale_day"]} | {row["bills"]} | ₹{row["subtotal"]} | ₹{row["discounts"]} | ₹{row["revenue"]}')

def profit_report():
    rows = run_query(
        """SELECT si.product_id, p.name,
                  SUM(si.quantity) AS units_sold,
                  SUM(si.line_total) AS sales_value,
                  SUM(si.quantity * si.unit_cost) AS cost_value,
                  SUM(si.line_total - si.quantity * si.unit_cost) AS gross_profit
           FROM sale_items si JOIN products p ON p.product_id=si.product_id
           GROUP BY si.product_id,p.name ORDER BY gross_profit DESC""",
        fetch=True
    )
    if not rows:
        print("No sales recorded yet.")
        return
    print("\nProduct | Units | Sales | Cost | Estimated gross profit")
    for row in rows:
        print(f'{row["name"]} | {row["units_sold"]} | ₹{row["sales_value"]} | ₹{row["cost_value"]} | ₹{row["gross_profit"]}')

def export_sales_report():
    rows = run_query("SELECT sale_id,sale_date,subtotal,discount,total FROM sales ORDER BY sale_id DESC", fetch=True)
    filename = f"logs/sales_report_{datetime.now():%Y%m%d_%H%M%S}.csv"
    import os, csv
    os.makedirs("logs", exist_ok=True)
    def write_file():
        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["sale_id", "sale_date", "subtotal", "discount", "total"])
            for row in rows:
                writer.writerow([row["sale_id"], row["sale_date"], row["subtotal"], row["discount"], row["total"]])
    thread = Thread(target=write_file, name="sales-report-export")
    thread.start()
    thread.join()
    print(f"Sales report exported to {filename}")
