from sqlite3 import connect
from types import ClassMethodDescriptorType
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

db = 'email_validation_schema'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (email) VALUES (%(email)s);"

        user = connectToMySQL(db).query_db(query, data)

    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"

        results = connectToMySQL(db).query_db(query)

        users = []

        for row in results:
            users.append(cls(row))

        return users

    @classmethod
    def get_last_user(cls):
        query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
        results = connectToMySQL(db).query_db(query)
        user = cls(results[0])

        return user

    # =======================

    @staticmethod
    def validate_user(user):
        is_valid = True
        if not EMAIL_REGEX.match(user['email']):
            flash("Email is not valid!")
            is_valid = False
        return is_valid
    
