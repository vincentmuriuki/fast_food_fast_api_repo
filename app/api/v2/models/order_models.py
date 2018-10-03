


import os
import psycopg2
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequest, NotFound
from datetime import datetime
from app.api.v2.db.db_connection import init_database
from flask import jsonify



class OrderModels(object):
    """ This class will hold all methods for user authentication """
	url = os.environ.get('URL')
	connection = psycopg2.connect(url)
	@staticmethod        
	def retrieve_all_orders():
		cursor = OrderModels.connection.cursor()
		cursor.execute("SELECT * FROM orders")
		rows = cursor.fetchall()
		cursor.close()
		return rows