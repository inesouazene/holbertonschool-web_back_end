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
            True if authentication is required, False otherwise
        """
        # Return True if path is None
        if path is None:
            return True

        # Return True if excluded_paths is None or empty
        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Normalize path to always end with a slash for comparison
        normalized_path = path if path.endswith('/') else path + '/'

        # Check if the normalized path is in excluded_paths
        return normalized_path not in excluded_paths

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
