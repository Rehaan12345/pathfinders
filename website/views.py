from flask import Flask, render_template, url_for, redirect, request, Blueprint
from pymongo import MongoClient
from bson.objectid import ObjectId
from . import users

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
    
@views.route("/findamentor", methods=["GET", "POST"])
def findamentor():
    return render_template("findamentor.html", mentors=users.find())

@views.route("/findamentee", methods=["GET", "POST"])
def findamentee():
    return render_template("findamentee.html")

@views.app_errorhandler(404)
def handle_404(err):
    return render_template("404.html"), 404

@views.app_errorhandler(500)
def handle_404(err):
    return render_template("500.html"), 500