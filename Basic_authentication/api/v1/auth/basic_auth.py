#!/usr/bin/env python3
""" BasicAuth module
"""
import base64
from typing import TypeVar, Tuple
from api.v1.auth.auth import Auth
from models.user import User


class BasicAuth(Auth):
    """ BasicAuth class - implements Basic Authentication
    """

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ Return the Base64 part of the Authorization header
            for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[len("Basic "):]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ Return the decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(
                base64_authorization_header, validate=True)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str
    ) -> Tuple[str, str]:
        """ Return the user email and password from the Base64
            decoded value
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        user_email, user_pwd = decoded_base64_authorization_header.split(
            ':', 1)
        return (user_email, user_pwd)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ Return the User instance based on his email and password
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        try:
            users = User.search({'email': user_email})
        except Exception:
            return None

        if not users or len(users) == 0:
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Overloads Auth and retrieves the User instance for a request
        """
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None

        b64_auth_header = self.extract_base64_authorization_header(
            auth_header)
        if b64_auth_header is None:
            return None

        decoded_header = self.decode_base64_authorization_header(
            b64_auth_header)
        if decoded_header is None:
            return None

        user_email, user_pwd = self.extract_user_credentials(decoded_header)
        if user_email is None or user_pwd is None:
            return None

        return self.user_object_from_credentials(user_email, user_pwd)
