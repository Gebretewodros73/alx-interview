#!/usr/bin/python3
"""
Module definition : pascals triangle
"""


def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to level n.

    Args:
        n (int): The level up to which to generate Pascal's Triangle.

    Returns:
        list of lists: A list of lists representing Pascal's Triangle.
        []: If n is not a non-negative integer.
    """
    try:
        if not isinstance(n, int) or n < 0:
            return []

        triangle = [[1]]

        for i in range(1, n):
            prev_row = triangle[-1]
            new_row = [1]

            for j in range(1, len(prev_row)):
                new_row.append(prev_row[j-1] + prev_row[j])

            new_row.append(1)
            triangle.append(new_row)

        return triangle

    except ValueError as e:
        print(e)
        return []
