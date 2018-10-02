







from flask import Flask, request, jsonify, make_response
from flask_restful import reqparse, Resource, Api


from app.api.v2.models.order_models import OrderModels


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
        order_id = order_models.order_creation()
        return(
            {
                "message":"Order created successfully",
                "order_id":order_id[0]
            }
        ), 201