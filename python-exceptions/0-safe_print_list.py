#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list safely.

    Args:
        my_list: The list to print from.
        x: Number of elements to print.

    Returns:
        The actual number of elements printed.
    """
    count = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count += 1
        except IndexError:
            break

    print()
    return count
