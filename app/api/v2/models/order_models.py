from datetime import datetime

# from app.api.v2.database.fastfood_tables import dbconn
from app.api.v2.database.tables import dbconn

class Orders:
    table = 'orders'

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.date_created = datetime.now()
        self.status = 'Pending'

    def __repr__(self):
        return f'<Order {self.name}'

    def add_to_list(self):
        return {
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price,
            'date_created': self.date_created,
            'status': self.status
        }

    def add_order(self):
        order = Orders(self.name,
                       self.quantity,
                       self.price)
        pass

    
    @classmethod
    def find_by_id(cls, order_id):
        pass

    @staticmethod
    def delete(order_id):
        pass

    @staticmethod
    def delete_all():
        pass