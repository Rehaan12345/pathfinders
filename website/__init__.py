from flask import Flask, render_template, url_for, redirect, request, Blueprint
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask_sqlalchemy import SQLAlchemy
from os import path 
from flask_login import LoginManager 
# If doesn't work - pip install werkzeug==2.3.0
from flask_admin import Admin 
from flask_admin.contrib.sqla import ModelView
from flask_mail import Mail, Message
from .models import User

client = MongoClient("localhost", 27017)

# Creating the mongodb database
db = client.flask_database

users = db.users

def create_app():
    app = Flask(__name__) 
    app.config["SECRET_KEY"] = "rehaan"

    from .views import views
    from .auth import auth

    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    all_users = db.users.find()

    @login_manager.user_loader # Source: https://stackoverflow.com/questions/53401996/attributeerror-dict-object-has-no-attribute-is-active-pymongo-and-flask
    def load_user(user_id):
        users = db.users
        try:
            user_json = users.find_one({'_id': ObjectId(user_id)})
            return User(user_json)
        except: print("37 - Failed")
        # user_json = users.find_one({'_id': ObjectId(user_id)})
        # return User(user_json)

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
