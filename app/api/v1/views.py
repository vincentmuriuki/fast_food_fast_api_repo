from flask import Flask, request
from flask_restful import Resource, reqparse

# local imports
from .models import CustomerOrders, food_orders


class PostOrder(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'name',
        type=str,
        required=True,
        help="Please fill out this field!"
        )
    parser.add_argument(
        'price',
        type=str,
        required=True,
        help="Please fill out this field!"
        )
    parser.add_argument(
        'description',
        type=str,
        required=True,
        help="Please fill out this field!"
        )

    def post(self):
        data = request.get_json()
        order = CustomerOrders(data['name'], data["price"],data['description'])
        food_orders.append(order)
        return {"message" : "Congratulations. Your new order has been posted. Kindly wait!"}, 201

class GetOrders(Resource):

    def get(self):
        return {"Orders":[order.order_details() for order in food_orders]},200 

class SingleOrder(Resource):
    def get(self, id):
        spec_order = CustomerOrders().retrieve_order_by_id(id)
        
        if spec_order:
            return {"order": spec_order.order_details()}, 200
        return {"message":"Order not found"}, 404

    def put(self, id):
        order = CustomerOrders().retrieve_order_by_id(id)
        if order:
            order.status="approved"
            return {"message":"status approved"}
        return {"message":"Order not found"}, 404


    def delete(self, id):
        spec_order = CustomerOrders().retrieve_order_by_id(id)
        if spec_order:
            food_orders.remove(spec_order)
            return {"Message" : "Requested Order deleted successfully!"},200
        return {"message" : "Requested Order not found! Try a different ID!"}, 404