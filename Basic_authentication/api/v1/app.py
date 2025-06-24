#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
from flask import jsonify


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize the Auth variable
auth = None

# Load authentication based on environment variable AUTH_TYPE
auth_type = getenv('AUTH_TYPE')
if auth_type == 'auth':
    from api.v1.auth.auth import Auth
    auth = Auth()
elif auth_type == 'basic_auth':
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()


@app.before_request
def before_request() -> None:
    """ Before request handler that validates authentication
    """
    # Check if auth is initialized
    if auth is None:
        return None

    # Define paths that do not require authentication
    excluded_paths = ['/api/v1/status/', '/api/v1/unauthorized/',
                      '/api/v1/forbidden/']

    # Check if authentication is required for current path
    if not auth.require_auth(request.path, excluded_paths):
        return   # If not required, skip authentication checks

    # Check if the Authorization header is present
    if auth.authorization_header(request) is None:
        abort(401, description="Unauthorized access")  # If not, abort with 401

    # Check if the current user is authenticated
    if auth.current_user(request) is None:
        abort(403, description="Forbidden access")  # If not, abort with 403


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized handler
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5001")
    app.run(host=host, port=port)
