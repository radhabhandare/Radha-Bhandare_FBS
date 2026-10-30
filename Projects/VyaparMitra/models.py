class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
    def allowed_actions(self):
        return ["list_products", "make_sale", "reports"]

class Admin(User):
    def allowed_actions(self):
        return ["list_products", "add_product", "update_product", "manage_suppliers",
                "manage_customers", "record_purchase", "make_sale", "reports"]

class Staff(User):
    pass

class Product:
    def __init__(self, name, category, purchase_price, selling_price, quantity, reorder_level):
        self.name = name
        self.category = category
        self.purchase_price = purchase_price
        self.selling_price = selling_price
        self.quantity = quantity
        self.reorder_level = reorder_level
    def is_low_stock(self):
        return self.quantity <= self.reorder_level
