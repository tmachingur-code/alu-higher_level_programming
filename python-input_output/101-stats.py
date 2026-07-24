#!/usr/bin/python3
"""Script that reads log input and computes statistics."""

import sys


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

line_count = 0


def print_stats():
    """Print the accumulated log statistics."""
    print("File size: {}".format(total_size))

    for code in sorted(status_codes):
        if status_codes[code] != 0:
            print("{}: {}".format(code, status_codes[code]))


def process_line(line):
    """Process a single log line and update statistics."""
    global total_size

    try:
        parts = line.split()
        status = int(parts[-2])
        size = int(parts[-1])

        total_size += size

        if status in status_codes:
            status_codes[status] += 1

    except (ValueError, IndexError):
        pass


try:
    for line in sys.stdin:
        line_count += 1
        process_line(line)

        if line_count % 10 == 0:
            print_stats()

    if line_count % 10 != 0 or line_count == 0:
        print_stats()

except KeyboardInterrupt:
    print_stats()
