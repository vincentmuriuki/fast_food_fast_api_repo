from functools import wraps

from flask import request, make_response, jsonify

# local imports
from app.api.v2.models.noauth import NoAuth

from app.api.v2.models.user_models import User

def user_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        user_header_auth = request.headers.get('Authorization', None)
        if not user_header_auth:
            return make_response(jsonify({
                'error': 'No active auth tiken found for this session. Try logging in again'}), 401)
        else:
            token = user_header_auth.split("Bearer ")
            access_token = token[1]
            access_token = access_token.encode()
            if access_token:

                blacklisted = NoAuth.check_token(access_token)
                if not blacklisted:

                    response = User.decode_token(access_token)
                    if not isinstance(response, str):

                        user_id = User.find_by_id(user_id=response)
                    else:
                        return make_response(jsonify({'message': response}), 201)
                else:
                    return make_response(jsonify({'error': 'We cannot log you in due to issues with your auth token!'}), 401)
            else:
                return make_response(jsonify({'error': 'Access token is mandatory for you to log in!'}), 401)
        return f(user_id=user_id, *args, **kwargs)
    return decorated


def admin_required():
    pass