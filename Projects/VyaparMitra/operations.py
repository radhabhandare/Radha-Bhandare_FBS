import os
from functools import wraps

from database import (
    get_connection,
    hash_password,
    log_activity,
    run_query,
    verify_password,
)
from models import Admin, Staff, Product
from validators import (
    required_text,
    read_int,
    read_money,
    read_phone,
    read_email,
    read_optional_int,
    read_optional_money,
)


# Log successful operations
def audit_action(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        log_activity(f"{function.__name__} completed")
        return result
    return wrapper


# Login
def login():
    username = input("Username: ").strip()
    password = input("Password: ")

    rows = run_query(
        """SELECT user_id, username, password_hash, role
           FROM users WHERE username=%s""",
        (username,),
        True,
    )

    if not rows or not verify_password(password, rows[0]["password_hash"]):
        print("Invalid username or password.")
        return None

    row = rows[0]

    user = (
        Admin(row["user_id"], row["username"])
        if row["role"] == "admin"
        else Staff(row["user_id"], row["username"])
    )

    print(f"Welcome, {user.username} ({row['role']})")

    return {
        "id": user.user_id,
        "username": user.username,
        "role": row["role"],
        "actions": user.allowed_actions(),
    }


# Add product
@audit_action
def add_product():
    name = required_text("Product name: ")
    category = required_text("Category: ")
    purchase_price = read_money("Purchase price: ")
    selling_price = read_money("Selling price: ")
    quantity = read_int("Opening quantity: ")
    reorder_level = read_int("Low-stock alert level (default 5): ")

    if selling_price < purchase_price:
        print("Warning: selling price is lower than purchase price.")

    product = Product(
        name,
        category,
        purchase_price,
        selling_price,
        quantity,
        reorder_level,
    )

    product_id = run_query(
        """INSERT INTO products
           (name, category, purchase_price, selling_price,
            quantity, reorder_level)
           VALUES (%s, %s, %s, %s, %s, %s)""",
        (
            product.name,
            product.category,
            product.purchase_price,
            product.selling_price,
            product.quantity,
            product.reorder_level,
        ),
    )

    print(f"Product added successfully. Product ID: {product_id}")


# Display products in aligned columns
def list_products():
    rows = run_query(
        """SELECT product_id, name, category, purchase_price,
                  selling_price, quantity, reorder_level
           FROM products
           WHERE active=1
           ORDER BY product_id""",
        fetch=True,
    )

    if not rows:
        print("\nNo products found.")
        return

    print("\n" + "=" * 112)
    print(" " * 36 + "VYAPARMITRA - PRODUCT INVENTORY")
    print("=" * 112)

    print(
        f"{'ID':<5} "
        f"{'Product':<22} "
        f"{'Category':<18} "
        f"{'Cost (Rs.)':>12} "
        f"{'Price (Rs.)':>12} "
        f"{'Qty':>8} "
        f"{'Reorder':>8} "
        f"{'Status':<12}"
    )

    print("-" * 112)

    for row in rows:
        status = (
            "LOW STOCK"
            if row["quantity"] <= row["reorder_level"]
            else "In Stock"
        )

        print(
            f"{row['product_id']:<5} "
            f"{row['name']:<22.22} "
            f"{row['category']:<18.18} "
            f"{float(row['purchase_price']):>12.2f} "
            f"{float(row['selling_price']):>12.2f} "
            f"{row['quantity']:>8} "
            f"{row['reorder_level']:>8} "
            f"{status:<12}"
        )

    print("=" * 112)


# Search products
def search_products():
    term = f"%{required_text('Enter product name/category to search: ')}%"

    rows = run_query(
        """SELECT product_id, name, category, purchase_price,
                  selling_price, quantity, reorder_level
           FROM products
           WHERE active=1
             AND (name LIKE %s OR category LIKE %s)
           ORDER BY name""",
        (term, term),
        True,
    )

    if not rows:
        print("No matching products found.")
        return

    print("\nID | Product | Category | Cost | Price | Qty | Reorder | Status")
    print("-" * 95)

    for row in rows:
        status = (
            "LOW STOCK"
            if row["quantity"] <= row["reorder_level"]
            else "In Stock"
        )

        print(
            f'{row["product_id"]} | {row["name"]} | {row["category"]} | '
            f'Rs. {float(row["purchase_price"]):.2f} | '
            f'Rs. {float(row["selling_price"]):.2f} | '
            f'{row["quantity"]} | {row["reorder_level"]} | {status}'
        )


# Update product
@audit_action
def update_product():
    product_id = read_int("Product ID to update: ", 1)

    rows = run_query(
        "SELECT * FROM products WHERE product_id=%s AND active=1",
        (product_id,),
        True,
    )

    if not rows:
        print("Product not found.")
        return

    row = rows[0]

    name = input(f'Name [{row["name"]}]: ').strip() or row["name"]
    category = (
        input(f'Category [{row["category"]}]: ').strip()
        or row["category"]
    )

    purchase_price = read_optional_money(
        "Purchase price", row["purchase_price"]
    )
    selling_price = read_optional_money(
        "Selling price", row["selling_price"]
    )
    reorder_level = read_optional_int(
        "Reorder level", row["reorder_level"]
    )

    if selling_price < purchase_price:
        print("Warning: selling price is lower than purchase price.")

    run_query(
        """UPDATE products
           SET name=%s, category=%s, purchase_price=%s,
               selling_price=%s, reorder_level=%s
           WHERE product_id=%s""",
        (
            name,
            category,
            purchase_price,
            selling_price,
            reorder_level,
            product_id,
        ),
    )

    print("Product updated successfully.")
    print("Press Enter on a field to keep its current value.")
    print("Use the purchase process to change stock quantity.")


# Add supplier
@audit_action
def add_supplier():
    name = required_text("Supplier name: ")
    phone = read_phone("10-digit phone: ")
    email = read_email("Email (optional): ")
    address = input("Address (optional): ").strip() or None

    supplier_id = run_query(
        """INSERT INTO suppliers(name, phone, email, address)
           VALUES (%s, %s, %s, %s)""",
        (name, phone, email, address),
    )

    print(f"Supplier added. Supplier ID: {supplier_id}")


# List suppliers
def list_suppliers():
    rows = run_query(
        "SELECT * FROM suppliers ORDER BY supplier_id",
        fetch=True,
    )

    if not rows:
        print("No suppliers found.")
        return

    print("\nID | Supplier | Phone | Email | Address")
    print("-" * 90)

    for row in rows:
        print(
            f'{row["supplier_id"]} | {row["name"]} | {row["phone"]} | '
            f'{row["email"] or "-"} | {row["address"] or "-"}'
        )


# Add customer
@audit_action
def add_customer():
    name = required_text("Customer name: ")
    phone = read_phone(
        "10-digit phone (blank if unavailable): ",
        optional=True,
    )
    email = read_email("Email (optional): ")

    customer_id = run_query(
        """INSERT INTO customers(name, phone, email)
           VALUES (%s, %s, %s)""",
        (name, phone, email),
    )

    print(f"Customer added. Customer ID: {customer_id}")


# List customers
def list_customers():
    rows = run_query(
        "SELECT * FROM customers ORDER BY customer_id",
        fetch=True,
    )

    if not rows:
        print("No customers found.")
        return

    print("\nID | Customer | Phone | Email")
    print("-" * 70)

    for row in rows:
        print(
            f'{row["customer_id"]} | {row["name"]} | '
            f'{row["phone"] or "-"} | {row["email"] or "-"}'
        )


# Record a purchase and increase stock
@audit_action
def record_purchase():
    suppliers = run_query(
        "SELECT supplier_id, name FROM suppliers ORDER BY supplier_id",
        fetch=True,
    )

    if not suppliers:
        print("Add a supplier first.")
        return

    print("\nAvailable suppliers:")
    for supplier in suppliers:
        print(f'{supplier["supplier_id"]}: {supplier["name"]}')

    supplier_id = read_int("Supplier ID: ", 1)

    if not run_query(
        "SELECT supplier_id FROM suppliers WHERE supplier_id=%s",
        (supplier_id,),
        True,
    ):
        print("Supplier ID not found.")
        return

    items = []

    while True:
        list_products()
        product_id = read_int("Product ID (0 to finish): ", 0)

        if product_id == 0:
            break

        product = run_query(
            """SELECT product_id, name FROM products
               WHERE product_id=%s AND active=1""",
            (product_id,),
            True,
        )

        if not product:
            print("Product not found.")
            continue

        quantity = read_int("Quantity received: ", 1)
        cost = read_money("Cost per unit: ")

        items.append(
            (product_id, product[0]["name"], quantity, cost)
        )

    if not items:
        print("No purchase items entered.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO purchases(supplier_id, total) VALUES(%s, %s)",
            (supplier_id, 0),
        )

        purchase_id = cursor.lastrowid
        total = 0.0

        for product_id, _name, quantity, cost in items:
            line_total = quantity * cost

            cursor.execute(
                """INSERT INTO purchase_items
                   (purchase_id, product_id, quantity, unit_cost, line_total)
                   VALUES (%s, %s, %s, %s, %s)""",
                (
                    purchase_id,
                    product_id,
                    quantity,
                    cost,
                    line_total,
                ),
            )

            cursor.execute(
                """UPDATE products
                   SET quantity=quantity+%s, purchase_price=%s
                   WHERE product_id=%s""",
                (quantity, cost, product_id),
            )

            total += line_total

        cursor.execute(
            "UPDATE purchases SET total=%s WHERE purchase_id=%s",
            (total, purchase_id),
        )

        conn.commit()
        print(f"Purchase #{purchase_id} saved. Total: Rs. {total:.2f}")

    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()


# Sales and billing
@audit_action
def make_sale(user_id):
    cart = {}

    while True:
        list_products()
        product_id = read_int("Product ID (0 to checkout): ", 0)

        if product_id == 0:
            break

        rows = run_query(
            "SELECT * FROM products WHERE product_id=%s AND active=1",
            (product_id,),
            True,
        )

        if not rows:
            print("Product not found.")
            continue

        product = rows[0]
        quantity = read_int("Quantity: ", 1)

        already = cart.get(product_id, {}).get("quantity", 0)
        available = product["quantity"] - already

        if quantity > available:
            print(f"Not enough stock. Available to add: {available}")
            continue

        if product_id not in cart:
            cart[product_id] = {
                "name": product["name"],
                "quantity": 0,
                "price": float(product["selling_price"]),
                "cost": float(product["purchase_price"]),
            }

        cart[product_id]["quantity"] += quantity

    if not cart:
        print("Cart is empty.")
        return

    subtotal = round(
        sum(item["quantity"] * item["price"] for item in cart.values()),
        2,
    )

    discount = read_money("Discount amount (enter 0 for none): ")

    if discount > subtotal:
        print("Discount cannot exceed subtotal.")
        return

    total = round(subtotal - discount, 2)

    customer_text = input("Customer ID (blank for walk-in): ").strip()
    customer_id = None

    if customer_text:
        try:
            possible_id = int(customer_text)
            customers = run_query(
                "SELECT customer_id FROM customers WHERE customer_id=%s",
                (possible_id,),
                True,
            )

            if customers:
                customer_id = possible_id
            else:
                print("Customer not found; recording as walk-in.")

        except ValueError:
            print("Invalid customer ID; recording as walk-in.")

    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Recheck stock while locking rows to prevent overselling.
        for product_id, item in cart.items():
            cursor.execute(
                "SELECT quantity FROM products WHERE product_id=%s FOR UPDATE",
                (product_id,),
            )
            stock_row = cursor.fetchone()

            if not stock_row or stock_row[0] < item["quantity"]:
                raise ValueError(
                    f'Insufficient stock for {item["name"]}. Sale cancelled.'
                )

        cursor.execute(
            """INSERT INTO sales
               (customer_id, subtotal, discount, total, created_by)
               VALUES (%s, %s, %s, %s, %s)""",
            (customer_id, subtotal, discount, total, user_id),
        )

        sale_id = cursor.lastrowid

        for product_id, item in cart.items():
            quantity = item["quantity"]
            line_total = round(quantity * item["price"], 2)

            cursor.execute(
                """INSERT INTO sale_items
                   (sale_id, product_id, quantity, unit_price,
                    unit_cost, line_total)
                   VALUES (%s, %s, %s, %s, %s, %s)""",
                (
                    sale_id,
                    product_id,
                    quantity,
                    item["price"],
                    item["cost"],
                    line_total,
                ),
            )

            cursor.execute(
                "UPDATE products SET quantity=quantity-%s WHERE product_id=%s",
                (quantity, product_id),
            )

        conn.commit()

    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()

    print("\n" + "=" * 42)
    print("             VYAPARMITRA RECEIPT")
    print("=" * 42)
    print(f"Bill number: {sale_id}")

    for item in cart.values():
        line_total = item["quantity"] * item["price"]
        print(
            f'{item["name"]} | {item["quantity"]} x '
            f'Rs. {item["price"]:.2f} = Rs. {line_total:.2f}'
        )

    print("-" * 42)
    print(f"Subtotal: Rs. {subtotal:.2f}")
    print(f"Discount: Rs. {discount:.2f}")
    print(f"TOTAL:    Rs. {total:.2f}")
    print("=" * 42)

    os.makedirs("logs", exist_ok=True)
    receipt_path = os.path.join("logs", f"bill_{sale_id}.txt")

    with open(receipt_path, "w", encoding="utf-8") as file:
        file.write("VYAPARMITRA RECEIPT\n")
        file.write(f"Bill number: {sale_id}\n")

        for item in cart.values():
            line_total = item["quantity"] * item["price"]
            file.write(
                f'{item["name"]} | {item["quantity"]} x '
                f'Rs. {item["price"]:.2f} = Rs. {line_total:.2f}\n'
            )

        file.write(f"Subtotal: Rs. {subtotal:.2f}\n")
        file.write(f"Discount: Rs. {discount:.2f}\n")
        file.write(f"TOTAL: Rs. {total:.2f}\n")

    print(f"Receipt saved to {receipt_path}")


# Low-stock report
def show_low_stock():
    rows = run_query(
        """SELECT product_id, name, category, quantity, reorder_level
           FROM products
           WHERE active=1 AND quantity<=reorder_level
           ORDER BY quantity ASC, name ASC""",
        fetch=True,
    )

    print("\n" + "=" * 82)
    print(" " * 25 + "VYAPARMITRA - LOW STOCK REPORT")
    print("=" * 82)

    if not rows:
        print("No low-stock products.")
        print("All active products are above their alert levels.")
        print("=" * 82)
        return

    print(
        f"{'ID':<6} {'Product':<24} {'Category':<20} "
        f"{'Quantity':>10} {'Alert level':>12}"
    )
    print("-" * 82)

    for row in rows:
        print(
            f'{row["product_id"]:<6} '
            f'{row["name"]:<24.24} '
            f'{row["category"]:<20.20} '
            f'{row["quantity"]:>10} '
            f'{row["reorder_level"]:>12}'
        )

    print("=" * 82)


# Create staff login
def add_staff():
    username = required_text("New staff username: ")
    password = required_text("Temporary password: ")

    existing = run_query(
        "SELECT user_id FROM users WHERE username=%s",
        (username,),
        True,
    )

    if existing:
        print("Username already exists.")
        return

    user_id = run_query(
        """INSERT INTO users(username, password_hash, role)
           VALUES (%s, %s, 'staff')""",
        (username, hash_password(password)),
    )

    print(f"Staff user created with ID {user_id}.")
