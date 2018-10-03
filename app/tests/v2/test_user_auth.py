# import unittest
# import json
# import string

# import psycopg2
# from flask import request
# from app.api.v2.db.db_connection import init_test_db
# from app import create_app
# from app.database import init_test_database, dismantle

# class TestFlaskAuthentication(unittest.TestCase):
#     """ This class contains all enpoint tests for authentication """

#     def setUp(self):
#             self.app = create_app("testing")
#             self.client = self.app.test_client()

#             self.user_creds = {
#                 "username":"Erick Wachira",
#                 "email":"ewachira254@gmail.com",
#                 "password":"asdfgh",
#                 "address":"Kawangware"
#             }

#             with self.app.app_context():
#                 self.db = init_test_db()

#     def auth_data(self, path='/api/v2/auth/signup', data={}):
#         """ This method holds neccesary data to facilitate the test for user signup """
#         if not data:
#             data = self.user_creds
#         return (
#             self.client.post(
#                 path, data=json.dumps(data), content_type='applications/json'
#             )
#         )

#     def test_user_signup(self):
#         """ This will test the user registration """
#         response = self.auth_data(data=self.user_creds)
#         self.assertEqual(response.status_code, 201)

#     def test_user_login(self):
#         """ This will test the user registration """
#         data = {
#             "email":self.user_creds['email'],
#             "password":self.user_creds['password']
#         }
#         response = self.client.post(
#             '/api/v2/auth/login', 
#             data=json.dumps(data), 
#             content_type="application/json"
#         )
#         self.assertEqual(response.status_code, 200)

#     def tearDown(self):
#         dismantle()


# if __name__ == "__main__":
#     unittest.main()

import unittest
import json
from app.api.v2 import create_app

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        # self.user_details ={
        # "username": "pro",
        # "email": "mail@mail.co",
        # "password": "passwor"
        # }
        with self.app.app_context():
            self.db = init_test_db()

    # def auth_data(self, path='/api/v2/auth/signup', user_data={}):
    #     if not data:
    #         user_data = self.user_details
    #     return (
    #         self.client.post(
    #             path, data=json.dumps(data), content_type='applications/json'
    #         )
    #     )

    def test_user_reg(self):
        data = {
        "username" : self.user_details['email'],
        "email" : self.user_details['email'],
        "password" : self.user_details['password']
        }
        # response = self.auth_data(data=self.user_details)
        response = self.client().post('/api/v2/auth/signup')
        self.assertEqual(response.status_code, 201)

    def test_user_login(self):
        """ This will test the user login """
        response = self.client().post('/api/v2/auth/login', 
            data=json.dumps({
                "username" : "vinc",
                "password" : "passwor",
                }),content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn("User logged In", str(response.data))

    def test_if_user_exists(self):
        response  = self.client().post('api/v2/auth/login', data=json.dumps({
            "email" : "Youth",
            "password" : "youth",
            }), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertIn("User does not exist", str(response.data))

    def tearDown(self):
        dismantle()

if __name__ == "__main__":
    unittest.main()