# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex08.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/01 17:59:14 by alaparic          #+#    #+#              #
#    Updated: 2025/12/03 12:52:41 by alaparic         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Matrix import Matrix


def trace(matrix: Matrix) -> float:
    if matrix.shape()[0] != matrix.shape()[1]:
        raise ValueError("Trace is only defined for square matrices.")

    return sum(matrix.data[i][i] for i in range(matrix.shape()[0]))


def main():
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix = Matrix(mat)
    print("Matrix:")
    print(matrix)
    print("Trace of the matrix:", trace(matrix))

    mat = [
        [3, 4, 1],
        [5, 2, 8],
        [6, 9, 7]
    ]
    matrix = Matrix(mat)
    print("\nMatrix:")
    print(matrix)
    print("Trace of the matrix:", trace(matrix))

    mat = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    matrix = Matrix(mat)
    print("\nMatrix:")
    print(matrix)
    try:
        print("Trace of the matrix:", trace(matrix))
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
