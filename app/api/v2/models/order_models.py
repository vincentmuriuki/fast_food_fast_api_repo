from datetime import datetime

# from app.api.v2.database.fastfood_tables import dbconn
from app.api.v2.database.tables import dbconn

class Orders:
    table = 'orders'

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        self.date_created = datetime.now()
        self.status = 'Pending'

    def __repr__(self):
        return f'<Order {self.name}'

    def add_to_list(self):
        return {
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'date_created': self.date_created,
            'status': self.status
        }

    def add_order(self):
        order = Orders(self.name, self.price, self.description)
        pass
        
    @staticmethod
    def retrieve_list_all_orders():
        con = dbconn()
        curr = con.cursor()
        curr.execute("""SELECT * FROM orders""")
        orders = curr.fetchall()
        curr.close()
        con.close()

        return orders

    
    @classmethod
    def find_by_id(cls, order_id):
        pass

    @staticmethod
    def delete(order_id):
        pass

    @staticmethod
    def delete_all():
        pass