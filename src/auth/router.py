from flask import Blueprint, request, jsonify
from .models import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    profile_photo = data.get("photo")

    if User.find_by_email(email):
        return jsonify({"error": "User already exists"}), 400

    user = User.create_user(name, email, password, profile_photo)
    return jsonify({"message": "User created successfully", "user": {"name": user["name"], "email": user["email"]}}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = User.find_by_email(email)
    if not user or not User.verify_password(user, password):
        return jsonify({"error": "Invalid credentials"}), 401
    print("User logged in:", user)
    return jsonify({"message": "Login successful", "user": user}), 200

@auth_bp.route("/update-profile", methods=["PUT"])
def update_profile():
    data = request.json

    email = data.get("email")
    new_name = data.get("name")
    new_photo = data.get("profile_photo")

    if not email:
        return jsonify({"error": "Email is required"}), 400

    user = User.find_by_email(email)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Update data dictionary
    update_data = {}
    if new_name:
        update_data["name"] = new_name
    if new_photo:
        update_data["profile_photo"] = new_photo

    # Update in DB
    User.update_user(email, update_data)

    return jsonify({
        "message": "Profile updated successfully",
        "updated_user": {
            "name": update_data.get("name", user["name"]),
            "email": email,
            "profile_photo": update_data.get("profile_photo", user.get("profile_photo"))
        }
    }), 200
