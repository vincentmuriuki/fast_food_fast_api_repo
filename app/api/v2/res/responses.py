from flask import make_response, jsonify


class Feedback:
    @staticmethod
    def orders_defn(order):
        obj = {
            'order_id': order['order_id'],
            'name': order['name'],
            'price': order['price'],
            'date_created': order['date_created'],
            'created_by': order['created_by'],
            'status': order['status']}
        return obj

    @staticmethod
    def users_defn(user):
        obj = {
            'user_id': user['user_id'],
            'username': user['username'],
            'email': user['email'],
            'role': user['role'],
            'password': user['password'],
            'date_registered': user['date_registered']
        }
        return obj

    @staticmethod
    def category_defn(category):
        obj = {
            'category_id': category['category_id'],
            'name': category['name'],
            'description': category['description'],
            'date_created': category['date_created']
        }
        return obj

    @staticmethod
    def request_completion(message):
        res = jsonify({"status": "OK", "message": message})
        return make_response(res), 200

    @staticmethod
    def make(message):
        res = jsonify({"status": "Created", "message": message})
        return make_response(res), 201


class TokenAuth:
    @staticmethod
    def user_creation(message, token):
        res = jsonify({"status": "User successfuly created!",
                            "message": message, "access_token": token})
        return make_response(res), 201

    @staticmethod
    def finish_request(message, token):
        res = jsonify({"status": "OK",
                            "message": message, "access_token": token})
        return make_response(res), 200

class ResConflict(Exception):
    def __init__(self, message):
        self.message = make_response(jsonify({"status": "Resource Conflict!",
                                              "message": message}), 409)
class UserUnauthorized(Exception):
    def __init__(self, message):
        self.message = make_response(jsonify({"status": "Unauthorized! Acquire rights first.",
                                              "message": message}), 401)

class NotFound(Exception):
    def __init__(self, message):
        self.message = make_response(jsonify({"status": "Resource Not Found!",
                                              "message": message}), 404)

class InvalidReq(Exception):
    def __init__(self, message):
        self.message = make_response(jsonify({"status": "Invalid request!", "message": message}), 400)