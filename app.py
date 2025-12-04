from src.auth import create_app
from src.profiles import init_profiles
from flask_cors import CORS

app = create_app()

# Enable full CORS for ALL routes
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# Correct: after_request MUST be directly above the function
@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    return response

# Register profile blueprint AFTER decorators, NOT inside them
init_profiles(app)

if __name__ == "__main__":
    app.run(debug=True)
