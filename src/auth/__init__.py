from flask import Flask
from flask_cors import CORS
from .router import auth_bp
from .models import mongo
from config import Config
from flask_pymongo import PyMongo

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    # Initialize Mongo with the app
    mongo.init_app(app)  # use init_app, don't overwrite mongo
     
    # Register blueprint
    app.register_blueprint(auth_bp, url_prefix="/auth")
from flask import Flask
from flask_cors import CORS
from .router import auth_bp
from .models import mongo
from config import Config
from flask_pymongo import PyMongo

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    # Initialize Mongo with the app
    mongo.init_app(app)  # use init_app, don't overwrite mongo
    @app.route("/test-mongo")
    def test_mongo():
        try:
            return {"databases": mongo.cx.list_database_names()}
        except Exception as e:
            return {"error": str(e)}  
    # Register blueprint
    app.register_blueprint(auth_bp, url_prefix="/auth")

    return app


