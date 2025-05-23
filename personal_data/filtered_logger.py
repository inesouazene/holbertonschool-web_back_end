#!/usr/bin/env python3
"""
Module for filtering and obfuscating log messages containing PII data.
This module provides functionality to replace sensitive field values
in log messages with redacted placeholders for privacy protection.
"""

import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str, message: str, separator: str) -> str:
    """
    Returns the log message obfuscated by replacing specified field values.

    This function uses regex to find and replace values of specified fields
    in a log message with a redaction string to protect sensitive information.

    Args:
        fields: A list of strings representing all fields to obfuscate
        redaction: A string representing what the field will be replaced with
        message: A string representing the log line to process
        separator: A string representing the character separating fields

    Returns:
        str: The log message with specified fields obfuscated
    """

    pattern = f"({'|'.join(fields)})=([^{re.escape(separator)}]*)"
    return re.sub(pattern, fr'\1={redaction}', message)


# Test function (pour vérifier le fonctionnement)
if __name__ == "__main__":
    # Test avec l'exemple donné
    fields = ["password", "date_of_birth"]
    messages = [
        "name=egg;"
        "email=eggmin@eggsample.com;"
        "password=eggcellent;"
        "date_of_birth=12/12/1986;",
        "name=bob;"
        "email=bob@dylan.com;"
        "password=bobbycool;"
        "date_of_birth=03/04/1993;"
    ]

    for message in messages:
        result = filter_datum(fields, 'xxx', message, ';')
        print(result)
