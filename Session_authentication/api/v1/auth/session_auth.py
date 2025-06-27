#!/usr/bin/env python3
"""
SessionAuth module for the API
"""
from api.v1.auth.auth import Auth
from models.user import User
import uuid


class SessionAuth(Auth):
    """
    Session Authentication class that inherits from Auth
    """
    user_id_by_session_id = dict()

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a User ID
        """
        if user_id is None or type(user_id) is not str:
            return None
        self.session_id = str(uuid.uuid4())
        self.user_id_by_session_id[self.session_id] = user_id
        return self.session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a User ID based on a Session ID
        """
        if session_id is None or type(session_id) is not str:
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Returns a User instance based on a cookie value

        Args:
            request: Flask request object

        Returns:
            User instance if found, None otherwise
        """
        if request is None:
            return None

        # Get the session cookie value from the request
        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        # Get the user ID associated with this session ID
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        from models.user import User

        # Retrieve and return the User instance from the database
        return User.get(user_id)

    def destroy_session(self, request=None):
        """
        Deletes the user session / logout

        Args:
            request: Flask request object

        Returns:
            True if session was successfully destroyed, False otherwise
        """
        # Check if request is None
        if request is None:
            return False

        # Get the session ID from the cookie
        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        # Check if the session ID is linked to any User ID
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return False

        # Delete the session ID from the dictionary
        if session_id in self.user_id_by_session_id:
            del self.user_id_by_session_id[session_id]
            return True

        return False
