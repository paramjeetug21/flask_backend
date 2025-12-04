import os
from src.auth import create_app
from src.profiles import init_profiles
from flask import request, make_response
from flask_cors import CORS

app = create_app()
init_profiles(app)

# ----------------------------------------
# CORS CONFIG (local + production)
# ----------------------------------------
allowed_origins = [
    "http://localhost:5173",
    "https://flask-frontend-git-main-paramjeetug21s-projects.vercel.app"
]

CORS(
    app,
    resources={r"/*": {"origins": allowed_origins}},
    supports_credentials=True,
    allow_headers=["Content-Type", "Authorization"],
    methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"]
)

# ----------------------------------------
# PRE-FLIGHT HANDLER (OPTIONS requests)
# ----------------------------------------
@app.before_request
def handle_preflight():
    if request.method == "OPTIONS":
        response = make_response()
        origin = request.headers.get("Origin")
        if origin in allowed_origins:
            response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
        response.headers["Access-Control-Allow-Credentials"] = "true"
        return response, 200

# ----------------------------------------
# RENDER-SPECIFIC RUN
# ----------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render provides PORT
    app.run(host="0.0.0.0", port=port, debug=True)
