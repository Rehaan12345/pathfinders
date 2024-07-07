from flask import Flask, render_template, url_for, redirect, request, Blueprint, flash
# from pymongo import MongoClient, UpdateOne
# from bson.objectid import ObjectId
from .models import User, combining
from . import users
from flask_login import login_user, login_required, logout_user, current_user
from .forms import SignupForm, LoginForm


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
        if form.validate_on_submit:
            return render_template("signup.html", step="basicinfo", form=form)
    
    elif step == "morespecific":
        if form.validate_on_submit:
            first_name = form.firstname.data
            last_name = form.lastname.data
            # date_of_birth = form.dob.data
            email = form.email.data
            password = form.password.data
            confirmpassword = form.confirmpassword.data
            if password != confirmpassword:
                flash("Passwords don't match!", "error")
                return redirect("/signup/basicinfo")
            print(f"firstname - {first_name} lastname - {last_name} email - {email} password - {password}")
            # Creates the user the first time.
            users.insert_one({"firstname": first_name, "lastname": last_name, "email": email, "mentormentee": mentormentee, "password": password, "race": race, "religion": religion, "gender": gender, "languages": languages, "academics": academics})
            return render_template("signup.html", step="morespecific", email=email, form=form)
    
    elif step == "confirm":
        if request.method == "POST":
            mentormentee = form.mentormentee.data
            race = form.race.data
            religion = form.religion.data
            gender = form.gender.data
            languages = form.languages.data
            academics = form.academics.data
            email = form.email.data
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
            print(f"firstname - {first_name}, lastname - {last_name}, email - {email}, mentormentee - {mentormentee}, race - {race}, religion - {religion}, gender - {gender}, languages - {languages}, academics - {academics}")
            # users.insert_one({"firstname": first_name, "lastname": last_name, "dob": date_of_birth, "email": email, "mentormentee": mentormentee, "race": race, "religion": religion, "gender": gender, "languages": languages, "academics": academics})
            print("66 - successfully confirmed")
            flash("Account successfully created")
            return render_template("signup.html", step="finish", form=form)
                
    return render_template("signup.html", step="basicinfo", form=form)

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if current_user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        email = form.email.data
        password = form.password.data
        print(f"Login email - {email}")
        print(f"Login password - {password}")
        # for user in users.find():
        #     print(user)      
        # all_users = users.find()
        # for user in all_users:
        #     if user["email"] == email:
        #         if user["password"] == password:
        #             flash("Successfully signed in!", "success")
        #             login_user(user, remember=form.data.remember)
        #             return redirect("/")
        #         else:
        #             flash("Incorrect password", "error")
        #     else:
        #         flash("No user with this email.", "error")
        loginuser_json = users.find_one({'email': form.email.data})
        # if loginuser_json and bcrypt.check_password_hash(loginuser_json['password'], form.password.data):
        # Create a custom user and pass it to login_user:
        #     loginuser = User(loginuser_json)
        #     login_user(loginuser, remember=form.data.remember)
        #     return redirect("/")
        # else:
        #     flash('Login Unsuccessful. Please check username and password', 'error')
    # else:
    #     flash("Log In Failed", "error")

    return render_template("login.html", form=form)

@auth.route("/logout/<id>", methods=["GET", "POST"])
def logout(id):
    return render_template("logout.html")

@auth.route("/signupp", methods=["GET", "POST"])
def signupp():
    form = SignupForm()
    return render_template("signupp.html", form=form, step="basicinfo")
    