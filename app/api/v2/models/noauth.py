from datetime import datetime

from app.api.v2.database.dbcon import Connection, Database
# from app.api.v2.res.requirements import ProjectData
from app.api.v2.res.requirements import ProjectData

class NoAuth:
    summary = 'noauthlist'
    def __init__(self, token):
        self.token = token
        self.blacklisted_date = datetime.now()

    def __repr__(self):
        return '<token: {}'.format(self.token)

    def to_dict(self):
        return {
            'token': self.token,
            'blacklisted_date': self.blacklisted_date
        }

    def save(self):
        noauthlist = [self.token, 'now']
        query = """INSERT INTO blacklist (tokens, blacklisted_date) VALUES (%s, %s) RETURNING id"""
        return Database.postData(query, noauthlist)

    @staticmethod
    def check_token(self):
        """Check if token exists"""
        data = [self.token]
        query = """SELECT tokens::int FROM blacklist"""
        response = Database.find_one(query, data)
        if response:
            return True
        return False