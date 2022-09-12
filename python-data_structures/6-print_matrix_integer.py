#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j, num in enumerate(i):
            print("{:d}{}".format(
                num,
                " " if j < (len(i) - 1) else "\n"
                ),
                end="")