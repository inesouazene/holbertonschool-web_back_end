#!/usr/bin/env python3
"""
BasicAuth module for the API
"""
from api.v1.auth.auth import Auth
from typing import TypeVar

User = TypeVar('User')


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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
        Decodes value of Base 64 string

        Args:
            base64_authorization_header: The Base64 encoded string

        Returns:
            The decoded string, or None if not valid
        """
        if base64_authorization_header is None:
            return None

        # Check if the header isn't a string
        if not isinstance(base64_authorization_header, str):
            return None

        # Check if the header is not a valid Base64 string
        try:
            import base64
            decoded_bytes = base64.b64decode(base64_authorization_header)
        except Exception:
            return None

        # Return the decoded string
        return decoded_bytes.decode('utf-8')

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> tuple:
        """
        Returns the user email and password from the decoded Base64 value

        Args:
            decoded_base64_authorization_header: The decoded Base64 string
        Returns:
            A tuple containing the user email and password,
            or (None, None) if not valid
        """
        if decoded_base64_authorization_header is None:
            return None, None

        if not isinstance(decoded_base64_authorization_header, str):
            return None, None

        if ":" not in decoded_base64_authorization_header:
            return None, None

        return decoded_base64_authorization_header.split(":", 1)

    def user_object_from_credentials(self,
                                     user_email: str, user_pwd: str
                                     ) -> TypeVar('User'):
        """
        Returns the user instance based on the email and password

        Args:
            user_email: The user's email
            user_pwd: The user's password
        Returns:
            The user instance if found, None otherwise
        """
        if user_email is None or not isinstance(user_email, str):
            return None

        if user_pwd is None or not isinstance(user_pwd, str):
            return None

        # Import User model here to avoid circular import issues
        from models.user import User

        # Query the User model for a user with the given email and password
        users = User.search({'email': user_email})
        if not users:
            return None
        user = users[0]
        if user.is_valid_password(user_pwd):
            return user

        return None
