from app.api.v2 import db
from flask import current_app

from datetime import datetime, timedelta


class User(db.Model):
    	"""
	class to define a users table
	"""
	__tablename__ = 'users'
	# user table columns
	user_id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(500), nullable=False, unique=True)
	password = db.Column(db.String(500), nullable=False)
	orders = db.relationship(
		'Orders', order_by='Orders.user_id', cascade="all, delete-orphan")

	def __init__(self, email, password):
		"""
		This initializes the user with email and password
		"""
		self.email = email
		self.password = Bcrypt().generate_password_hash(password).decode()

	def password_is_valid(self, password):
		"""
		This function checks 
		the validity of the password by checking it against it's hash
		"""
		return Bcrypt().check_password_hash(self.password, password)

	def save(self):
		"""Function to save user to the database
		"""
		db.session.add(self)
		db.session.commit()

	