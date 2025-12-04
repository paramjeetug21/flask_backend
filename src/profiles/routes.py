from flask import Blueprint, request, jsonify
from .models import create_profile, get_profiles_by_user, get_profile_by_id, update_profile, delete_profile

profile_bp = Blueprint("profile_bp", __name__)

# Create profile
@profile_bp.route("/", methods=["POST"])
def add_profile():
    data = request.json
    user_id = data.get("user")
    if not user_id:
        return jsonify({"error": "User ID required"}), 400

    result = create_profile(user_id, data)
    return jsonify({"message": "Profile created", "profile_id": str(result.inserted_id)}), 201

# Get all profiles for a user
@profile_bp.route("/user/<user_id>", methods=["GET"])
def list_profiles(user_id):
    profiles = get_profiles_by_user(user_id)
    for p in profiles:
        p["_id"] = str(p["_id"])
        p["user"] = str(p["user"])
    print("profiles=", profiles)
    return jsonify(profiles), 200

# Get single profile
@profile_bp.route("/<profile_id>", methods=["GET"])
def get_profile(profile_id):
    profile = get_profile_by_id(profile_id)
    if not profile:
        return jsonify({"error": "Profile not found"}), 404
    profile["_id"] = str(profile["_id"])
    profile["user"] = str(profile["user"])
    print("profile=", profile)
    return jsonify(profile), 200

# Update profile
@profile_bp.route("/<profile_id>", methods=["PUT"])
def edit_profile(profile_id):
    data = request.json
    update_profile(profile_id, data)
    print("data=>",data)
    return jsonify({"message": "Profile updated"}), 200

# Delete profile
@profile_bp.route("/<profile_id>", methods=["DELETE"])
def remove_profile(profile_id):
    delete_profile(profile_id)
    return jsonify({"message": "Profile deleted"}), 200

