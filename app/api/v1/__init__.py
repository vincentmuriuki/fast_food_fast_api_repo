# Library imports
from flask import Flask
from flask_restful import Api


# local imports
from instance.config import app_config
from .views import GetOrders
# SingleOrder, PostOrder, 

def create_app(config_stage):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_stage])

    api = Api(app)

#     api.add_resource(SingleOrder, '/api/v1/orders/<int:id>')
#     api.add_resource(PostOrder, '/api/v1/orders')
    api.add_resource(GetOrders, '/api/v1/orders')

    return app
