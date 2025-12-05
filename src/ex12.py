# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex12.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/04 20:23:18 by alaparic          #+#    #+#              #
#    Updated: 2025/12/05 14:20:10 by alaparic         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Matrix import Matrix


def inverse(matrix: Matrix[float]) -> Matrix[float]:
    """Calculate the inverse of the matrix using Gauss-Jordan elimination."""
    rows, cols = matrix.shape()

    if rows != cols:
        raise ValueError(
            "\033[0;31mOnly square matrices can be inverted.\033[0m")

    n = rows

    # Create augmented matrix [A | I]
    augmented = []
    for i in range(n):
        row = matrix.data[i][:] + [0] * n
        row[n + i] = 1  # Identity matrix on the right
        augmented.append(row)

    # Forward elimination (to row echelon form)
    for col in range(n):
        # Find pivot
        pivot_row = None
        for row in range(col, n):
            if augmented[row][col] != 0:
                pivot_row = row
                break

        # If no pivot found, matrix is singular (not invertible)
        if pivot_row is None:
            raise ValueError(
                "\033[0;31mMatrix is singular and cannot be inverted.\033[0m")

        # Swap rows if needed
        if pivot_row != col:
            augmented[col], augmented[pivot_row] = augmented[pivot_row], augmented[col]

        # Scale pivot row to make pivot = 1
        pivot_value = augmented[col][col]
        for j in range(2 * n):
            augmented[col][j] /= pivot_value

        # Eliminate column entries below pivot
        for row in range(col + 1, n):
            factor = augmented[row][col]
            for j in range(2 * n):
                augmented[row][j] -= factor * augmented[col][j]

    # Back substitution (to reduced row echelon form)
    for col in range(n - 1, -1, -1):
        for row in range(col):
            factor = augmented[row][col]
            for j in range(2 * n):
                augmented[row][j] -= factor * augmented[col][j]

    # Extract the right half (the inverse matrix)
    inverse_data = []
    for i in range(n):
        inverse_data.append(augmented[i][n:])

    return Matrix(inverse_data)


def main():
    m = Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    inv = inverse(m)
    print("Original Matrix:")
    print(m)
    print("Inverse Matrix:")
    print(inv)
    print("Checking multiplication (should be identity):")
    print(m @ inv)
    print("-"*20)
    print()

    m = Matrix([
        [8.0, 5.0, -2.0],
        [4.0, 7.0, 20.0],
        [7.0, 6.0, 1.0]
    ])
    inv = inverse(m)
    print("Original Matrix:")
    print(m)
    print("Inverse Matrix:")
    print(inv)
    print("Checking multiplication (should be identity):")
    print(m @ inv)
    print("-"*20)
    print()

    m = Matrix([
        [2.0, 0.0, 0.0],
        [3.0, 5.0, 0.0],
        [4.0, 6.0, 7.0]
    ])
    inv = inverse(m)
    print("Original Matrix:")
    print(m)
    print("Inverse Matrix:")
    print(inv)
    print("Checking multiplication (should be identity):")
    print(m @ inv)
    print("-"*20)
    print()

    m = Matrix([
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0],
        [7.0, 8.0, 9.0]     # This matrix is singular
    ])
    try:
        print("Original Matrix:")
        print(m)
        inv = inverse(m)
        print("Inverse Matrix:")
        print(inv)
        print("Checking multiplication (should be identity):")
        print(m @ inv)
        print("-"*20)
        print()
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
