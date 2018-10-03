import os
import psycopg2
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.exceptions import BadRequest, NotFound

from app.api.v2.db.db_connection import init_database

class UserModels(object):
    """ This class will hold all methods for user authentication """    
    def __init__(self):
        url = os.environ.get('URL')
        self.connection = psycopg2.connect(url)

    def email_exists(self, email):
        self.email = email
        curr = self.connection.cursor()
        curr.execute("SELECT * FROM users WHERE email='%s'" % self.email)
        existing_email = curr.fetchone()
        curr.close()
        if existing_email:
            raise BadRequest("User exists! Please choose another one")
        else:
            return self.email
                


    def user_creation(self, username, email, address, password, user_type = False):        
        self.username = username
        self.email = email
        self.address = address
        self.password = password
        self.user_type = user_type

        cursor = self.connection.cursor()
        cursor.execute("""INSERT INTO users (username, email, password, address) 
        VALUES (
            '%s', '%s', '%s', '%s'
        ) RETURNING user_id
        """ % (self.username, self.email, self.password, self.address))
        user_id = cursor.fetchone()
        self.connection.commit()
        # self.db.close()
        #GET USER
        cursor.execute("SELECT * FROM users WHERE email='%s'" % self.email)

        user = cursor.fetchone()
        print("User is" + str(user))

        return user_id

    def create_admin(self,username, email, password, address, user_type):
        self.username = username
        self.email = email
        self.address = address
        self.password = password
        self.user_type = user_type

        cursor = self.connection.cursor()
        cursor.execute("""INSERT INTO users (username, email, password, address) 
        VALUES (
            '%s', '%s', '%s', '%s'
        ) RETURNING user_id
        """ % (self.username, self.email, self.password, self.address))
        user_id = cursor.fetchone()
        self.connection.commit()
        
    def get_login_email(self, email):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email='%s'" % email)
        user = cursor.fetchone()
        # self.db.close()
        return user
 
    def login(self, email, password):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email='%s" % email)
        id = cursor.fetchone()
        # print(id)
        return id

    def get_user_password(self, email):
        cursor = self.connection.cursor()
        # query = """SELECT password FROM users WHERE email = '%s"email)s"""
        cursor.execute("SELECT * FROM users WHERE email='%s'" % email)
        # data = {'email': email}
        # cursor.execute(query, data)
        hashed_password = cursor.fetchone()[3]
        # self.db.close()
        return hashed_password

    def get_user_id(self, email):
        cursor = self.connection.cursor()
        cursor.execute("SELECT user_id FROM users WHERE email='%s'" % email)
        user_id = cursor.fetchone()
        # self.db.close()
        return user_id
   

    def get_user_creds_with_id(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id='%s'" % user_id)
        user_details = cursor.fetchone()
        # self.db.close()
        return user_details
        