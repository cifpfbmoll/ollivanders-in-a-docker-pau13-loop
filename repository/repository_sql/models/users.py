from flask import g
from repository.repository_sql.models.db_model import db

# * FLASK_LOGIN: UserMixin
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(80))
    # email = db.Column(db.String(50), unique=True)

    def __init__(self, username, password):

        self.username = username
        # self.email = email
        self.password = password
