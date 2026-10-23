from database import initialize_database
from operations import (
    login, add_product, list_products, search_products, update_product,
    add_supplier, list_suppliers, add_customer, list_customers,
    record_purchase, make_sale, show_low_stock, add_staff
)
from reports import sales_report, profit_report, export_sales_report

def product_menu(user):
    while True:
        print("\n--- Product Management ---")
        print("1. Add product")
        print("2. List products")
        print("3. Search product")
        print("4. Update product")
        print("5. Low-stock report")
        print("0. Back")
        choice = input("Choice: ").strip()
        if choice == "1":
            if user["role"] == "admin":
                add_product()
            else:
                print("Admin permission required.")
        elif choice == "2":
            list_products()
        elif choice == "3":
            search_products()
        elif choice == "4":
            if user["role"] == "admin":
                update_product()
            else:
                print("Admin permission required.")
        elif choice == "5":
            show_low_stock()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

def main_menu(user):
    while True:
        print("\n== VYAPARMITRA ==")
        print(f'Logged in: {user["username"]} ({user["role"]})')
        print("1. Product management")
        print("2. Supplier management")
        print("3. Customer management")
        print("4. Record purchase")
        print("5. Sales and billing")
        print("6. Low-stock report")
        print("7. Daily sales report")
        print("8. Product-wise gross profit report")
        print("9. Export sales report to CSV")
        if user["role"] == "admin":
            print("10. Create staff login")
        print("0. Logout")
        choice = input("Enter choice: ").strip()
        try:
            if choice == "1":
                product_menu(user)
            elif choice == "2":
                if user["role"] != "admin":
                    print("Admin permission required.")
                else:
                    print("\n1. Add supplier\n2. List suppliers")
                    sub = input("Choice: ").strip()
                    if sub == "1":
                        add_supplier()
                    elif sub == "2":
                        list_suppliers()
                    else:
                        print("Invalid choice.")
            elif choice == "3":
                print("\n1. Add customer\n2. List customers")
                sub = input("Choice: ").strip()
                if sub == "1":
                    add_customer()
                elif sub == "2":
                    list_customers()
                else:
                    print("Invalid choice.")
            elif choice == "4":
                if user["role"] != "admin":
                    print("Admin permission required.")
                else:
                    record_purchase()
            elif choice == "5":
                make_sale(user["id"])
            elif choice == "6":
                show_low_stock()
            elif choice == "7":
                sales_report()
            elif choice == "8":
                profit_report()
            elif choice == "9":
                export_sales_report()
            elif choice == "10" and user["role"] == "admin":
                add_staff()
            elif choice == "0":
                print("Logged out.")
                break
            else:
                print("Invalid choice.")
        except Exception as error:
            print(f"Operation failed: {error}")
            print("Please check your input and database connection. No partial sale/purchase should be saved.")

def main():
    print("Starting VyaparMitra...")
    try:
        initialize_database()
    except Exception as error:
        print(f"Cannot connect to MySQL or initialize tables: {error}")
        print("Check MySQL is running and update DB_CONFIG in database.py.")
        return
    while True:
        print("\n1. Login\n0. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            user = login()
            if user:
                main_menu(user)
        elif choice == "0":
            print("Thank you for using VyaparMitra.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
