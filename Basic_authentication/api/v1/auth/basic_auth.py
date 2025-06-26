#!/usr/bin/env python3
"""
BasicAuth module for the API
"""
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    BasicAuth class that inherits from Auth
    Implements Basic Authentication for the API
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header for Basic Auth

        Args:
            authorization_header: The Authorization header string
        Returns:
            The Base64 part of the Authorization header, or None if not valid
        """
        if authorization_header is None:
            return None

        # Check if the header isn't a string
        if not isinstance(authorization_header, str):
            return None

        # Check if the header starts with 'Basic '
        if not authorization_header.startswith('Basic '):
            return None

        # Return the value after 'Basic '
        return authorization_header[6:]
