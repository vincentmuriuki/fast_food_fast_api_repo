from flask import Flask, request
from flask_restful import    Resource

# local imports
from .models import Order, food_orders



class PostOrder(Resource):

    def post(self):
        data = request.get_json()
        order = Order(data['name'], data["price"],data['description'])
        food_orders.append(order)
        return {"message":"Congratulations. Your new order has been posted. Kindly wait!"}, 201

class GetOrders(Resource):
    def get(self):
        return {"Orders":[order.serialize() for order in food_orders]}

class SingleOrder(Resource):
    def get(self, id):
        spec_order = Order().retrieve_order_by_id(id)
        
        if spec_order:
            return {"order": spec_order.serialize()}, 200
        return {"message":"Order not found"}, 404