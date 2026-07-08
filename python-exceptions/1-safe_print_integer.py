#!/usr/bin/python3
def safe_print_integer(value):
    """Prints an integer safely.

    Args:
        value: The value to print.

    Returns:
        True if value is an integer and was printed successfully,
        otherwise False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
