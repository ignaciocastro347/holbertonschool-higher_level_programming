#!/usr/bin/python3
""" pascal_triangle module """


def pascal_triangle(n):
    """ pascal_triangle function"""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        triangle.append([])
        for j in range(i + 1):
            if j == 0:
                val = 1
            else:
                try:
                    val = triangle[i - 1][j - 1] + triangle[i - 1][j]
                except IndexError:
                    val = triangle[i - 1][j - 1]
            triangle[i].append(val)
    return triangle
