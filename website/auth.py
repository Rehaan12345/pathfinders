from flask import Flask, render_template, url_for, redirect, request, Blueprint
from pymongo import MongoClient
from bson.objectid import ObjectId
from .models import users

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/logout/<id>")
def logout():
    return render_template("logout.html")

@auth.route("/signup")
def signup():
    return render_template("signup.html")