#!/usr/bin/python3
"""This module contains a function that multiplies two matrices."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a: First matrix (list of lists of integers/floats).
        m_b: Second matrix (list of lists of integers/floats).

    Returns:
        A new matrix representing the product of m_a and m_b.

    Raises:
        TypeError: If the matrices are not valid.
        ValueError: If the matrices are empty or cannot be multiplied.
    """

    # Validate m_a
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")

    for row in m_a:
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError(
                    "m_a should contain only integers or floats"
                )

    row_size = len(m_a[0])
    for row in m_a:
        if len(row) != row_size:
            raise TypeError(
                "each row of m_a must be of the same size"
            )

    # Validate m_b
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_b:
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError(
                    "m_b should contain only integers or floats"
                )

    row_size = len(m_b[0])
    for row in m_b:
        if len(row) != row_size:
            raise TypeError(
                "each row of m_b must be of the same size"
            )

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = []

    for i in range(len(m_a)):
        new_row = []

        for j in range(len(m_b[0])):
            total = 0

            for k in range(len(m_b)):
                total += m_a[i][k] * m_b[k][j]

            new_row.append(total)

        result.append(new_row)

    return result
