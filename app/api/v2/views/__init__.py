from flask import request, Blueprint
from flask.views import MethodView

#local imports
import app.api.v2.res.responses as UserErrors

from app.api.v2.models.user_models import User
from app.api.v2.res.requirements import Credentials
from app.api.v2.res.responses import TokenAuth

auth = Blueprint('auth', __name__)


class RegistrationView(MethodView):
    """This class-based view registers a new user and fetches all user."""

    def post(self):
        """API POST Requests for this view. Url ---> /v1/auth/register"""
        data = request.get_json(force=True)
        username = str(data['username'])
        email = str(data['email']).lower()
        password = data['password']
        confirm_password = data['confirm_password']
        try:
            User.validate_register_details(email, username, password, confirm_password)
            user = User.fetch_email(email)
            if not user:
                user = User(username=username, email=email, password=password)
                user_email = user.save()
                # generate access_token for user
                access_token = user.generate_token(user_email)
                return TokenAuth().user_creation(
                    'User {} successfully registered.'.format(user.email), access_token.decode())
            raise UserErrors.Conflict('User already exists! Please login.')

        except UserErrors.BadRequest as e:
            return e.message
        except UserErrors.Conflict as e:
            return e.message


class LoginView(MethodView):
    """This class-based view handles user login and access token generation"""

    def post(self):
        """API POST Requests for this view. Url ---> /v1/auth/login"""
        data = request.get_json(force=True)
        password = data['password']
        email = data['email']
        try:
            if not email:
                raise UserErrors.BadRequest('Your email is missing!')
            if not Utils.email_is_valid(email):
                raise UserErrors.Unauthorized('Your email is invalid! Kindly recheck your email.')

            user = User.fetch_email(email)
            user_role = User.fetch_role(email)
            if not user:
                raise UserErrors.NotFound('User does not exist. Kindly register!')
            else:
                if email and password:
                    password_hash = User.fetch_password(email)[0]
                    if Utils.check_hashed_password(password, password_hash):
                        access_token = User.generate_token(user_role)
                        if access_token:
                            return AuthResponse.complete_request(
                                'You have logged in successfully!', access_token.decode())
                    else:
                        raise UserErrors.BadRequest('Wrong Password!')
                else:
                    if not password:
                        raise UserErrors.BadRequest('Your password is missing!')
        except UserErrors.BadRequest as e:
            return e.message
        except UserErrors.NotFound as e:
            return e.message
        except UserErrors.Unauthorized as e:
            return e.message


registration_view = RegistrationView.as_view('register_view')
login_view = LoginView.as_view('login_view')

auth.add_url_rule('auth/register',
                  view_func=registration_view,
                  methods=['POST'])

auth.add_url_rule('auth/login',
                  view_func=login_view,
                  methods=['POST'])