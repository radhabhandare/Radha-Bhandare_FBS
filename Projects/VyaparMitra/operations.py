import os
import csv
from functools import wraps

from database import get_connection, verify_password, run_query, log_activity
from models import Admin, Staff, Product
from validators import (
    required_text, read_int, read_money, read_phone, read_email,
    read_optional_int, read_optional_money
)

def print_table(headers, rows):
    if not rows:
        print("No records found.")
        return

    rows = [["-" if value is None else str(value) for value in row]
            for row in rows]
    widths = [
        min(25, max(len(str(headers[i])), *(len(row[i]) for row in rows)))
        for i in range(len(headers))
    ]

    def format_row(row):
        return " | ".join(
            (value[:width - 1] + "…" if len(value) > width else value).ljust(width)
            for value, width in zip(map(str, row), widths)
        )

    print(format_row(headers))
    print("-+-".join("-" * width for width in widths))
    for row in rows:
        print(format_row(row))


def audit_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        user_id = args[0] if args and isinstance(args[0], int) else None
        log_activity(user_id, func.__name__, "Operation completed")
        return result
    return wrapper


def login():
    username = input("Username: ").strip()
    password = input("Password: ")

    row = run_query(
        "SELECT user_id, username, password_hash, role FROM users WHERE username=%s",
        (username,), fetchone=True
    )

    if not row or not verify_password(password, row["password_hash"]):
        print("Invalid username or password.")
        return None

    cls = Admin if row["role"] == "admin" else Staff
    user = cls(row["user_id"], row["username"])
    print(f"Welcome, {user.username} ({row['role']})")

    return {
        "id": user.user_id,
        "username": user.username,
        "role": row["role"],
        "actions": user.allowed_actions()
    }


@audit_action
def add_product():
    name = required_text("Product name: ")
    category = required_text("Category: ")
    cost = read_money("Purchase price: ")
    price = read_money("Selling price: ")
    qty = read_int("Opening quantity: ")
    reorder = read_int("Low-stock alert level: ")

    if price < cost:
        print("Warning: selling price is lower than purchase price.")

    product = Product(name, category, cost, price, qty, reorder)

    pid = run_query(
        """INSERT INTO products
        (name, category, purchase_price, selling_price, quantity, reorder_level)
        VALUES (%s, %s, %s, %s, %s, %s)""",
        (product.name, product.category, product.purchase_price,
         product.selling_price, product.quantity, product.reorder_level)
    )

    print(f"Product added. ID: {pid}" if pid else "Product could not be added.")


def list_products():
    rows = run_query(
        """SELECT product_id, name, category, purchase_price,
        selling_price, quantity, reorder_level
        FROM products WHERE active=1 ORDER BY product_id""",
        fetchall=True
    )

    print("\n--- PRODUCT LIST ---")
    if rows is None:
        print("Could not retrieve products.")
        return
    if not rows:
        print("No products found.")
        return

    print_table(
        ["ID", "Product", "Category", "Cost (Rs.)", "Price (Rs.)",
         "Qty", "Alert", "Status"],
        [[r["product_id"], r["name"], r["category"],
          f'{float(r["purchase_price"]):.2f}',
          f'{float(r["selling_price"]):.2f}', r["quantity"],
          r["reorder_level"],
          "LOW STOCK" if r["quantity"] <= r["reorder_level"] else "In stock"]
         for r in rows]
    )


@audit_action
def update_product():
    pid = read_int("Product ID to update: ", 1)
    r = run_query(
        "SELECT * FROM products WHERE product_id=%s AND active=1",
        (pid,), fetchone=True
    )

    if not r:
        print("Product not found.")
        return

    name = input(f'Name [{r["name"]}]: ').strip() or r["name"]
    category = input(f'Category [{r["category"] or ""}]: ').strip() or r["category"]
    cost = read_optional_money("Purchase price", r["purchase_price"])
    price = read_optional_money("Selling price", r["selling_price"])
    reorder = read_optional_int("Reorder level", r["reorder_level"])

    run_query(
        """UPDATE products SET name=%s, category=%s, purchase_price=%s,
        selling_price=%s, reorder_level=%s WHERE product_id=%s""",
        (name, category, cost, price, reorder, pid)
    )
    print("Product updated. Use Record Purchase to change stock quantity.")


@audit_action
def add_supplier():
    name = required_text("Supplier name: ")
    phone = read_phone("10-digit phone: ")
    email = read_email("Email (optional): ")
    address = input("Address (optional): ").strip() or None

    sid = run_query(
        "INSERT INTO suppliers(name, phone, email, address) VALUES(%s,%s,%s,%s)",
        (name, phone, email, address)
    )
    print(f"Supplier added. ID: {sid}" if sid else "Supplier could not be added.")


def list_suppliers():
    rows = run_query(
        "SELECT supplier_id, name, phone, email, address FROM suppliers ORDER BY supplier_id",
        fetchall=True
    )
    print("\n--- SUPPLIER LIST ---")
    if rows is None:
        print("Could not retrieve suppliers.")
        return
    print_table(
        ["ID", "Supplier", "Phone", "Email", "Address"],
        [[r["supplier_id"], r["name"], r["phone"], r["email"], r["address"]]
         for r in rows]
    )


@audit_action
def add_customer():
    name = required_text("Customer name: ")
    phone = read_phone("10-digit phone (blank if unavailable): ", optional=True)
    email = read_email("Email (optional): ")
    address = input("Address (optional): ").strip() or None

    cid = run_query(
        "INSERT INTO customers(name, phone, email, address) VALUES(%s,%s,%s,%s)",
        (name, phone, email, address)
    )
    print(f"Customer added. ID: {cid}" if cid else "Customer could not be added.")


def list_customers():
    rows = run_query(
        "SELECT customer_id, name, phone, email FROM customers ORDER BY customer_id",
        fetchall=True
    )
    print("\n--- CUSTOMER LIST ---")
    if rows is None:
        print("Could not retrieve customers.")
        return
    print_table(
        ["ID", "Customer", "Phone", "Email"],
        [[r["customer_id"], r["name"], r["phone"], r["email"]]
         for r in rows]
    )


@audit_action
def record_purchase():
    suppliers = run_query(
        "SELECT supplier_id, name FROM suppliers ORDER BY supplier_id",
        fetchall=True
    )

    if not suppliers:
        print("Add a supplier first.")
        return

    print("\n--- AVAILABLE SUPPLIERS ---")
    print_table(["ID", "Supplier"],
                [[s["supplier_id"], s["name"]] for s in suppliers])

    sid = read_int("Supplier ID: ", 1)
    if not run_query(
        "SELECT supplier_id FROM suppliers WHERE supplier_id=%s",
        (sid,), fetchone=True
    ):
        print("Supplier ID not found.")
        return

    items = []
    while True:
        list_products()
        pid = read_int("Product ID (0 to finish): ", 0)
        if pid == 0:
            break

        product = run_query(
            "SELECT name FROM products WHERE product_id=%s AND active=1",
            (pid,), fetchone=True
        )
        if not product:
            print("Product not found.")
            continue

        qty = read_int("Quantity received: ", 1)
        cost = read_money("Cost per unit: ")
        items.append((pid, qty, cost))

    if not items:
        print("No purchase items entered.")
        return

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute(
            "INSERT INTO purchases(supplier_id, total) VALUES(%s, 0)",
            (sid,)
        )
        purchase_id = cur.lastrowid
        total = 0

        for pid, qty, cost in items:
            line = qty * cost
            cur.execute(
                """INSERT INTO purchase_items
                (purchase_id, product_id, quantity, unit_cost, line_total)
                VALUES(%s,%s,%s,%s,%s)""",
                (purchase_id, pid, qty, cost, line)
            )
            cur.execute(
                """UPDATE products
                SET quantity=quantity+%s, purchase_price=%s
                WHERE product_id=%s""",
                (qty, cost, pid)
            )
            total += line

        cur.execute(
            "UPDATE purchases SET total=%s WHERE purchase_id=%s",
            (total, purchase_id)
        )
        conn.commit()
        print(f"Purchase #{purchase_id} saved. Total: Rs. {float(total):.2f}")

    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()


@audit_action
def make_sale(user_id):
    cart = {}

    while True:
        list_products()
        pid = read_int("Product ID (0 to checkout): ", 0)
        if pid == 0:
            break

        r = run_query(
            "SELECT * FROM products WHERE product_id=%s AND active=1",
            (pid,), fetchone=True
        )
        if not r:
            print("Product not found.")
            continue

        qty = read_int("Quantity: ", 1)
        available = r["quantity"] - cart.get(pid, {}).get("quantity", 0)

        if qty > available:
            print(f"Not enough stock. Available to add: {available}")
            continue

        if pid not in cart:
            cart[pid] = {
                "name": r["name"], "quantity": 0,
                "price": float(r["selling_price"]),
                "cost": float(r["purchase_price"])
            }
        cart[pid]["quantity"] += qty

    if not cart:
        print("Cart is empty.")
        return

    subtotal = round(sum(x["quantity"] * x["price"] for x in cart.values()), 2)
    discount = float(read_money("Discount amount (0 for none): "))

    if discount > subtotal:
        print("Discount cannot exceed subtotal.")
        return

    total = round(subtotal - discount, 2)
    customer_id = None
    text_id = input("Customer ID (blank for walk-in): ").strip()

    if text_id:
        try:
            cid = int(text_id)
            if run_query(
                "SELECT customer_id FROM customers WHERE customer_id=%s",
                (cid,), fetchone=True
            ):
                customer_id = cid
            else:
                print("Customer not found; recording as walk-in.")
        except ValueError:
            print("Invalid customer ID; recording as walk-in.")

    conn = get_connection()
    cur = conn.cursor()

    try:
        for pid, item in cart.items():
            cur.execute(
                "SELECT quantity FROM products WHERE product_id=%s FOR UPDATE",
                (pid,)
            )
            stock = cur.fetchone()
            if not stock or stock[0] < item["quantity"]:
                raise ValueError(
                    f'Insufficient stock for {item["name"]}; sale cancelled.'
                )

        cur.execute(
            """INSERT INTO sales(customer_id, subtotal, discount, total, created_by)
            VALUES(%s,%s,%s,%s,%s)""",
            (customer_id, subtotal, discount, total, user_id)
        )
        sale_id = cur.lastrowid

        for pid, item in cart.items():
            qty = item["quantity"]
            line = round(qty * item["price"], 2)
            cur.execute(
                """INSERT INTO sale_items
                (sale_id, product_id, quantity, unit_price, unit_cost, line_total)
                VALUES(%s,%s,%s,%s,%s,%s)""",
                (sale_id, pid, qty, item["price"], item["cost"], line)
            )
            cur.execute(
                "UPDATE products SET quantity=quantity-%s WHERE product_id=%s",
                (qty, pid)
            )

        conn.commit()

    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()

    print("\n========== VYAPARMITRA RECEIPT ==========")
    print(f"Bill number: {sale_id}")
    print_table(
        ["Product", "Qty", "Unit price (Rs.)", "Amount (Rs.)"],
        [[x["name"], x["quantity"], f'{x["price"]:.2f}',
          f'{x["quantity"] * x["price"]:.2f}']
         for x in cart.values()]
    )
    print(f"Subtotal: Rs. {subtotal:.2f}")
    print(f"Discount: Rs. {discount:.2f}")
    print(f"TOTAL: Rs. {total:.2f}")

    os.makedirs("logs", exist_ok=True)
    path = os.path.join("logs", f"bill_{sale_id}.txt")

    with open(path, "w", encoding="utf-8") as file:
        file.write(f"VYAPARMITRA RECEIPT\nBill number: {sale_id}\n")
        for item in cart.values():
            amount = item["quantity"] * item["price"]
            file.write(
                f'{item["name"]}: {item["quantity"]} x Rs. '
                f'{item["price"]:.2f} = Rs. {amount:.2f}\n'
            )
        file.write(
            f"Subtotal: Rs. {subtotal:.2f}\n"
            f"Discount: Rs. {discount:.2f}\n"
            f"TOTAL: Rs. {total:.2f}\n"
        )

    print(f"Receipt saved to {path}")


def show_low_stock():
    rows = run_query(
        """SELECT product_id, name, category, quantity, reorder_level
        FROM products
        WHERE active=1 AND quantity<=reorder_level
        ORDER BY quantity, name""",
        fetchall=True
    )

    print("\n--- LOW-STOCK REPORT ---")
    if rows is None:
        print("Could not retrieve low-stock products.")
        return
    if not rows:
        print("No low-stock products. All active products are above their alert levels.")
        return

    print_table(
        ["ID", "Product", "Category", "Quantity", "Alert level"],
        [[r["product_id"], r["name"], r["category"],
          r["quantity"], r["reorder_level"]]
         for r in rows]
    )


def export_products_csv():
    """Export active products to a CSV file that opens in Excel."""
    rows = run_query(
        """SELECT product_id, name, category, purchase_price,
        selling_price, quantity, reorder_level
        FROM products WHERE active=1 ORDER BY product_id""",
        fetchall=True
    )

    if rows is None:
        print("Could not export products because the database query failed.")
        return

    os.makedirs("exports", exist_ok=True)
    path = os.path.join("exports", "products.csv")

    with open(path, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Product ID", "Product Name", "Category",
            "Purchase Price", "Selling Price", "Quantity", "Reorder Level"
        ])
        for r in rows:
            writer.writerow([
                r["product_id"], r["name"], r["category"] or "",
                f'{float(r["purchase_price"]):.2f}',
                f'{float(r["selling_price"]):.2f}',
                r["quantity"], r["reorder_level"]
            ])

    print(f"Products exported to {path} ({len(rows)} records).")
