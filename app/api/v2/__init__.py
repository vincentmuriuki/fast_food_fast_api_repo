from flask import Flask, Blueprint
from flask_restful import Api

# Local Import
from instance.config import app_config
# from app.api.v1.views import Orders, OrdersManipulation, LandingPage
# from app.api.v1.views import SingleOrder, PostOrder, GetOrders
from app.api.v2.views.users import UserRegistration, UserLogin, UserLogout
from app.api.v2.views.order_views import PostOrder, RetrieveAllOrders, DeleteOrder, UserOrderHistory, RetrieveSpecificOrder, UpdateOrderStatus, RetrieveAvailableMenu, AddMenuOptions

v1 = Blueprint('v1', __name__, url_prefix='/api/v1')
v2 = Blueprint('v2', __name__, url_prefix='/api/v2')

def create_app(config_stage):

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_stage])
    #app.config.from_pyfile('config.py')
    api = Api(app)

    # api.add_resource(SingleOrder, '/api/v1/orders/<int:id>')
    # api.add_resource(PostOrder, '/api/v1/orders')
    # api.add_resource(GetOrders, '/api/v1/orders')
    api.add_resource(UserRegistration, '/api/v2/auth/signup')    
    api.add_resource(UserLogin, '/api/v2/auth/login')
    api.add_resource(PostOrder, '/api/v2/users/orders')
    api.add_resource(RetrieveAllOrders, '/api/v2/orders')
    api.add_resource(DeleteOrder, '/api/v2/orders/<order_id>')
    api.add_resource(UserOrderHistory, '/api/v2/users/orders')
    api.add_resource(RetrieveSpecificOrder, '/api/v2/orders/<order_id>')
    api.add_resource(UpdateOrderStatus, '/api/v2/orders/<order_id>')
    api.add_resource(RetrieveAvailableMenu, '/api/v2/menu')
    api.add_resource(AddMenuOptions, '/api/v2/menu')


    return app