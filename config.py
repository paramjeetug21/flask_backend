import os
from urllib.parse import quote_plus

class Config:
    # Encode password to handle special characters like @
    PASSWORD = quote_plus("Abcd@1234")

    # Use encoded password in Mongo URI
    MONGO_URI = f"mongodb+srv://paramjeet:{PASSWORD}@cluster0.patrtp0.mongodb.net/flask_auth_db?retryWrites=true&w=majority"
    print("MONGO_URI=", MONGO_URI)
    # Secret key for Flask sessions
    SECRET_KEY = os.environ.get("SECRET_KEY", "your_secret_key_here")
