import re
import string

from werkzeug.exceptions import BadRequest, NotFound


class UseerCredSValidators(object):
    def __init__(self):
        pass 

    def check_email_validity(self, email):
        self.email = email
        if not re.match(r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
            email):
            raise BadRequest("Invalid email. Kindly use a correct email!")
        else:
            return self.email


    def check_password_validity(self, password):
        self.password = password

        if len(self.password) < 4:
            raise BadRequest("Your password is too short!")
        return self.password            
            