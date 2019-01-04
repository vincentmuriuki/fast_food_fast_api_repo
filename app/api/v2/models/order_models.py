from app.api.v2 import db
from flask_bcrypt import Bcrypt
from flask import current_app
import jwt
from datetime import datetime, timedelta


class Orders(db.Model):
	# table columns
	__tablename__ = 'customer_orders'

	order_id = db.Column(db.Integer, primary_key=True)
	ordered_by = db.Column(db.Integer, db.ForeignKey(User.user_id))
	order_date = db.Column(db.DateTime, default=db.func.current_timestamp())
	date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
		onupdate=db.func.current_timestamp())
	price = db.Column(db.String(500))
	name = db.Column(db.String(500))
	status = db.Column(db.Boolean)

	def __init__(self, name, price, status, ordered_by):
		self.name = name
		self.price = price
		self.status = status
		self.ordered_by = ordered_by

	def save(self):
		"""
		This function saves the order details
		"""
		db.session.add(self)
		db.session.commit()

	@staticmethod
	def get_all_user_orders(user_id):
		"""
		Function to retrieve all orders by a specific user
		"""
		return Order.query.filter_by(ordered_by=user_id)

	def delete(self):
		"""
		This function deletes a specific order given order_id
		"""
		db.session.delete(self)
		db.session.commit()

	def __repr__(self):
		"""
		This function returns a representation of an order
		"""
		return "<Order: {}>".format(self.name)
