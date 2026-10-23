from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username

    @abstractmethod
    def allowed_actions(self):
        pass

class Admin(User):
    def allowed_actions(self):
        return ["products", "suppliers", "customers", "purchases", "sales", "reports", "users"]

class Staff(User):
    def allowed_actions(self):
        return ["products", "customers", "sales", "reports"]

class Product:
    def __init__(self, name, category, purchase_price, selling_price, quantity, reorder_level=5):
        self.name = name
        self.category = category
        self.purchase_price = purchase_price
        self.selling_price = selling_price
        self.quantity = quantity
        self.reorder_level = reorder_level

    def is_low_stock(self):
        return self.quantity <= self.reorder_level
