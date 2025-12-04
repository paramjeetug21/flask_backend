from src.auth import create_app
from src.profiles import init_profiles
from flask_cors import CORS

# ------------------------
# Create Flask app
# ------------------------
app = create_app()

# ------------------------
# Initialize blueprints
# ------------------------
init_profiles(app)

# ------------------------
# CORS configuration
# ------------------------
frontend_origin = "http://localhost:5173"  # change to your live frontend URL in production
# Apply CORS after blueprints so all routes get headers
CORS(app, origins=[frontend_origin], supports_credentials=True)

# ------------------------
# Run locally for testing only
# ------------------------
if __name__ == "__main__":
    # Local dev server; Vercel will handle production automatically
    app.run(debug=True)
