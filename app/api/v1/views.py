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
