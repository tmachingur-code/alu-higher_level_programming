#!/usr/bin/python3
def safe_function(fct, *args):
    """Executes a function safely.

    Args:
        fct: Function to execute.
        *args: Arguments passed to the function.

    Returns:
        The result of the function, or None if an exception occurs.
    """
    try:
        return fct(*args)
    except Exception as err:
        sys = __import__('sys')
        print("Exception: {}".format(err), file=sys.stderr)
        return None
