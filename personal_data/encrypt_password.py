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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validate that a provided password matches the hashed password.

    This function uses bcrypt to verify if a plain text password
    corresponds to a given hashed password. It safely compares
    the password against the hash without revealing timing information.

    Args:
        hashed_password: A bytes object representing the stored hash
        password: A string representing the plain text password to verify

    Returns:
        bool: True if the password matches the hash, False otherwise

    Example:
        >>> hashed = hash_password("MyPassword123")
        >>> is_valid(hashed, "MyPassword123")
        True
        >>> is_valid(hashed, "WrongPassword")
        False
    """
    # Convert string password to bytes
    password_bytes = password.encode('utf-8')

    # Use bcrypt to check if password matches the hash
    return bcrypt.checkpw(password_bytes, hashed_password)


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

    # Test the is_valid function
    print("\n=== Test is_valid ===")

    # Test with correct password
    is_valid_correct = is_valid(hash1, test_password)
    print(f"Correct password validation: {is_valid_correct}")

    # Test with incorrect password
    wrong_password = "WrongPassword123"
    is_valid_wrong = is_valid(hash1, wrong_password)
    print(f"Wrong password validation: {is_valid_wrong}")

    # Test that both hashes validate the same password
    is_valid1 = is_valid(hash1, test_password)
    is_valid2 = is_valid(hash2, test_password)

    print(f"Hash 1 validates original password: {is_valid1}")
    print(f"Hash 2 validates original password: {is_valid2}")

    # Test case sensitivity
    case_sensitive_test = is_valid(hash1, test_password.upper())
    print(f"Case sensitive test (should be False): {case_sensitive_test}")
