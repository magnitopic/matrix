# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex11.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/03 12:34:49 by alaparic          #+#    #+#              #
#    Updated: 2025/12/04 20:29:20 by alaparic         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import List
from Matrix import Matrix


def determinant(matrix: Matrix[float]) -> float:
    n = len(matrix)
    if n == 1:
        return matrix[0][0]

    total = 0
    for j in range(n):
        sign = (-1) ** j  # Alternating sign
        submatrix = []
        for i in range(1, n):
            fila = matrix[i][:j] + matrix[i][j+1:]
            submatrix.append(fila)
        total += matrix[0][j] * sign * determinant(submatrix)

    return total


def main():
    mat = Matrix([
        [2, -3, 0],
        [1, -1, 0],
        [-2, 5, 1]
    ])
    print("Matrix:")
    print(mat)
    det = determinant(mat.data)
    print(f"\nDeterminant: {det}\n")

    mat = Matrix([
        [1, 2],
        [3, 4]
    ])
    print("Matrix:")
    print(mat)
    det = determinant(mat.data)
    print(f"\nDeterminant: {det}\n")
    print()
    m = Matrix([
        [0.0, 1.0, 2.0],
        [3.0, 0.0, 4.0],
        [5.0, 6.0, 0.0]
    ])
    print("Matrix:")
    print(m)
    det = determinant(m.data)
    print(f"\nDeterminant: {det}\n")


if __name__ == "__main__":
    main()
