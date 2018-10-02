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


    		
	