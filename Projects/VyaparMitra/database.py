import hashlib
import mysql.connector

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "radha",
}

DB_NAME = "vyaparmitra"


def get_connection():
    return mysql.connector.connect(
        **DB_CONFIG,
        database=DB_NAME,
    )


def hash_password(password):
    """Return the SHA-256 hash of a password."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def verify_password(password, stored_hash):
    """Verify a password against its stored hash."""
    return hash_password(password) == stored_hash


def run_query(
    query,
    params=None,
    fetchone=False,
    fetchall=False,
    commit=False,
    fetch=False,
):
    """
    Execute an SQL query.

    fetchone=True returns one dictionary.
    fetchall=True or fetch=True returns a list of dictionaries.
    INSERT returns the new row ID.
    UPDATE/DELETE return the number of affected rows.
    Data-changing queries are committed automatically.
    """
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params or ())

        if fetchone:
            result = cursor.fetchone()
        elif fetchall or fetch:
            result = cursor.fetchall()
        elif cursor.with_rows:
            result = None
        elif query.lstrip().upper().startswith("INSERT"):
            result = cursor.lastrowid
        else:
            result = cursor.rowcount

        if commit or not cursor.with_rows:
            connection.commit()

        return result

    except mysql.connector.Error as error:
        if connection:
            connection.rollback()

        print(f"Database error: {error}")
        return None

    finally:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()


def log_activity(user_id, action, details=""):
    """Record an activity in the activity_logs table."""
    return run_query(
        """
        INSERT INTO activity_logs (user_id, action, details)
        VALUES (%s, %s, %s)
        """,
        (user_id, action, details),
    )


def initialize_database():
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()

        cursor.execute(
            f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}` "
            "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
        )
        connection.database = DB_NAME

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                user_id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL UNIQUE,
                password_hash VARCHAR(255) NOT NULL,
                role ENUM('admin', 'staff') NOT NULL DEFAULT 'staff',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                product_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                category VARCHAR(100),
                quantity INT NOT NULL DEFAULT 0,
                purchase_price DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
                selling_price DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
                reorder_level INT NOT NULL DEFAULT 5,
                active TINYINT(1) NOT NULL DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS suppliers (
                supplier_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                phone VARCHAR(15),
                email VARCHAR(100),
                address VARCHAR(255),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                phone VARCHAR(15),
                email VARCHAR(100),
                address VARCHAR(255),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS purchases (
                purchase_id INT AUTO_INCREMENT PRIMARY KEY,
                supplier_id INT,
                total DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
                purchase_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (supplier_id)
                    REFERENCES suppliers(supplier_id)
                    ON DELETE SET NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS purchase_items (
                purchase_item_id INT AUTO_INCREMENT PRIMARY KEY,
                purchase_id INT NOT NULL,
                product_id INT NOT NULL,
                quantity INT NOT NULL,
                unit_cost DECIMAL(10, 2) NOT NULL,
                line_total DECIMAL(10, 2) NOT NULL,
                FOREIGN KEY (purchase_id)
                    REFERENCES purchases(purchase_id)
                    ON DELETE CASCADE,
                FOREIGN KEY (product_id)
                    REFERENCES products(product_id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                sale_id INT AUTO_INCREMENT PRIMARY KEY,
                customer_id INT,
                subtotal DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
                discount DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
                total DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
                created_by INT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (customer_id)
                    REFERENCES customers(customer_id)
                    ON DELETE SET NULL,
                FOREIGN KEY (created_by)
                    REFERENCES users(user_id)
                    ON DELETE SET NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sale_items (
                sale_item_id INT AUTO_INCREMENT PRIMARY KEY,
                sale_id INT NOT NULL,
                product_id INT NOT NULL,
                quantity INT NOT NULL,
                unit_price DECIMAL(10, 2) NOT NULL,
                unit_cost DECIMAL(10, 2) NOT NULL,
                line_total DECIMAL(10, 2) NOT NULL,
                FOREIGN KEY (sale_id)
                    REFERENCES sales(sale_id)
                    ON DELETE CASCADE,
                FOREIGN KEY (product_id)
                    REFERENCES products(product_id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS activity_logs (
                log_id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                action VARCHAR(100) NOT NULL,
                details TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id)
                    REFERENCES users(user_id)
                    ON DELETE SET NULL
            )
        """)

        cursor.execute(
            "SELECT user_id FROM users WHERE username = %s",
            ("admin",),
        )

        if not cursor.fetchone():
            cursor.execute("""
                INSERT INTO users (username, password_hash, role)
                VALUES (%s, %s, %s)
            """, ("admin", hash_password("admin123"), "admin"))

        connection.commit()
        print("Database initialized successfully.")

    except mysql.connector.Error as error:
        if connection:
            connection.rollback()

        print(f"Database initialization error: {error}")
        raise

    finally:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()
