
import json
from flask_api import FlaskAPI
from flask import request, jsonify, abort, make_response
from instance.config import app_config
from flask_bcrypt import Bcrypt

#initialize the db

db = init_db()


@app.route('/api/v2/orders', methods=['POST', 'GET'])
def Orders():
    auth_header = request.headers.get('Authorization')
    access_token = auth_header.split(" ")[1]



    if access_token:
        user_id = User.decode_token(access_token)
        if not isinstace(user_id, str):
            if request.method == "POST":
                name = str(request.data.get('name', ''))
                if name:
                    order = Order(name=name, ordered_by=user_id)
                    order.save()
                    response = jsonify({
                            'order_id' : order.order_id,
                            'ordered_by' : order.ordered_by,
                            'order_date' : order.order_date,
                            'name' : order.name,
                            'price' : order.price,
                            'status' : order.status
                        })
                    return make_response(response), 201
                else:
                    order = Order.get_all(user_id)
                    results = []

                    for orders in customer_orders:
                        obj = {
                           'order_id' : order.order_id,
                            'ordered_by' : order.ordered_by,
                            'order_date' : order.order_date,
                            'name' : order.name,
                            'price' : order.price,
                            'status' : order.status
                        }
                        results.append(obj)

                    return make_response(jsonify(results)), 200
            else:
                message = user_id
                response = {
                        'message' : message
                }
                return make_response(jsonify(response)), 401
