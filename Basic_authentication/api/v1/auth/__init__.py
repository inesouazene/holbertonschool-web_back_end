#!/usr/bin/env python3
"""
Auth module for the API
"""
from flask import request
from typing import List, TypeVar

User = TypeVar('User')


class Auth:
    """
    Auth class to manage the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required for a given path

        Args:
            path: The path to check
            excluded_paths: List of paths that don't require authentication

        Returns:
            False - path and excluded_paths will be used later
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Gets the authorization header from the request

        Args:
            request: The Flask request object

        Returns:
            None - request will be the Flask request object
        """
        return None

    def current_user(self, request=None) -> User:
        """
        Gets the current user from the request

        Args:
            request: The Flask request object

        Returns:
            None - request will be the Flask request object
        """
        return None
