
import time
import re

from abc import abstractmethod, ABCMeta
from passlib.handlers.pbkdf2 import pbkdf2_sha512


class Credentials:
    @staticmethod
    def valid_email(email):
        emai_addr_structure = re.compile('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        return True if emai_addr_structure.match(email) else False

    @staticmethod
    def check_password(password):
        check_password = re.match(r"^(?=.*[a-z])(?=.*[0-9]){6}", password)
        return True if check_password else False

    @staticmethod
    def check_username(username):
        check_username = re.match(r"(?=^.{3,}$)(?=.*[a-z])^[A-Za-z0-9_-]+( +[A-Za-z0-9_-]+)*$", username)
        return True if check_username else False

    @staticmethod
    def timestamp():
        return int(time.time())

    @staticmethod
    def hash_password(password):
        """
        Method to hash the password using sha 512
        """
        return pbkdf2_sha512.hash(password)

    @staticmethod
    def hashed_password_validity(password, hashed_password):
        """
        This returns the hashed password
        """
        return pbkdf2_sha512.verify(password, hashed_password)


class ProjectData(metaclass=ABCMeta):
    def save_user(self):
        collection = 'users'
        Database.insert(collection, self.to_dict())

    def save_order(self):
        collection = 'orders'
        Database.insert(collection, self.to_dict())

    def save_blacklist(self):
        collection = 'blacklist'
        Database.insert(collection, self.to_dict())

    def save_role(self):
        collection = 'role'
        Database.insert(collection, self.to_dict())

    def save_category(self):
        collection = 'category'
        Database.insert(collection, self.to_dict())

    @abstractmethod
    def to_dict(self):
        pass