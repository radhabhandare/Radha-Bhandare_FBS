import os
import csv
from functools import wraps
from database import (
    get_connection,
    verify_password,
    hash_password,
    run_query,
    log_activity
)
from models import Admin, Staff, Product
from validators import (
    required_text,
    read_int,
    read_money,
    read_phone,
    read_email,
    read_optional_int,
    read_optional_money
)

def print_table(headers, rows):
    if not rows:
        print('No records found.')
        return

    rows = [
        ['-' if value is None else str(value) for value in row]
        for row in rows
    ]

    widths = [
        min(25, max(len(str(headers[i])), *(len(row[i]) for row in rows)))
        for i in range(len(headers))
    ]

    def format_row(row):
        return ' | '.join(
            (value[:width - 1] + '…' if len(value) > width else value).ljust(width)
            for value, width in zip(map(str, row), widths)
        )

    print(format_row(headers))
    print('-+-'.join('-' * width for width in widths))

    for row in rows:
        print(format_row(row))
def audit_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        user_id = args[0] if args and isinstance(args[0], int) else None

        log_activity(user_id, func.__name__, 'Operation completed')

        return result

    return wrapper

def login():
    username = input('Username: ').strip()
    password = input('Password: ')

    row = run_query(
        'SELECT user_id, username, password_hash, role FROM users WHERE username=%s',
        (username,),
        fetchone=True
    )

    if not row or not verify_password(password, row['password_hash']):
        print('Invalid username or password.')
        return None

    if row['role'] == 'admin':
        user = Admin(row['user_id'], row['username'])
    else:
        user = Staff(row['user_id'], row['username'])

    print(f"Welcome, {user.username} ({row['role']})")

    return {
        'id': user.user_id,
        'username': user.username,
        'role': row['role'],
        'actions': user.allowed_actions()
    }

@audit_action
def add_product():
    name = required_text('Product name: ')
    category = required_text('Category: ')
    cost = read_money('Purchase price: ')
    price = read_money('Selling price: ')
    quantity = read_int('Opening quantity: ')
    reorder = read_int('Low-stock alert level: ')

    if price < cost:
        print('Warning: selling price is lower than purchase price.')

    product = Product(name, category, cost, price, quantity, reorder)

    product_id = run_query(
        """
        INSERT INTO products
        (name, category, purchase_price, selling_price, quantity, reorder_level)
        VALUES (%s, %s, %s, %s, %s, %s)
        """,
        (
            product.name,
            product.category,
            product.purchase_price,
            product.selling_price,
            product.quantity,
            product.reorder_level
        )
    )

    if product_id:
        print(f'Product added. ID: {product_id}')
    else:
        print('Product could not be added.')


def list_products():
    rows = run_query(
        """
        SELECT product_id, name, category, purchase_price,
               selling_price, quantity, reorder_level
        FROM products
        WHERE active=1
        ORDER BY product_id
        """,
        fetchall=True
    )

    print('\n--- PRODUCT LIST ---')

    if rows is None:
        print('Could not retrieve products.')
        return

    if not rows:
        print('No products found.')
        return

    print_table(
        [
            'ID', 'Product', 'Category', 'Cost (Rs.)',
            'Price (Rs.)', 'Qty', 'Alert', 'Status'
        ],
        [
            [
                row['product_id'],
                row['name'],
                row['category'],
                f"{float(row['purchase_price']):.2f}",
                f"{float(row['selling_price']):.2f}",
                row['quantity'],
                row['reorder_level'],
                'LOW STOCK' if row['quantity'] <= row['reorder_level'] else 'In stock'
            ]
            for row in rows
        ]
    )


@audit_action
def update_product():
    product_id = read_int('Product ID to update: ', 1)

    row = run_query(
        'SELECT * FROM products WHERE product_id=%s AND active=1',
        (product_id,),
        fetchone=True
    )

    if not row:
        print('Product not found.')
        return

    name = input(f"Name [{row['name']}]: ").strip() or row['name']
    category = input(
        f"Category [{row['category'] or ''}]: "
    ).strip() or row['category']

    cost = read_optional_money('Purchase price', row['purchase_price'])
    price = read_optional_money('Selling price', row['selling_price'])
    reorder = read_optional_int('Reorder level', row['reorder_level'])

    result = run_query(
        """
        UPDATE products
        SET name=%s, category=%s, purchase_price=%s,
            selling_price=%s, reorder_level=%s
        WHERE product_id=%s
        """,
        (name, category, cost, price, reorder, product_id)
    )

    if result is not None:
        print('Product updated. Use Record Purchase to change stock quantity.')
    else:
        print('Product could not be updated.')

@audit_action
def add_supplier():
    name = required_text('Supplier name: ')
    phone = read_phone('10-digit phone: ')
    email = read_email('Email (optional): ')
    address = input('Address (optional): ').strip() or None

    supplier_id = run_query(
        """
        INSERT INTO suppliers (name, phone, email, address)
        VALUES (%s, %s, %s, %s)
        """,
        (name, phone, email, address)
    )

    if supplier_id:
        print(f'Supplier added. ID: {supplier_id}')
    else:
        print('Supplier could not be added.')

def list_suppliers():
    rows = run_query(
        """
        SELECT supplier_id, name, phone, email, address
        FROM suppliers
        ORDER BY supplier_id
        """,
        fetchall=True
    )

    print('\n--- SUPPLIER LIST ---')

    if rows is None:
        print('Could not retrieve suppliers.')
        return

    print_table(
        ['ID', 'Supplier', 'Phone', 'Email', 'Address'],
        [
            [
                row['supplier_id'],
                row['name'],
                row['phone'],
                row['email'],
                row['address']
            ]
            for row in rows
        ]
    )

@audit_action
def add_customer():
    name = required_text('Customer name: ')
    phone = read_phone('10-digit phone (blank if unavailable): ', optional=True)
    email = read_email('Email (optional): ')
    address = input('Address (optional): ').strip() or None

    customer_id = run_query(
        """
        INSERT INTO customers (name, phone, email, address)
        VALUES (%s, %s, %s, %s)
        """,
        (name, phone, email, address)
    )

    if customer_id:
        print(f'Customer added. ID: {customer_id}')
    else:
        print('Customer could not be added.')

def list_customers():
    rows = run_query(
        """
        SELECT customer_id, name, phone, email
        FROM customers
        ORDER BY customer_id
        """,
        fetchall=True
    )

    print('\n--- CUSTOMER LIST ---')

    if rows is None:
        print('Could not retrieve customers.')
        return

    print_table(
        ['ID', 'Customer', 'Phone', 'Email'],
        [
            [
                row['customer_id'],
                row['name'],
                row['phone'],
                row['email']
            ]
            for row in rows
        ]
    )

@audit_action
def record_purchase():
    suppliers = run_query(
        'SELECT supplier_id, name FROM suppliers ORDER BY supplier_id',
        fetchall=True
    )

    if suppliers is None:
        print('Could not retrieve suppliers.')
        return

    if not suppliers:
        print('Add a supplier first.')
        return

    print('\n--- AVAILABLE SUPPLIERS ---')

    print_table(
        ['ID', 'Supplier'],
        [[row['supplier_id'], row['name']] for row in suppliers]
    )

    supplier_id = read_int('Supplier ID: ', 1)

    supplier = run_query(
        'SELECT supplier_id FROM suppliers WHERE supplier_id=%s',
        (supplier_id,),
        fetchone=True
    )

    if not supplier:
        print('Supplier ID not found.')
        return

    items = []

    while True:
        list_products()

        product_id = read_int('Product ID (0 to finish): ', 0)

        if product_id == 0:
            break

        product = run_query(
            'SELECT name FROM products WHERE product_id=%s AND active=1',
            (product_id,),
            fetchone=True
        )

        if not product:
            print('Product not found.')
            continue

        quantity = read_int('Quantity received: ', 1)
        cost = read_money('Cost per unit: ')

        items.append((product_id, quantity, cost))

    if not items:
        print('No purchase items entered.')
        return

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            'INSERT INTO purchases (supplier_id, total) VALUES (%s, 0)',
            (supplier_id,)
        )

        purchase_id = cursor.lastrowid
        total = 0

        for product_id, quantity, cost in items:
            line_total = quantity * cost

            cursor.execute(
                """
                INSERT INTO purchase_items
                (purchase_id, product_id, quantity, unit_cost, line_total)
                VALUES (%s, %s, %s, %s, %s)
                """,
                (purchase_id, product_id, quantity, cost, line_total)
            )

            cursor.execute(
                """
                UPDATE products
                SET quantity=quantity+%s, purchase_price=%s
                WHERE product_id=%s
                """,
                (quantity, cost, product_id)
            )

            total += line_total

        cursor.execute(
            'UPDATE purchases SET total=%s WHERE purchase_id=%s',
            (total, purchase_id)
        )

        connection.commit()

        print(f'Purchase #{purchase_id} saved. Total: Rs. {float(total):.2f}')

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()

@audit_action
def make_sale(user_id):
    cart = {}

    while True:
        list_products()

        product_id = read_int('Product ID (0 to checkout): ', 0)

        if product_id == 0:
            break

        row = run_query(
            'SELECT * FROM products WHERE product_id=%s AND active=1',
            (product_id,),
            fetchone=True
        )

        if not row:
            print('Product not found.')
            continue

        quantity = read_int('Quantity: ', 1)

        already_added = cart.get(product_id, {}).get('quantity', 0)
        available = row['quantity'] - already_added

        if quantity > available:
            print(f'Not enough stock. Available to add: {available}')
            continue

        if product_id not in cart:
            cart[product_id] = {
                'name': row['name'],
                'quantity': 0,
                'price': float(row['selling_price']),
                'cost': float(row['purchase_price'])
            }

        cart[product_id]['quantity'] += quantity

    if not cart:
        print('Cart is empty.')
        return

    subtotal = round(
        sum(item['quantity'] * item['price'] for item in cart.values()),
        2
    )

    discount = float(read_money('Discount amount (0 for none): '))

    if discount > subtotal:
        print('Discount cannot exceed subtotal.')
        return

    total = round(subtotal - discount, 2)

    customer_id = None
    entered_id = input('Customer ID (blank for walk-in): ').strip()

    if entered_id:
        try:
            customer_id_input = int(entered_id)

            customer = run_query(
                'SELECT customer_id FROM customers WHERE customer_id=%s',
                (customer_id_input,),
                fetchone=True
            )

            if customer:
                customer_id = customer_id_input
            else:
                print('Customer not found; recording as walk-in.')

        except ValueError:
            print('Invalid customer ID; recording as walk-in.')

    connection = get_connection()
    cursor = connection.cursor()

    try:
        for product_id, item in cart.items():
            cursor.execute(
                'SELECT quantity FROM products WHERE product_id=%s FOR UPDATE',
                (product_id,)
            )

            stock = cursor.fetchone()

            if not stock or stock[0] < item['quantity']:
                raise ValueError(
                    f"Insufficient stock for {item['name']}; sale cancelled."
                )

        cursor.execute(
            """
            INSERT INTO sales
            (customer_id, subtotal, discount, total, created_by)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (customer_id, subtotal, discount, total, user_id)
        )

        sale_id = cursor.lastrowid

        for product_id, item in cart.items():
            quantity = item['quantity']
            line_total = round(quantity * item['price'], 2)

            cursor.execute(
                """
                INSERT INTO sale_items
                (sale_id, product_id, quantity, unit_price, unit_cost, line_total)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (
                    sale_id,
                    product_id,
                    quantity,
                    item['price'],
                    item['cost'],
                    line_total
                )
            )

            cursor.execute(
                'UPDATE products SET quantity=quantity-%s WHERE product_id=%s',
                (quantity, product_id)
            )

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        cursor.close()
        connection.close()

    print('\n========== VYAPARMITRA RECEIPT ==========')
    print(f'Bill number: {sale_id}')

    print_table(
        ['Product', 'Qty', 'Unit price (Rs.)', 'Amount (Rs.)'],
        [
            [
                item['name'],
                item['quantity'],
                f"{item['price']:.2f}",
                f"{item['quantity'] * item['price']:.2f}"
            ]
            for item in cart.values()
        ]
    )

    print(f'Subtotal: Rs. {subtotal:.2f}')
    print(f'Discount: Rs. {discount:.2f}')
    print(f'TOTAL: Rs. {total:.2f}')

    os.makedirs('logs', exist_ok=True)
    path = os.path.join('logs', f'bill_{sale_id}.txt')

    with open(path, 'w', encoding='utf-8') as file:
        file.write(f'VYAPARMITRA RECEIPT\nBill number: {sale_id}\n')

        for item in cart.values():
            amount = item['quantity'] * item['price']

            file.write(
                f"{item['name']}: {item['quantity']} x Rs. "
                f"{item['price']:.2f} = Rs. {amount:.2f}\n"
            )

        file.write(f'Subtotal: Rs. {subtotal:.2f}\n')
        file.write(f'Discount: Rs. {discount:.2f}\n')
        file.write(f'TOTAL: Rs. {total:.2f}\n')

    print(f'Receipt saved to {path}')

def show_low_stock():
    rows = run_query(
        """
        SELECT product_id, name, category, quantity, reorder_level
        FROM products
        WHERE active=1 AND quantity<=reorder_level
        ORDER BY quantity, name
        """,
        fetchall=True
    )

    print('\n--- LOW-STOCK REPORT ---')

    if rows is None:
        print('Could not retrieve low-stock products.')
        return

    if not rows:
        print('No low-stock products. All active products are above their alert levels.')
        return

    print_table(
        ['ID', 'Product', 'Category', 'Quantity', 'Alert level'],
        [
            [
                row['product_id'],
                row['name'],
                row['category'],
                row['quantity'],
                row['reorder_level']
            ]
            for row in rows
        ]
    )

def export_products_csv():
    rows = run_query(
        """
        SELECT product_id, name, category, purchase_price,
               selling_price, quantity, reorder_level
        FROM products
        WHERE active=1
        ORDER BY product_id
        """,
        fetchall=True
    )

    if rows is None:
        print('Could not export products because the database query failed.')
        return

    os.makedirs('exports', exist_ok=True)
    path = os.path.join('exports', 'products.csv')

    with open(path, 'w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)

        writer.writerow([
            'Product ID',
            'Product Name',
            'Category',
            'Purchase Price',
            'Selling Price',
            'Quantity',
            'Reorder Level'
        ])

        for row in rows:
            writer.writerow([
                row['product_id'],
                row['name'],
                row['category'] or '',
                f"{float(row['purchase_price']):.2f}",
                f"{float(row['selling_price']):.2f}",
                row['quantity'],
                row['reorder_level']
            ])

    print(f'Products exported to {path} ({len(rows)} records).')

@audit_action
def add_staff():
    print('\n--- CREATE STAFF ACCOUNT ---')

    username = required_text('Enter staff username: ')

    if len(username) < 3:
        print('Username must contain at least 3 characters.')
        return

    existing_user = run_query(
        'SELECT user_id FROM users WHERE username=%s',
        (username,),
        fetchone=True
    )

    if existing_user:
        print('This username already exists. Choose another username.')
        return

    password = required_text('Enter staff password: ')

    if len(password) < 6:
        print('Password must contain at least 6 characters.')
        return

    confirm_password = required_text('Confirm password: ')

    if password != confirm_password:
        print('Passwords do not match.')
        return

    password_hash = hash_password(password)

    staff_id = run_query(
        """
        INSERT INTO users (username, password_hash, role)
        VALUES (%s, %s, 'staff')
        """,
        (username, password_hash)
    )

    if staff_id:
        print(f'Staff account created successfully. Staff ID: {staff_id}')
    else:
        print('Staff account could not be created.')

def list_staff():
    rows = run_query(
        """
        SELECT user_id, username, role, created_at
        FROM users
        WHERE role='staff'
        ORDER BY user_id
        """,
        fetchall=True
    )

    print('\n--- STAFF ACCOUNTS ---')

    if rows is None:
        print('Could not retrieve staff accounts.')
        return

    if not rows:
        print('No staff accounts found.')
        return

    print_table(
        ['Staff ID', 'Username', 'Role', 'Created date'],
        [
            [
                row['user_id'],
                row['username'],
                row['role'],
                row['created_at'].strftime('%Y-%m-%d %H:%M:%S')
            ]
            for row in rows
        ]
    )
