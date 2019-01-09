import os
import json
import datetime as dt

from flask import Flask, request, jsonify, make_response
from flask_restful import reqparse, Resource, Api
from werkzeug.exceptions import Conflict, Unauthorized, BadRequest
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

# local imports
from app.api.v2.models.fastfood_users import UserModels
from app.api.v2.validators.validators import Validators

user_models = UserModels()
validate = Validators()

class UserRegistration(Resource):
    """ This class holds the endpoint for user registration """
    
    # def get(self):
    #     return "This is the signup page"

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, help="Email required to log in!")
        parser.add_argument('password', type=str, help="Password required for log in!")
        parser.add_argument('user_type', type=bool, required=False, default=False)
        args = parser.parse_args()
        status = user_models.get_login_email(args['email'])
        # if status:
        #     if check_password_hash(status[3], args['password']):
                # auth_token = 
        data = request.get_json()
        email = validate.email_validator(data['email'])
        password = validate.password_validator(data['password'])
        username = validate.username_validator(data['username'])
        hashed_password = generate_password_hash(password, method='sha256')
        new_email = user_models.email_exists(email)
        user_id = user_models.user_creation(username=username, email=new_email, address=data['address'], password=hashed_password, user_type=data['user_type'])
        return(
            {
                "message":"User created successfully",
                "user_id":user_id[0]
            }
        ), 201

class UserLogin(Resource):

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, help="Email required to log in!")
        parser.add_argument('password', type=str, help="Password required for log in!")
        args = parser.parse_args()
        data = request.get_json()
        email = validate.email_validator(data['email'])
        password = validate.password_validator(data['password'])

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
                print(jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=['HS256']))
                
                return({'token':token.decode('UTF-8')})


            return {"message" : "Wrong pass!"}  

class UserLogout(Resource):
    """ This endpoint serves the logout of a user """
    pass



