import os
import mysql.connector
from mysql.connector import Error
from hashlib import pbkdf2_hmac
from secrets import token_hex

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'radha',
    'database': 'vyaparmitra'
    
}

def get_connection():
    
    return mysql.connector.connect(**DB_CONFIG)

def hash_password(password, salt=None):
    salt = salt or token_hex(16)
    digest = pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), 120000).hex()
    return f"{salt}${digest}"

def verify_password(password, stored_hash):
    try:
        salt, expected = stored_hash.split("$", 1)
        actual = pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), 120000).hex()
        return actual == expected
    except (ValueError, AttributeError):
        return False

def initialize_database():
    """Create tables and add a first-run administrator if no users exist."""
    conn = get_connection()
    cursor = conn.cursor()
    statements = [
        """CREATE TABLE IF NOT EXISTS users (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            password_hash VARCHAR(255) NOT NULL,
            role ENUM('admin','staff') NOT NULL DEFAULT 'staff',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""",
        """CREATE TABLE IF NOT EXISTS products (
            product_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            category VARCHAR(60) NOT NULL,
            purchase_price DECIMAL(10,2) NOT NULL,
            selling_price DECIMAL(10,2) NOT NULL,
            quantity INT NOT NULL DEFAULT 0,
            reorder_level INT NOT NULL DEFAULT 5,
            active TINYINT NOT NULL DEFAULT 1
        )""",
        """CREATE TABLE IF NOT EXISTS suppliers (
            supplier_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(15) NOT NULL,
            email VARCHAR(120),
            address VARCHAR(255)
        )""",
        """CREATE TABLE IF NOT EXISTS customers (
            customer_id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(15),
            email VARCHAR(120)
        )""",
        """CREATE TABLE IF NOT EXISTS purchases (
            purchase_id INT AUTO_INCREMENT PRIMARY KEY,
            supplier_id INT NOT NULL,
            purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            total DECIMAL(12,2) NOT NULL DEFAULT 0,
            FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id)
        )""",
        """CREATE TABLE IF NOT EXISTS purchase_items (
            item_id INT AUTO_INCREMENT PRIMARY KEY,
            purchase_id INT NOT NULL,
            product_id INT NOT NULL,
            quantity INT NOT NULL,
            unit_cost DECIMAL(10,2) NOT NULL,
            line_total DECIMAL(12,2) NOT NULL,
            FOREIGN KEY (purchase_id) REFERENCES purchases(purchase_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )""",
        """CREATE TABLE IF NOT EXISTS sales (
            sale_id INT AUTO_INCREMENT PRIMARY KEY,
            customer_id INT NULL,
            sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            subtotal DECIMAL(12,2) NOT NULL,
            discount DECIMAL(12,2) NOT NULL DEFAULT 0,
            total DECIMAL(12,2) NOT NULL,
            created_by INT NULL,
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE SET NULL,
            FOREIGN KEY (created_by) REFERENCES users(user_id) ON DELETE SET NULL
        )""",
        """CREATE TABLE IF NOT EXISTS sale_items (
            item_id INT AUTO_INCREMENT PRIMARY KEY,
            sale_id INT NOT NULL,
            product_id INT NOT NULL,
            quantity INT NOT NULL,
            unit_price DECIMAL(10,2) NOT NULL,
            unit_cost DECIMAL(10,2) NOT NULL,
            line_total DECIMAL(12,2) NOT NULL,
            FOREIGN KEY (sale_id) REFERENCES sales(sale_id),
            FOREIGN KEY (product_id) REFERENCES products(product_id)
        )"""
    ]
    try:
        for statement in statements:
            cursor.execute(statement)
        conn.commit()
        cursor.execute("SELECT COUNT(*) FROM users")
        if cursor.fetchone()[0] == 0:
            cursor.execute(
                "INSERT INTO users (username, password_hash, role) VALUES (%s, %s, %s)",
                ("admin", hash_password("admin123"), "admin")
            )
            conn.commit()
            print("First-run admin created: username=admin, password=admin123")
            print("Change this password before using the application seriously.")
    finally:
        cursor.close()
        conn.close()

def run_query(query, params=(), fetch=False):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(query, params)
        if fetch:
            return cursor.fetchall()
        conn.commit()
        return cursor.lastrowid
    finally:
        cursor.close()
        conn.close()

def log_activity(message):
    from datetime import datetime
    os.makedirs("logs", exist_ok=True)
    with open(os.path.join("logs", "activity.log"), "a", encoding="utf-8") as file:
        file.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} | {message}\n")
