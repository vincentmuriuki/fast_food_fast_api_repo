
from flask import Flask, request, jsonify, make_response
from flask_restful import reqparse, Resource, Api

from functools import wraps
# from jwt import get_jwt_identity

from app.api.v2.models.order_models import OrderModels
from app.api.v2.models.fastfood_users import UserModels
from app.api.v2.validators.validators import Validators
from app.api.v2.helpers.helpers import token_required
from app.api.v2.helpers.helpers import token_required


# validate = Validators()
# order_models = OrderModels()

# def admin_level(func):
# 	@wraps(func)
# 	def inner_function(*args, **kwargs):
# 		user = UserModels().get_user_creds_with_id(get_jwt_identity())

# 		if user.user_id



class PostOrder(Resource):
	
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('name', type=str, required=True, help="Food name is required!")
		parser.add_argument('description', type=str, required=True, help="Food description is required!")
		parser.add_argument('price', type=str, required=True, help="Price is required!")

		args = parser.parse_args()
		order_data = request.get_json()
		name = order_data['name']
		description = order_data['description']
		price = order_data['price']
		
		order_models = OrderModels(name=name, description=description, price=price)
		food_name = order_models.order_exists(name)
		# order_name = order_models.order_exists(name)
		order_id = order_models.order_creation()
		user_id = order_models.order_creation()
		return(
            {
                "message":"Order created successfully",
                "order_id":order_id[0],
                "user_id":user_id[0]
            }
        ), 201


class RetrieveAllOrders(Resource):
    def get(self):
        """
        Thus function retrieves all orders from the database
        Only Admin has access to this route
        """

        order = OrderModels.retrieve_all_orders()
        print("print",order)
        return ({"Orders" : order}), 200

class RetrieveSpecificOrder(Resource):
    def get(self, order_id):
        """
        This function get a specific order
        Only Admin has access to this route
        """
        #data = request.get_json()

        order = OrderModels.retrieve_specific_order(order_id)
        import pprint; pprint.pprint("here")
        return {"order": order}
		



class UpdateOrderStatus(Resource):
	def put(self, order_id):
		parser = reqparse.RequestParser()
		parser.add_argument('status', type=str, required=True, help="Status is required!")
		args = parser.parse_args()
		print(args)
		# order_data = request.get_json()
		status = args['status']
		# order_models = OrderModels(status=status, order_id=order_id)
		order = OrderModels.update_order_status(order_id, status)
		return order


class DeleteOrder(Resource):
	def delete(self, order_id):
		"""
		This function deletes an order from the database
		"""
		# order_models = OrderModels()
		order = OrderModels.delete_order(order_id)
		return order

class UserOrderHistory(Resource):
	def get(self, user_id):
		"""
		This function retrieves the order history for a particular user
		"""
		# order_models = OrderModels()
		order = OrderModels.get_user_order_history(user_id)
		return order


class RetrieveAvailableMenu(Resource):
	def get(self):
		menu = OrderModels.retrieve_available_menu()
		return ({"Menu" : menu}), 200

class AddMenuOptions(Resource):
	# @token_required
	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('name', type=str, required=True, help="Food name is required!")
		parser.add_argument('description', type=str, required=True, help="Food description is required!")
		parser.add_argument('price', type=str, required=True, help="Price is required!")

		args = parser.parse_args()
		menu_data = request.get_json()
		name = menu_data['name']
		description = menu_data['description']
		price = menu_data['price']
		
		order_models = OrderModels(name=name, description=description, price=price)
		menu_option_name = order_models.menu_item_exists(name)
		# order_name = order_models.order_exists(name)
		menu_id = order_models.menu_option_creation()
		# user_id = order_models.menu_option_creation()
		return(
            {
                "message":"Order created successfully",
                "menu_id":menu_id[0],
                
            }
        ), 201