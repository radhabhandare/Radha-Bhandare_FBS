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
    add_staff,
    list_staff
)
from reports import sales_report, export_sales_csv
def products_menu(user):
    while True:
        print('\n--- PRODUCTS ---')
        print('1. List products')

        if user['role'] == 'admin':
            print('2. Add product')
            print('3. Update product')

        print('0. Back')

        choice = input('Choose an option: ').strip()

        if choice == '1':
            list_products()

        elif choice == '2' and user['role'] == 'admin':
            add_product()

        elif choice == '3' and user['role'] == 'admin':
            update_product()

        elif choice == '0':
            break

        else:
            print('Invalid choice or permission denied.')
def suppliers_menu():
    while True:
        print('\n--- SUPPLIERS ---')
        print('1. Add supplier')
        print('2. List suppliers')
        print('0. Back')

        choice = input('Choose an option: ').strip()

        if choice == '1':
            add_supplier()

        elif choice == '2':
            list_suppliers()

        elif choice == '0':
            break

        else:
            print('Invalid choice.')

def customers_menu(user):
    while True:
        print('\n--- CUSTOMERS ---')

        if user['role'] == 'admin':
            print('1. Add customer')

        print('2. List customers')
        print('0. Back')

        choice = input('Choose an option: ').strip()

        if choice == '1' and user['role'] == 'admin':
            add_customer()

        elif choice == '2':
            list_customers()

        elif choice == '0':
            break

        else:
            print('Invalid choice or permission denied.')
def reports_menu():
    while True:
        print('\n--- REPORTS ---')
        print('1. Low-stock report')
        print('2. Daily sales report')
        print('3. Export products to CSV')
        print('4. Export sales to CSV')
        print('0. Back')

        choice = input('Choose an option: ').strip()

        if choice == '1':
            show_low_stock()

        elif choice == '2':
            sales_report()

        elif choice == '3':
            export_products_csv()

        elif choice == '4':
            export_sales_csv()

        elif choice == '0':
            break

        else:
            print('Invalid choice.')
def staff_menu():
    while True:
        print('\n--- MANAGE STAFF ---')
        print('1. Add staff account')
        print('2. View staff accounts')
        print('0. Back')

        choice = input('Choose an option: ').strip()

        if choice == '1':
            add_staff()

        elif choice == '2':
            list_staff()

        elif choice == '0':
            break

        else:
            print('Invalid choice.')
def menu(user):
    while True:
        print('\n========== VYAPARMITRA ==========')
        print(f"Welcome, {user['username']}!")
        print(f"Role: {user['role'].upper()}")

        print('\nMAIN MENU')
        print('1. Products')

        if user['role'] == 'admin':
            print('2. Suppliers')

        print('3. Customers')

        if user['role'] == 'admin':
            print('4. Record Purchase')

        print('5. Sales and Billing')
        print('6. Reports')

        if user['role'] == 'admin':
            print('7. Manage Staff')

        print('0. Logout')

        choice = input('\nChoose an option: ').strip()

        try:
            if choice == '1':
                products_menu(user)

            elif choice == '2' and user['role'] == 'admin':
                suppliers_menu()

            elif choice == '3':
                customers_menu(user)

            elif choice == '4' and user['role'] == 'admin':
                record_purchase()

            elif choice == '5':
                make_sale(user['id'])

            elif choice == '6':
                reports_menu()

            elif choice == '7' and user['role'] == 'admin':
                staff_menu()

            elif choice == '0':
                print('Logged out successfully.')
                break

            else:
                print('Invalid choice or permission denied.')

        except Exception as error:
            print(f'Operation failed: {error}')
def main():
    try:
        initialize_database()
    except Exception as error:
        print(f'MySQL connection/setup failed: {error}')
        print('Check that MySQL is running and DB_CONFIG is correct.')
        return

    while True:
        print('\n========== VYAPARMITRA LOGIN ==========')
        print('1. Login')
        print('0. Exit')

        choice = input('Choose an option: ').strip()

        if choice == '1':
            user = login()

            if user:
                menu(user)

        elif choice == '0':
            print('Thank you for using VyaparMitra.')
            break

        else:
            print('Invalid choice.')


if __name__ == '__main__':
    main()
