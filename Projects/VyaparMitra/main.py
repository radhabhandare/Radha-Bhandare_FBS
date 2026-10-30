from database import initialize_database
from operations import (
    login,
    add_product,
    list_products,
    update_product,
    add_supplier,
    list_suppliers,
    add_customer,
    list_customers,
    record_purchase,
    make_sale,
    show_low_stock,
    export_products_csv,
)
from reports import sales_report, export_sales_csv

def menu(user):
    while True:
        print("\n... VYAPARMITRA ...")
        print("1. Products  2. Suppliers (admin)  3. Customers")
        print("4. Record purchase (admin)  5. Sales and billing")
        print("6. Reports and CSV exports  0. Logout")

        choice = input("Choose: ").strip()

        try:
            if choice == "1":
                while True:
                    print("\n--- PRODUCTS ---")
                    print("1. List products")
                    print("2. Add product (admin)")
                    print("3. Update product (admin)")
                    print("0. Back")

                    option = input("Choose: ").strip()

                    if option == "1":
                        list_products()
                    elif option == "2":
                        if user["role"] == "admin":
                            add_product()
                        else:
                            print("Only admin can add products.")
                    elif option == "3":
                        if user["role"] == "admin":
                            update_product()
                        else:
                            print("Only admin can update products.")
                    elif option == "0":
                        break
                    else:
                        print("Invalid choice.")

            elif choice == "2":
                if user["role"] != "admin":
                    print("Only admin can manage suppliers.")
                    continue

                while True:
                    print("\n--- SUPPLIERS ---")
                    print("1. Add supplier")
                    print("2. List suppliers")
                    print("0. Back")

                    option = input("Choose: ").strip()

                    if option == "1":
                        add_supplier()
                    elif option == "2":
                        list_suppliers()
                    elif option == "0":
                        break
                    else:
                        print("Invalid choice.")

            elif choice == "3":
                while True:
                    print("\n--- CUSTOMERS ---")
                    print("1. Add customer")
                    print("2. List customers")
                    print("0. Back")

                    option = input("Choose: ").strip()

                    if option == "1":
                        add_customer()
                    elif option == "2":
                        list_customers()
                    elif option == "0":
                        break
                    else:
                        print("Invalid choice.")

            elif choice == "4":
                if user["role"] == "admin":
                    record_purchase()
                else:
                    print("Only admin can record purchases.")

            elif choice == "5":
                make_sale(user["id"])

            elif choice == "6":
                while True:
                    print("\n--- REPORTS AND EXPORTS ---")
                    print("1. Low-stock report")
                    print("2. Daily sales report")
                    print("3. Export products to CSV")
                    print("4. Export all sales to CSV")
                    print("0. Back")

                    option = input("Choose: ").strip()

                    if option == "1":
                        show_low_stock()
                    elif option == "2":
                        sales_report()
                    elif option == "3":
                        export_products_csv()
                    elif option == "4":
                        export_sales_csv()
                    elif option == "0":
                        break
                    else:
                        print("Invalid choice.")

            elif choice == "0":
                print("Logged out.")
                break

            else:
                print("Invalid choice.")

        except Exception as error:
            print(f"Operation failed: {error}")


def main():
    try:
        initialize_database()
    except Exception as error:
        print(f"MySQL connection/setup failed: {error}")
        print("Check that MySQL is running and DB_CONFIG in database.py is correct.")
        return

    while True:
        print("\n--- VYAPARMITRA LOGIN ---")
        print("1. Login")
        print("0. Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            user = login()
            if user:
                menu(user)
        elif choice == "0":
            print("Thank you for using VyaparMitra.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
