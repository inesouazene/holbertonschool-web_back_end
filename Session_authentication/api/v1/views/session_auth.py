#!/usr/bin/env python3
"""
Session authentication views
"""
from os import getenv
from flask import abort, jsonify, request, make_response
from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_login():
    """
    POST /api/v1/auth_session/login
    Handles user login via session authentication
    """
    # Get email and password from form data
    email = request.form.get('email')
    password = request.form.get('password')

    # Check if email is provided
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400

    # Check if password is provided
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400

    # Search for user by email
    users = User.search({"email": email})
    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]  # Get the first

    # Validate password
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth

    # Create session ID for the user
    session_id = auth.create_session(user.id)

    # Create response with user data
    response = make_response(jsonify(user.to_json()))

    # Set cookie with session ID
    session_name = getenv('SESSION_NAME')
    response.set_cookie(session_name, session_id)

    return response


@app_views.route('/auth_session/logout',
                 methods=['DELETE'], strict_slashes=False)
def session_logout():
    """
    DELETE /api/v1/auth_session/logout
    Handles user logout via session authentication
    """
    from api.v1.app import auth

    # Attempt to destroy the session
    if not auth.destroy_session(request):
        abort(404)

    # Return empty JSON dictionary with 200 status
    return jsonify({})
