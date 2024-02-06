from flask import Flask, render_template, url_for, redirect, request, Blueprint
from pymongo import MongoClient
from bson.objectid import ObjectId
from .models import users

views = Blueprint("views", __name__)

@views.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user = request.form.get("user")
        users.insert_one( {"content": user} )
        all_users = users.find()
        return render_template("layout.html", users=all_users)
    
    all_users = users.find()
    return render_template("layout.html", users=all_users)

@views.route("/<id>/delete", methods=["GET", "POST"])
def delete(id):
    if request.method == "POST":
        users.delete_one({"_id":ObjectId(id)})
        return redirect("/")