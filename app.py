from src.auth import create_app
from src.profiles import init_profiles
from flask import make_response, request
from flask_cors import CORS

app = create_app()

# ------------------------
# CORS configuration
# ------------------------
# Allow only your frontend for credentials
frontend_origin = "http://localhost:5173"  # change to your live frontend URL in production
CORS(app, origins=[frontend_origin], supports_credentials=True)

# Optional: Handle preflight requests for serverless
@app.before_request
def handle_options_requests():
    if request.method == "OPTIONS":
        response = make_response()
        response.headers["Access-Control-Allow-Origin"] = frontend_origin
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response.status_code = 200
        return response

# ------------------------
# Initialize blueprints
# ------------------------
init_profiles(app)

# ------------------------
# Run locally for testing
# ------------------------
if __name__ == "__main__":
    app.run(debug=True)
