from app.api.v2.database.dbcon import init_database
import jwt

from datetime import datetime, timedelta


class User(object):
	
	"""
	class to define a users table
	"""
	def __init__(self):
		url = os.environ.get('URL')
		self.connection = psycopg2.connect(url)

	def check_if _user_exists(self, email):
		self.email = email
        	curr = self.connection.cursor()
        	curr.execute("SELECT * FROM users WHERE email='%s'" % self.email)
        	registered_email = curr.fetchone()
        	curr.close()
        	if registered_email:
            		return {"message" : "The email has already been registered. Please try logging in!"}
        	else:
            		return self.email

	def user_creation(self, username, email, location, password, role = False):        
        	self.username = username
        	self.email = email
        	self.location = location
        	self.password = password
        	self.role = role

        	curr = self.connection.cursor()
        	curr.execute("""INSERT INTO users (username, email, password, location, role) 
        	VALUES ('%s', '%s', '%s', '%s', '%s') RETURNING customer_id
        	""" % (self.username, self.email, self.password, self.location, self.user))
        	customer_id = curr.fetchone()
        	self.connection.commit()
        	curr.execute("SELECT * FROM users WHERE email='%s'" % self.email)

        	customer = curr.fetchone()
        	print("Welcome" + str(customer))

        	return customer		
	
	def user_login(self, email, password):
        	curr = self.connection.cursor()
        	curr.execute("SELECT * FROM users WHERE email='%s" % email)
        	customer_id = curr.fetchone()
        	return customer_id


	def get_user_email(self, email):
        	curr = self.connection.cursor()
        	curr.execute("SELECT * FROM users WHERE email='%s'" % email)
        	fastfood_user = curr.fetchone()
        	# self.connection.close()
        	return fastfood_user


    	def retrieve_user_password(self, email):
        	curr = self.connection.cursor()
        	# query = """SELECT password FROM users WHERE email = '%s"email)s"""
        	curr.execute("SELECT * FROM users WHERE email='%s'" % email)
        	# data = {'email': email}
        	# curr.execute(query, data)
        	hashed_password = curr.fetchone()[3]
        	# it checks the index
        	# self.db.close()
        	return hashed_password

	def retrieve_customer_id(self, email):
        	curr = self.connection.cursor()
        	curr.execute("SELECT customer_id FROM users WHERE email='%s'" % email)
        	customer_id = curr.fetchone()
        	# self.connection.close()
        	return customer_id
   
	def customer_det(self, customer_id):
        	curr = self.connection.cursor()
        	curr.execute("SELECT * FROM users WHERE customer_id='%s'" % customer_id)
        	customer_details = curr.fetchone()
        	# self.db.close()
        	return customer_details
