from flask_pymongo import PyMongo

# Just define the variable; don't initialize here
mongo = PyMongo()# Will initialize in __init__.py

class User:
    @staticmethod
    def create_user(name, email, password, profile_photo=None):
        user = {
            "name": name,
            "email": email,
            "password": password,  # stored as plain text
            "profile_photo": profile_photo
        }
        mongo.db.users.insert_one(user)
        return user

    @staticmethod
    def find_by_email(email):
        return mongo.db.users.find_one({"email": email})

    @staticmethod
    def verify_password(user, password):
        return user["password"] == password  # simple comparison

    @staticmethod
    def update_user(email, update_data):
        mongo.db.users.update_one(
            {"email": email},
            {"$set": update_data}
        )
