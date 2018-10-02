import os
from datetime import datetime
import json
from flask import Flask, request, jsonify
from flask_restful import reqparse, Resource, Api


# local library imports
from app.api.v2.models.user_models import User
from app.api.v2.views.fastfood_validators.user_creds import UserCredsValidators

from app.api.v2.models.user_models import User


user_creds = UserCredsValidators()
user_structure = User()


"""
This class defines user registration
"""
class SignUp(Resource):
	def post(self):
		parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, help="Email required to register!")
        parser.add_argument('password', type=str, help="Password required to register!")
        args = parser.parse_args()
        status = user_creds.get_user_email(args['email'])
        user_data = request.get_json()
        email = validate.check_email_validity(user_data['email'])
        password = validate.check_password_validity(user_data['password'])
        username = validate.check_username_validity(user_data['username'])
        hashed_password = generate_password_hash(password, method='sha256')
        new_email = user_models.check_if_user_exists(email)
        user_id = user_models.user_creation(username=username, email=new_email, address=data['address'], password=hashed_password, user_type=False)
        
        return(
            {
                "message":"User created successfully!",
                "user_id":user_id[0]
            }
        ), 201

class UserLogin(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, help="Please enter your email!")
        parser.add_argument('password', type=str, help="Enter your preferred password!")
        args = parser.parse_args()
        user_data = request.get_json()
        email = validate.check_email_validity(user_data['email'])
        password = validate.check_password_validity(user_data['password'])
        if not email or not password:
            return {"message" : "Login Unsuccessful!"}
        
        user = user_models.get_login_email(email)
        # print (user)
        if not user:
            return {"message" : "User not registered!"}
        else:
            hashed_password = user_models.get_user_password(email)
            print (hashed_password)

            user_id = user_models.get_user_id(email)
            if check_password_hash(hashed_password, password):
                token = jwt.encode(
                    {
                        "user_id":user_id,
                        "exp":dt.datetime.utcnow() + dt.timedelta(minutes=20),},
                    os.getenv("SECRET_KEY"),
                    algorithm="HS256")
                return(
                    {
                        'token':token.decode('UTF-8')})
            return {"message" : "Wrong pass!"} 