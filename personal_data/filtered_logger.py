#!/usr/bin/env python3
"""
Module for filtering and obfuscating log messages containing PII data.
This module provides functionality to replace sensitive field values
in log messages with redacted placeholders for privacy protection.
"""

import re
import logging
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

    Example:
        >>> filter_datum(['password'], 'xxx', 'name=bob;password=secret;', ';')
        'name=bob;password=xxx;'
    """
    pattern = f"({'|'.join(fields)})=([^{re.escape(separator)}]*)"
    return re.sub(pattern, fr'\1={redaction}', message)


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class that filters sensitive
    information from log records.

    This formatter automatically obfuscates specified fields in log messages
    to protect personally identifiable information (PII) while maintaining
    log structure and readability.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str] = None):
        """
        Initialize the RedactingFormatter with fields to redact.

        Args:
            fields: List of field names to obfuscate in log messages.
                   If None, no fields will be redacted.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields or []

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the log record and filter sensitive field values.

        This method formats the log record using the parent formatter,
        then applies field filtering to obfuscate sensitive information.

        Args:
            record: The LogRecord instance to format

        Returns:
            str: The formatted log message with sensitive fields redacted
        """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


# Test function (pour vérifier le fonctionnement)
if __name__ == "__main__":
    # Test de filter_datum
    print("=== Test filter_datum ===")
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

    # Test de RedactingFormatter
    print("\n=== Test RedactingFormatter ===")
    message = ("name=Bob;email=bob@dylan.com;"
               "ssn=000-123-0000;password=bobby2019;")
    log_record = logging.LogRecord("my_logger", logging.INFO, None, None,
                                   message, None, None)
    formatter = RedactingFormatter(fields=["email", "ssn", "password"])
    print(formatter.format(log_record))
