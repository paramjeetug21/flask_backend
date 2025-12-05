import os
from urllib.parse import quote_plus

class Config:
    
    
    MONGO_URI = f"mongodb+srv://paramjeet:Abcd%401234@cluster0.patrtp0.mongodb.net/flask_auth_db?retryWrites=true&w=majority"
    print("MONGO_URI=", MONGO_URI)
    # Secret key for Flask sessions
    SECRET_KEY = os.environ.get("SECRET_KEY", "your_secret_key_here")
