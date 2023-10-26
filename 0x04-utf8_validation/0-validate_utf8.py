#!/usr/bin/python3
"""
Moduel to validate UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines if a given data set
    represents a valid UTF-8 encoding.

    Args:
        data (list of int): List of
        integers representing the data.

    Returns:
        bool: True if data is a valid
        UTF-8 encoding, else return False.
    """
    num_bytes = 0

    for byte in data:
        byte = byte & 255  # Ensure only 8 least signi

        if num_bytes == 0:
            if (byte >> 3) == 30:  # 4-byte character
                num_bytes = 3
            elif (byte >> 4) == 14:  # 3-byte character
                num_bytes = 2
            elif (byte >> 5) == 6:  # 2-byte character
                num_bytes = 1
            elif (byte >> 7) == 0:  # 1-byte character
                num_bytes = 0
            else:
                return False
        else:
            if (byte >> 6) == 2:  # Additional bytes should start with '10'
                num_bytes -= 1
            else:
                return False

    return num_bytes == 0
