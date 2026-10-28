#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # Print each integer in the row separated by a space
        # We loop with an index or print dynamically
        for i in range(len(row)):
            if i == len(row) - 1:
                print("{:d}".format(row[i]), end="")
            else:
                print("{:d}".format(row[i]), end=" ")
        print()
