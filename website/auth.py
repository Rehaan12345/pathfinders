from flask import Flask, render_template, url_for, redirect, request, Blueprint
from pymongo import MongoClient, UpdateOne
from bson.objectid import ObjectId
from .models import users

auth = Blueprint("auth", __name__)

# Combines a 
def combining(str):
        final_str = ""
        if len(str) == 1:
            final_str = str[0]
        # elif len(str) == 2: 
        #     final_str += str[0] + " and " + str[1]
        else:
            for i in range(len(str)):
                if i == len(str) - 2:
                    final_str += str[len(str) - 2] + " and " + str[len(str) - 1]
                    break
                final_str += str[i] + " "
            ind_and = final_str.index("and")
            final_str = final_str[:ind_and]
        return final_str

@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/logout/<id>")
def logout(id):
    return render_template("logout.html")

@auth.route("/signup/<step>", methods=["GET", "POST"])
def signup(step):

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
            return render_template("signup.html", step="basicinfo") 
    
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
            return render_template("signup.html", step="morespecific", email=email)
    
    elif step == "confirm":
        if request.method == "POST":
            mentormentee = request.form.get("menteementor")
            race = request.form.getlist("race")
            religion = request.form.getlist("religion")
            gender = request.form.get("gender")
            languages = request.form.getlist("languages")
            academics = request.form.getlist("academics")
            email = request.form.get("email")
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
            return render_template("signup.html", step="confirm", mentormentee=mentormentee, race=race, religion=religion, gender=gender, languages=languages, academics=academics)
        
    elif step == "finish":
        if request.method == "POST":
            # NEED TO Upload all into DB (try catch, etc)
            print(f"firstname - {first_name}, lastname - {last_name}, dob - {date_of_birth}, email - {email}, mentormentee - {mentormentee}, race - {race}, religion - {religion}, gender - {gender}, languages - {languages}, academics - {academics}")
            # users.insert_one({"firstname": first_name, "lastname": last_name, "dob": date_of_birth, "email": email, "mentormentee": mentormentee, "race": race, "religion": religion, "gender": gender, "languages": languages, "academics": academics})
            print("66 - successfully confirmed")
            return render_template("signup.html", step="finish")
                
    return render_template("signup.html", step="basicinfo")

def update_first(first_name, last_name, date_of_birth, email):
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

    first_name = first_name
    last_name = last_name
    date_of_birth = date_of_birth
    email = email
    mentormentee = mentormentee
    race = race
    religion = religion
    gender = gender
    languages = languages
    academics = academics

    users.insert_one({"firstname": first_name, "lastname": last_name, "dob": date_of_birth, "email": email, "mentormentee": mentormentee, "race": race, "religion": religion, "gender": gender, "languages": languages, "academics": academics})

def update_second(first_name, last_name, date_of_birth, email, mentormentee, race, religion, gender, languages, academics):
    print("ok")
    