#!/usr/bin/python3
def safe_print_integer_err(value):
    """Prints an integer with an error message in stderr if it fails.

    Args:
        value: The value to print.

    Returns:
        True if value is printed successfully, otherwise False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as err:
        sys = __import__('sys')
        print("Exception: {}".format(err), file=sys.stderr)
        return False
