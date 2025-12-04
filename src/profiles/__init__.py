from flask_pymongo import PyMongo

mongo = PyMongo()   # this will be initialized by init_profiles()

def init_profiles(app):
    mongo.init_app(app)

    from .routes import profile_bp
    app.register_blueprint(profile_bp, url_prefix="/profile")
