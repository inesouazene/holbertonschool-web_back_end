#!/usr/bin/env python3
"""
Module for secure password encryption and validation.
This module provides functionality to hash passwords using bcrypt
for secure storage and authentication in applications.
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password with a random salt using bcrypt.

    This function takes a plain text password and returns a salted,
    hashed password using the bcrypt algorithm. Each call generates
    a unique salt, ensuring that identical passwords produce different
    hashes for enhanced security.

    Args:
        password: A string representing the plain text password to hash

    Returns:
        bytes: A salted, hashed password as a byte string

    Example:
        >>> hashed = hash_password("MyPassword123")
        >>> len(hashed)
        60
        >>> hashed.startswith(b'$2b$')
        True
    """
    # Convert string to bytes
    password_bytes = password.encode('utf-8')

    # Generate salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)

    return hashed_password


# Test function for development and validation
if __name__ == "__main__":
    # Test the hash_password function
    print("=== Test hash_password ===")

    test_password = "MyAmazingPassw0rd"

    # Generate two hashes of the same password
    hash1 = hash_password(test_password)
    hash2 = hash_password(test_password)

    print(f"Password: {test_password}")
    print(f"Hash 1: {hash1}")
    print(f"Hash 2: {hash2}")
    print(f"Hashes are different: {hash1 != hash2}")
    print(f"Hash length: {len(hash1)} bytes")

    # Verify that both hashes are valid for the same password
    is_valid1 = bcrypt.checkpw(test_password.encode('utf-8'), hash1)
    is_valid2 = bcrypt.checkpw(test_password.encode('utf-8'), hash2)

    print(f"Hash 1 validates: {is_valid1}")
    print(f"Hash 2 validates: {is_valid2}")
