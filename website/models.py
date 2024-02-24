from . import db
from flask import Flask, jsonify, request

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

# Users collection
users = db.users

class User:

    def signup(self):

        user = {
            "_id": "",
            "firstname": request.form.get("firstname"), 
            "lastname": request.form.get("lastname"),
            "dob": request.form.get("dob"), 
            "email": request.form.get("email"),
            "mentormentee": request.form.get("mentormentee"),
            "race": combining(request.form.getlist("race")),
            "religion": combining(request.form.getlist("religion")), 
            "gender": request.form.get("gender"),
            "languages": combining(request.form.getlist("languages")),
            "academics": combining(request.form.getlist("academics"))
        }

        return jsonify(user), 200