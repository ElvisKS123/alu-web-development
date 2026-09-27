#!/usr/bin/env python3
""" Session Auth view module
"""
from os import getenv
from flask import jsonify, request
from api.v1.views import app_views
from models.user import User


@app_views.route(
    '/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login
    Return:
      - the JSON representation of the authenticated User
      - 400 if email or password is missing
      - 404 if no User found for the email
      - 401 if the password is wrong
    """
    email = request.form.get('email')
    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if not users or len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    response = jsonify(user.to_json())
    session_name = getenv('SESSION_NAME')
    response.set_cookie(session_name, session_id)

    return response
