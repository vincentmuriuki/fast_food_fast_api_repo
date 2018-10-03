import os
import psycopg2
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequest, NotFound
from datetime import datetime
from app.api.v2.db.db_connection import init_database
from flask import jsonify
import json

class OrderModels(object):
    """ This class will hold all methods for user authentication """
    url = os.environ.get('URL')
    connection = psycopg2.connect(url)

    def __init__(self, name, price, description, order_date=None):
        
        self.name = name
        self.price = price
        self.description = description
        # self.order_date = datetime.now()

    def order_id_exists(self, order_id):
        curr = self.connection.cursor()
        curr.execute("SELECT * FROM orders WHERE order_id='%s'" % order_id)
        order = curr.fetchone()
        curr.close()
        if order:
            return {
            "message" : "Order exists"
            }
        else:
            return order_id
       
    def order_creation(self):        
        cursor = self.connection.cursor()
        # cursor.execute("")
        cursor.execute("""INSERT INTO orders (name, price, description) 
        VALUES (
            '%s', '%s', '%s'
        ) RETURNING order_id
        """ % (self.name, self.price, self.description))
        order_id = cursor.fetchone()
        self.connection.commit()

        return order_id

    def menu_option_creation(self):
        cursor = self.connection.cursor()
        cursor.execute("""INSERT INTO meals (name, price, description) 
        VALUES (
            '%s', '%s', '%s'
        ) RETURNING meal_id
        """ % (self.name, self.price, self.description))
        meal_id = cursor.fetchone()
        self.connection.commit()
        return meal_id

    def menu_item_exists(self, name):
        self.name = name
        curr = self.connection.cursor()
        curr.execute("SELECT name FROM meals WHERE name='%s'" % self.name)
        found_meal = curr.fetchone()
        curr.close()
        if found_meal == True:
            return {
            "message" : "Order exists! Please make a new one"
            }
        else:
            return self.name

    def order_exists(self, name):
        self.name = name
        curr = self.connection.cursor()
        curr.execute("SELECT name FROM orders WHERE name='%s'" % self.name)
        existing_order = curr.fetchone()
        curr.close()
        if existing_order == True:
            return {
            "message" : "Order exists! Please make a new one"
            }
        else:
            return self.name

    # def get_login_email(self, email):
    #     cursor = self.connection.cursor()
    #     cursor.execute("SELECT * FROM users WHERE email='%s'" % email)
    #     user = cursor.fetchone()
    #     # self.db.close()
    #     return user
 
    # def login(self, email, password):
    #     cursor = self.connection.cursor()
    #     cursor.execute("SELECT * FROM users WHERE email='%s" % email)
    #     id = cursor.fetchone()
    #     # print(id)
    #     return id

    # def get_user_password(self, email):
    #     cursor = self.connection.cursor()
    #     # query = """SELECT password FROM users WHERE email = '%s"email)s"""
    #     cursor.execute("SELECT * FROM users WHERE email='%s'" % email)
    #     # data = {'email': email}
    #     # cursor.execute(query, data)
    #     hashed_password = cursor.fetchone()[3]
    #     # self.db.close()
    #     return hashed_password

    # def get_user_id(self, email):
    #     cursor = self.connection.cursor()
    #     cursor.execute("SELECT user_id FROM users WHERE email='%s'" % email)
    #     user_id = cursor.fetchone()
    #     # self.db.close()
    #     return user_id
   

    # def get_user_creds_with_id(self, user_id):
    #     cursor = self.connection.cursor()
    #     cursor.execute("SELECT * FROM users WHERE user_id='%s'" % user_id)
    #     user_details = cursor.fetchone()
    #     # self.db.close()
    #     return user_details
    @staticmethod
    def retrieve_order_history_for_particular_user(self):
        cursor = OrderModels.connection.cursor()
        cursor.execute("SELECT * FROM orders WHERE user_id='%s'" % self.user_id)
        order_data = cursor.fetchone()
        cursor.close()
        if order_data:
            return {
            "message" : "The order exists"
            }
        return self.user_id

    @staticmethod
    def retrieve_specific_order(order_id):
        cursor = OrderModels.connection.cursor()
        cursor.execute("SELECT * FROM orders WHERE order_id='%s'" % order_id)
        order_data = cursor.fetchall()
        import pprint; pprint.pprint(order_data)
        cursor.close()
        if order_data:
            return {
            "Order" : order_data
            }
            # return {"medbxbg": "cgvhbnm"}

    @staticmethod        
    def retrieve_all_orders():
        cursor = OrderModels.connection.cursor()
        cursor.execute("SELECT * FROM orders")
        rows = cursor.fetchall()
        # results = []
        cursor.close()
        # for a in rows:
        #     str(a)
        #     results.append(a)
        # return results
        length = len(rows)
        return {"message" : rows}
    @staticmethod
    def update_order_status(order_id, status):
        cursor = OrderModels.connection.cursor()
        cursor.execute("UPDATE orders SET status = 'Completed' WHERE order_id ='%s'" % (order_id))
        # order_data = cursor.fetchone()
        cursor.close()
        return {"status" : status}