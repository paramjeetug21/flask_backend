from bson.objectid import ObjectId
from . import mongo   # use the mongo from __init__.py

def create_profile(user_id, profile_data):
    profile_data["user"] = ObjectId(user_id)
    return mongo.db.profiles.insert_one(profile_data)

def get_profiles_by_user(user_id):
    return list(mongo.db.profiles.find({"user": ObjectId(user_id)}))

def get_profile_by_id(profile_id):
    return mongo.db.profiles.find_one({"_id": ObjectId(profile_id)})

def update_profile(profile_id, data):
    # Convert profile_id to ObjectId
    profile_obj_id = ObjectId(profile_id)

    # Remove _id if it exists in the data, MongoDB cannot update _id
    data.pop("_id", None)

    # Convert user field to ObjectId if needed
    if "user" in data and isinstance(data["user"], str):
        data["user"] = ObjectId(data["user"])

    return mongo.db.profiles.update_one(
        {"_id": profile_obj_id},
        {"$set": data}
    )

def delete_profile(profile_id):
    return mongo.db.profiles.delete_one({"_id": ObjectId(profile_id)})
