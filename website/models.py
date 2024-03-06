from flask import Flask, jsonify, request
from flask_login import UserMixin

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
# users = db.users

class User(UserMixin): # Source: https://stackoverflow.com/questions/53401996/attributeerror-dict-object-has-no-attribute-is-active-pymongo-and-flask
    def __init__(self, user_json):
        self.user_json = user_json

    def get_id(self):
        object_id = self.user_json.get("_id")
        return str(object_id)

# class User: # Source: https://www.youtube.com/watch?v=mISFEwojJmE&t=661s 

#     def signup(self):

#         user = {
#             "_id": "",
#             "firstname": request.form.get("firstname"), 
#             "lastname": request.form.get("lastname"),
#             "dob": request.form.get("dob"), 
#             "email": request.form.get("email"),
#             "mentormentee": request.form.get("mentormentee"),
#             "race": combining(request.form.getlist("race")),
#             "religion": combining(request.form.getlist("religion")), 
#             "gender": request.form.get("gender"),
#             "languages": combining(request.form.getlist("languages")),
#             "academics": combining(request.form.getlist("academics"))
#         }

#         return jsonify(user), 200