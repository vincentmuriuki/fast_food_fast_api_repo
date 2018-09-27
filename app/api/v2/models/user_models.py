from app.api.v2 import db
from flask_bcrypt import Bcrypt
from flask import current_app
import jwt
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

	def generate_token(self, user_id):
		"""
		Function to generate token that will be used as the Authorization header
		"""
		try:
			#set payload with an expiration time
			payload = {
			'exp': datetime.utcnow() + timedelta(minutes=3),
			'iat': datetime.utcnow(),
			'sub': user_id
			}
			# create a byte string token using the payload and the SECRET key
			jwt_string jwt.encode(
				payload,
				current_app.config.get('SECRET_KEY'),
				algorithm='HS256'
				)
			return jwt_string
		except Exception as e:
			# return an error in string format
			return str(e)

	@staticmethod
	def decode_token(token):
		"""
		Decode the access token from the authorization header
		"""
		try:
			payload = jwt.decode(token, current_app.config.get('SECRET_KEY'))
			return payload['sub']
		except jwt.ExpiredSignatureError:
			return "Expired token. Please login to get a new token!"
		except jwt.InvalidTokenError:
			return "Invalid token. Please register or login!"
