#!/usr/bin/env python3
""" Auth module
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """ Auth class - template for all authentication systems
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determine if a given path requires authentication
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Normalize path to be slash tolerant
        if path[-1] != '/':
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path[-1] != '/':
                excluded_path += '/'
            if path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Return the value of the Authorization header, or None
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ Return None - to be overloaded by subclasses
        """
        return None

    def session_cookie(self, request=None):
        """ Return a cookie value from a request
        """
        if request is None:
            return None
        session_name = getenv('SESSION_NAME')
        return request.cookies.get(session_name)
