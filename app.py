from src.auth import create_app
from src.profiles import init_profiles
from flask import request, make_response
from flask_cors import CORS

app = create_app()
init_profiles(app)

# Apply global CORS
CORS(app, supports_credentials=True)

# Handle preflight requests for serverless/Vercel
@app.before_request
def handle_options_requests():
    if request.method == "OPTIONS":
        response = make_response()
        origin = request.headers.get("Origin", "*")
        response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response.headers["Access-Control-Allow-Credentials"] = "true"
        response.status_code = 200
        return response

if __name__ == "__main__":
    app.run(debug=True)
