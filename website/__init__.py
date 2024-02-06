from flask import Flask, render_template, url_for, redirect, request, Blueprint
from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient("localhost", 27017)

# Creating the mongodb database
db = client.flask_database

def create_app():
    app = Flask(__name__) 

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
