from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from .models import User

auth_bp = Blueprint("auth", __name__)

# ----------------- SIGNUP -----------------
@auth_bp.route("/signup", methods=["POST", "OPTIONS"])
@cross_origin(origins="http://localhost:5173", supports_credentials=True)
def signup():
    if request.method == "OPTIONS":
        return jsonify({}), 200  # preflight

    data = request.json
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    profile_photo = data.get("photo")

    if User.find_by_email(email):
        return jsonify({"error": "User already exists"}), 400

    user = User.create_user(name, email, password, profile_photo)
    return jsonify({"message": "User created successfully", "user": {"name": user["name"], "email": user["email"]}}), 201


# ----------------- LOGIN -----------------
@auth_bp.route("/login", methods=["POST", "OPTIONS"])
@cross_origin(origins="http://localhost:5173", supports_credentials=True)
def login():
    if request.method == "OPTIONS":
        return jsonify({}), 200

    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = User.find_by_email(email)
    if not user or not User.verify_password(user, password):
        return jsonify({"error": "Invalid credentials"}), 401

    return jsonify({"message": "Login successful", "user": user}), 200


# --------------- UPDATE PROFILE ---------------
@auth_bp.route("/update-profile", methods=["PUT", "OPTIONS"])
@cross_origin(origins="http://localhost:5173", supports_credentials=True)
def update_profile():
    if request.method == "OPTIONS":
        return jsonify({}), 200

    data = request.json
    email = data.get("email")
    new_name = data.get("name")
    new_photo = data.get("profile_photo")

    if not email:
        return jsonify({"error": "Email is required"}), 400

    user = User.find_by_email(email)
    if not user:
        return jsonify({"error": "User not found"}), 404

    update_data = {}
    if new_name:
        update_data["name"] = new_name
    if new_photo:
        update_data["profile_photo"] = new_photo

    User.update_user(email, update_data)

    return jsonify({
        "message": "Profile updated successfully",
        "updated_user": {
            "name": update_data.get("name", user["name"]),
            "email": email,
            "profile_photo": update_data.get("profile_photo", user.get("profile_photo"))
        }
    }), 200
