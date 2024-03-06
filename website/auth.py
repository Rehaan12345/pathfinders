from flask import Flask, render_template, url_for, redirect, request, Blueprint, flash
from pymongo import MongoClient, UpdateOne
from bson.objectid import ObjectId
from .models import User, combining
from . import users
from flask_login import login_user, login_required, logout_user, current_user
from .forms import SignupForm

auth = Blueprint("auth", __name__)

# @auth.route("/user", methods=["GET", "POST"])
# def signupp():
#     return User().signup()

@auth.route("/signup/<step>", methods=["GET", "POST"])
def signup(step):

    form = SignupForm()

    # Default values:
    first_name = ""
    last_name = ""
    date_of_birth = ""
    email = ""
    mentormentee = ""
    race = ""
    religion = ""
    gender = ""
    languages = ""
    academics = ""

    if step == "basicinfo":
        if request.method == "POST":
            return render_template("signup.html", step="basicinfo", form=form) 
    
    elif step == "morespecific":
        if request.method == "POST":
            first_name = request.form.get("firstname")
            last_name = request.form.get("lastname")
            date_of_birth = request.form.get("dob")
            email = request.form.get("email")
            password = request.form.get("password")
            confirmpassword = request.form.get("confirmpassword")
            if password != confirmpassword:
                #flash
                return redirect("/signup/basicinfo")
            print(f"firstname - {first_name} lastname - {last_name} dateofbirth - {date_of_birth} email - {email} password - {password}")
            # Creates the user the first time.
            users.insert_one({"firstname": first_name, "lastname": last_name, "dob": date_of_birth, "email": email, "mentormentee": mentormentee, "password": password, "race": race, "religion": religion, "gender": gender, "languages": languages, "academics": academics})
            return render_template("signup.html", step="morespecific", email=email, form=form)
    
    elif step == "confirm":
        if request.method == "POST":
            mentormentee = request.form.get("menteementor")
            race = request.form.getlist("race")
            religion = request.form.getlist("religion")
            gender = request.form.get("gender")
            languages = request.form.getlist("languages")
            academics = request.form.getlist("academics")
            email = request.form.get("email")
            # password = request.form.get("password") # Also have to add the confirm password verification.
            print(f"72 - {email}")
            race = combining(race)
            religion = combining(religion)
            languages = combining(languages)
            academics = combining(academics)
            print(f"77 - mentormentee - {mentormentee} race - {race} religion - {religion} gender - {gender} languages - {languages} academics - {academics}")
            users.update_one({"email": email}, {"$set": {"mentormentee": mentormentee}})
            users.update_one({"email": email}, {"$set": {"race": race}})
            users.update_one({"email": email}, {"$set": {"religion": religion}})
            users.update_one({"email": email}, {"$set": {"gender": gender}})
            users.update_one({"email": email}, {"$set": {"languages": languages}})
            users.update_one({"email": email}, {"$set": {"academics": academics}})
            # users.update_one({"email": email}, {"$set": {"password": password}})
            return render_template("signup.html", step="confirm", mentormentee=mentormentee, race=race, religion=religion, gender=gender, languages=languages, academics=academics, form=form)
        
    elif step == "finish":
        if request.method == "POST":
            # NEED TO Upload all into DB (try catch, etc)
            print(f"firstname - {first_name}, lastname - {last_name}, dob - {date_of_birth}, email - {email}, mentormentee - {mentormentee}, race - {race}, religion - {religion}, gender - {gender}, languages - {languages}, academics - {academics}")
            # users.insert_one({"firstname": first_name, "lastname": last_name, "dob": date_of_birth, "email": email, "mentormentee": mentormentee, "race": race, "religion": religion, "gender": gender, "languages": languages, "academics": academics})
            print("66 - successfully confirmed")
            flash("Account successfully created")
            return render_template("signup.html", step="finish", form=form)
                
    return render_template("signup.html", step="basicinfo", form=form)

@auth.route("/login", methods=["GET", "POST"])
def login():
    # form = LoginForm()
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        print(f"Login email - {email}")
        print(f"Login password - {password}")
        # for user in users.find():
        #     print(user)      
        all_users = users.find()
        for user in all_users:
            if user["email"] == email:
                if user["password"] == password:
                    flash("Successfully signed in!", "success")
                    loginuser = User(user)
                    # login_user(user, remember=form.data.remember)
                    return redirect("/")
                else:
                    flash("Incorrect password", "error")
            else:
                flash("No user with this email.", "error")

    return render_template("login.html")

@auth.route("/logout/<id>", methods=["GET", "POST"])
def logout(id):
    return render_template("logout.html")

@auth.route("/signupp", methods=["GET", "POST"])
def signupp():
    form = SignupForm()
    return render_template("signupp.html", form=form, step="basicinfo")
    