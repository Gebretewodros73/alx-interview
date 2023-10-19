#!/usr/bin/python3
"""
Log Parsing Script
"""
import sys


def print_stats(total_size, status_codes):
    """
    Print statistics

    Args:
        total_size (int): Total file size
        status_codes (dict): Dictionary containing status code counts
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line):
    """
    Parse a log line

    Args:
        line (str): Log line to parse

    Returns:
        tuple: Tuple containing IP, status code, and file size
    """
    try:
        parts = line.split()
        ip = parts[0]
        status = int(parts[-2])
        size = int(parts[-1])
        return (ip, status, size)
    except Exception as e:
        return None


def main():
    total_size = 0
    status_codes = {
            200: 0,
            301: 0,
            400: 0,
            401: 0,
            403: 0,
            404: 0,
            405: 0,
            500: 0
            }
    lines_read = 0

    try:
        for line in sys.stdin:
            lines_read += 1
            log_data = parse_line(line)
            if log_data:
                total_size += log_data[2]
                status_codes[log_data[1]] += 1
            if lines_read % 10 == 0:
                print_stats(total_size, status_codes)
    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        sys.exit(0)


if __name__ == "__main__":
    main()
