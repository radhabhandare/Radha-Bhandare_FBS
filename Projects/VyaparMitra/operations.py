from functools import wraps
from database import run_query, log_activity, hash_password, verify_password, get_connection
from models import Admin, Staff, Product
from validators import required_text, read_int, read_money, read_phone, read_email

def audit_action(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        log_activity(f"{function.__name__} completed")
        return result
    return wrapper

def login():
    username = input("Username: ").strip()
    password = input("Password: ")
    rows = run_query("SELECT user_id, username, password_hash, role FROM users WHERE username=%s", (username,), True)
    if not rows or not verify_password(password, rows[0]["password_hash"]):
        print("Invalid username or password.")
        return None
    row = rows[0]
    user = Admin(row["user_id"], row["username"]) if row["role"] == "admin" else Staff(row["user_id"], row["username"])
    print(f"Welcome, {user.username} ({row['role']})")
    return {"id": user.user_id, "username": user.username, "role": row["role"], "actions": user.allowed_actions()}

@audit_action
def add_product():
    name = required_text("Product name: ")
    category = required_text("Category: ")
    purchase_price = read_money("Purchase price: ")
    selling_price = read_money("Selling price: ")
    quantity = read_int("Opening quantity: ")
    reorder_level = read_int("Low-stock alert level (default 5): ")
    product = Product(name, category, purchase_price, selling_price, quantity, reorder_level)
    product_id = run_query(
        "INSERT INTO products(name,category,purchase_price,selling_price,quantity,reorder_level) VALUES(%s,%s,%s,%s,%s,%s)",
        (product.name, product.category, product.purchase_price, product.selling_price, product.quantity, product.reorder_level)
    )
    print(f"Product added. Product ID: {product_id}")

def list_products():
    rows = run_query("SELECT * FROM products WHERE active=1 ORDER BY product_id", fetch=True)
    if not rows:
        print("No products found.")
        return
    print("\nID | Product | Category | Cost | Price | Qty | Reorder")
    for row in rows:
        marker = "  LOW STOCK" if row["quantity"] <= row["reorder_level"] else ""
        print(f'{row["product_id"]} | {row["name"]} | {row["category"]} | {row["purchase_price"]} | {row["selling_price"]} | {row["quantity"]} | {row["reorder_level"]}{marker}')

def search_products():
    term = f"%{required_text('Enter product name/category to search: ')}%"
    rows = run_query(
        "SELECT * FROM products WHERE active=1 AND (name LIKE %s OR category LIKE %s) ORDER BY name",
        (term, term), True
    )
    for row in rows:
        print(f'{row["product_id"]}: {row["name"]} | {row["category"]} | Price ₹{row["selling_price"]} | Stock {row["quantity"]}')
    if not rows:
        print("No matching products.")

@audit_action
def update_product():
    product_id = read_int("Product ID to update: ", 1)
    rows = run_query("SELECT * FROM products WHERE product_id=%s AND active=1", (product_id,), True)
    if not rows:
        print("Product not found.")
        return
    row = rows[0]
    name = input(f'Name [{row["name"]}]: ').strip() or row["name"]
    category = input(f'Category [{row["category"]}]: ').strip() or row["category"]
    purchase_price = read_money(f'Purchase price [{row["purchase_price"]}]: ')
    selling_price = read_money(f'Selling price [{row["selling_price"]}]: ')
    reorder_level = read_int(f'Reorder level [{row["reorder_level"]}]: ')
    run_query(
        "UPDATE products SET name=%s,category=%s,purchase_price=%s,selling_price=%s,reorder_level=%s WHERE product_id=%s",
        (name, category, purchase_price, selling_price, reorder_level, product_id)
    )
    print("Product updated. Note: quantity changes should be recorded through purchases.")

@audit_action
def add_supplier():
    name = required_text("Supplier name: ")
    phone = read_phone("10-digit phone: ")
    email = read_email("Email (optional): ")
    address = input("Address (optional): ").strip() or None
    sid = run_query("INSERT INTO suppliers(name,phone,email,address) VALUES(%s,%s,%s,%s)", (name, phone, email, address))
    print(f"Supplier added. Supplier ID: {sid}")

def list_suppliers():
    rows = run_query("SELECT * FROM suppliers ORDER BY supplier_id", fetch=True)
    for r in rows:
        print(f'{r["supplier_id"]}: {r["name"]} | {r["phone"]} | {r["email"] or "-"} | {r["address"] or "-"}')
    if not rows:
        print("No suppliers found.")

@audit_action
def add_customer():
    name = required_text("Customer name: ")
    phone = read_phone("10-digit phone (blank if unavailable): ", optional=True)
    email = read_email("Email (optional): ")
    cid = run_query("INSERT INTO customers(name,phone,email) VALUES(%s,%s,%s)", (name, phone, email))
    print(f"Customer added. Customer ID: {cid}")

def list_customers():
    rows = run_query("SELECT * FROM customers ORDER BY customer_id", fetch=True)
    for r in rows:
        print(f'{r["customer_id"]}: {r["name"]} | {r["phone"] or "-"} | {r["email"] or "-"}')
    if not rows:
        print("No customers found.")

@audit_action
def record_purchase():
    suppliers = run_query("SELECT supplier_id,name FROM suppliers ORDER BY supplier_id", fetch=True)
    if not suppliers:
        print("Add a supplier first.")
        return
    for s in suppliers:
        print(f'{s["supplier_id"]}: {s["name"]}')
    supplier_id = read_int("Supplier ID: ", 1)
    if not run_query("SELECT supplier_id FROM suppliers WHERE supplier_id=%s", (supplier_id,), True):
        print("Supplier ID not found.")
        return
    items = []
    while True:
        list_products()
        product_id = read_int("Product ID (0 to finish): ", 0)
        if product_id == 0:
            break
        product = run_query("SELECT product_id,name FROM products WHERE product_id=%s AND active=1", (product_id,), True)
        if not product:
            print("Product not found.")
            continue
        qty = read_int("Quantity received: ", 1)
        cost = read_money("Cost per unit: ")
        items.append((product_id, product[0]["name"], qty, cost))
    if not items:
        print("No purchase items entered.")
        return
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO purchases(supplier_id,total) VALUES(%s,%s)", (supplier_id, 0))
        purchase_id = cur.lastrowid
        total = 0
        for product_id, name, qty, cost in items:
            line_total = qty * cost
            cur.execute("INSERT INTO purchase_items(purchase_id,product_id,quantity,unit_cost,line_total) VALUES(%s,%s,%s,%s,%s)",
                        (purchase_id, product_id, qty, cost, line_total))
            cur.execute("UPDATE products SET quantity=quantity+%s,purchase_price=%s WHERE product_id=%s", (qty, cost, product_id))
            total += line_total
        cur.execute("UPDATE purchases SET total=%s WHERE purchase_id=%s", (total, purchase_id))
        conn.commit()
        print(f"Purchase #{purchase_id} saved. Total: ₹{total:.2f}")
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
        product_id = read_int("Product ID (0 to checkout): ", 0)
        if product_id == 0:
            break
        rows = run_query("SELECT * FROM products WHERE product_id=%s AND active=1", (product_id,), True)
        if not rows:
            print("Product not found.")
            continue
        product = rows[0]
        qty = read_int("Quantity: ", 1)
        already = cart.get(product_id, {}).get("quantity", 0)
        if qty + already > product["quantity"]:
            print(f'Not enough stock. Available: {product["quantity"] - already}')
            continue
        if product_id not in cart:
            cart[product_id] = {"name": product["name"], "quantity": 0, "price": float(product["selling_price"]), "cost": float(product["purchase_price"])}
        cart[product_id]["quantity"] += qty
    if not cart:
        print("Cart is empty.")
        return
    subtotal = sum(item["quantity"] * item["price"] for item in cart.values())
    discount = read_money("Discount amount (enter 0 for none): ")
    if discount > subtotal:
        print("Discount cannot exceed subtotal.")
        return
    total = subtotal - discount
    customer_text = input("Customer ID (blank for walk-in): ").strip()
    customer_id = None
    if customer_text:
        try:
            customer_id = int(customer_text)
            if not run_query("SELECT customer_id FROM customers WHERE customer_id=%s", (customer_id,), True):
                print("Customer not found; recording as walk-in.")
                customer_id = None
        except ValueError:
            print("Invalid customer ID; recording as walk-in.")
            customer_id = None

    conn = get_connection()
    cur = conn.cursor()
    try:
        # Lock stock rows and re-check quantities to avoid overselling.
        for product_id, item in cart.items():
            cur.execute("SELECT quantity FROM products WHERE product_id=%s FOR UPDATE", (product_id,))
            stock_row = cur.fetchone()
            if not stock_row or stock_row[0] < item["quantity"]:
                raise ValueError(f'Insufficient stock for {item["name"]}. Sale cancelled.')
        cur.execute("INSERT INTO sales(customer_id,subtotal,discount,total,created_by) VALUES(%s,%s,%s,%s,%s)",
                    (customer_id, subtotal, discount, total, user_id))
        sale_id = cur.lastrowid
        for product_id, item in cart.items():
            qty = item["quantity"]
            line_total = qty * item["price"]
            cur.execute("INSERT INTO sale_items(sale_id,product_id,quantity,unit_price,unit_cost,line_total) VALUES(%s,%s,%s,%s,%s,%s)",
                        (sale_id, product_id, qty, item["price"], item["cost"], line_total))
            cur.execute("UPDATE products SET quantity=quantity-%s WHERE product_id=%s", (qty, product_id))
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        cur.close()
        conn.close()

    print("\n=== VYAPARMITRA RECEIPT ===")
    print(f"Bill number: {sale_id}")
    for item in cart.values():
        print(f'{item["name"]} | {item["quantity"]} x ₹{item["price"]:.2f} = ₹{item["quantity"]*item["price"]:.2f}')
    print(f"Subtotal: ₹{subtotal:.2f}")
    print(f"Discount: ₹{discount:.2f}")
    print(f"TOTAL: ₹{total:.2f}")
    print("=========================================")
    import os
    from datetime import datetime
    os.makedirs("logs", exist_ok=True)
    with open(f"logs/bill_{sale_id}.txt", "w", encoding="utf-8") as f:
        f.write(f"VYAPARMITRA RECEIPT\nBill number: {sale_id}\n")
        for item in cart.values():
            f.write(f'{item["name"]} | {item["quantity"]} x ₹{item["price"]:.2f} = ₹{item["quantity"]*item["price"]:.2f}\n')
        f.write(f"Subtotal: ₹{subtotal:.2f}\nDiscount: ₹{discount:.2f}\nTOTAL: ₹{total:.2f}\n")
    print(f"Receipt saved to logs/bill_{sale_id}.txt")

def show_low_stock():
    rows = run_query("SELECT product_id,name,quantity,reorder_level FROM products WHERE active=1 AND quantity<=reorder_level ORDER BY quantity", fetch=True)
    if not rows:
        print("No low-stock products.")
        return
    for row in rows:
        print(f'{row["product_id"]}: {row["name"]} | Quantity {row["quantity"]} | Alert level {row["reorder_level"]}')

def add_staff():
    username = required_text("New staff username: ")
    password = required_text("Temporary password: ")
    existing = run_query("SELECT user_id FROM users WHERE username=%s", (username,), True)
    if existing:
        print("Username already exists.")
        return
    user_id = run_query("INSERT INTO users(username,password_hash,role) VALUES(%s,%s,'staff')", (username, hash_password(password)))
    print(f"Staff user created with ID {user_id}.")
