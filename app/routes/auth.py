from flask import Blueprint, request

# Blueprint for all authentication-related routes under the `/auth` prefix.
auth_bp = Blueprint("auth" , __name__ , url_prefix="/auth")



# Simple health-check style endpoint for the auth blueprint.
@auth_bp.route("/")
def root():
    # Minimal JSON response to confirm the auth route is reachable.
    return {"message":"testing done"}

# Register a new user (placeholder implementation).
@auth_bp.route("/register", methods=["POST"])
def register():
    # Extract minimal registration details from the request body.
    payload = request.get_json(silent=True) or {}
    username = payload.get("username")
    email = payload.get("email")

    # Basic response for now; hook into real user-creation logic later.
    return {
        "message": "registration received",
        "username": username,
        "email": email,
    }, 201
