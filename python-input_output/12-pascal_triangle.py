#!/usr/bin/python3
"""Module that provides a function to create Pascal's triangle."""


def pascal_triangle(n):
    """
    Return a list of lists of integers representing Pascal's triangle.

    Args:
        n: Number of rows of the triangle.

    Returns:
        A list containing Pascal's triangle rows.
    """
    if n <= 0:
        return []

    triangle = []

    for row_number in range(n):
        row = [1] * (row_number + 1)

        for index in range(1, row_number):
            row[index] = (
                triangle[row_number - 1][index - 1] +
                triangle[row_number - 1][index]
            )

        triangle.append(row)

    return triangle
