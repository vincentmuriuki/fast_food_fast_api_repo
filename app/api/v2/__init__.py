
from flask import Flask, Blueprint, request, jsonify
from flask_restful import Api
import json

from instance.config import app_config

# local imports
from app.api.v2.views.customer_views import RegisterUser
from app.api.v2.views.order_views import Orders, order_manipulation

def create_app(config_stage):
    from app.api.v2.models.user_models import User
    from app.api.vs.models.order_models import Orders
    app = Flask(__name__, instance_relative_config=True)
    bcrypt = Bcrypt(app)

    app.config.from_object(app_config[config_stage])
    app.config.from_pyfile('config.py')


    db.init_app(app)
    from app.api.v2.views.customer_views.RegisterUser
    api.add_resource(SingleOrder, '/api/v1/orders/<int:id>')
    api.add_resource(PostOrder, '/api/v1/orders')
    api.add_resource(GetOrders, '/api/v1/orders')
    api.add_resource(RegisterUser, '/api/v2/auth/register')

    return app