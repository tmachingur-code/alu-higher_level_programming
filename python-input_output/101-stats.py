#!/usr/bin/python3
"""Script that reads stdin and computes log metrics."""

import sys


total_file_size = 0
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

count = 0


def print_statistics():
    """Print statistics."""
    print("File size: {}".format(total_file_size))

    for key in sorted(status_codes):
        if status_codes[key] != 0:
            print("{}: {}".format(key, status_codes[key]))


try:
    for line in sys.stdin:
        count += 1

        try:
            data = line.split()

            if len(data) < 2:
                continue

            status = data[-2]
            size = data[-1]

            total_file_size += int(size)

            if int(status) in status_codes:
                status_codes[int(status)] += 1

        except (ValueError, IndexError):
            continue

        if count == 10:
            print_statistics()
            count = 0

    if count != 0 or total_file_size == 0:
        print_statistics()

except KeyboardInterrupt:
    print_statistics()
