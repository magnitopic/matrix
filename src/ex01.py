# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex01.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/30 20:55:54 by alaparic          #+#    #+#              #
#    Updated: 2025/12/01 13:14:46 by alaparic         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Vector import Vector
from Matrix import Matrix


def linear_combination_vector(vectors: list[Vector], coefficients: list[float | complex]) -> Vector:
    if len(vectors) != len(coefficients):
        raise ValueError(
            "The number of vectors must match the number of coefficients.")

    result = Vector([0] * len(vectors[0].data))

    for vec, coeff in zip(vectors, coefficients):
        result += vec * coeff

    return result


def linear_combination_matrix(matrices: list['Matrix'], coefficients: list[float | complex]) -> 'Matrix':
    if len(matrices) != len(coefficients):
        raise ValueError(
            "The number of matrices must match the number of coefficients.")

    result = Matrix([[0] * matrices[0].shape()[1]
                     for _ in range(matrices[0].shape()[0])])

    for mat, coeff in zip(matrices, coefficients):
        result += mat * coeff

    return result


def main():
    print("Linear Combination of Vectors")
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    v3 = Vector([7, 8, 9])

    k = [0.2, 0.3, 0.5]
    result = linear_combination_vector([v1, v2, v3], k)

    print(
        f"Linear combination of {v1}, {v2}, and {v3} with coefficients {k} is: {result}\n")

    print(
        f"{v1} * {k[0]} + {v2} * {k[1]} + {v3} * {k[2]} = {v1 * k[0] + v2 * k[1] + v3 * k[2]}")

    print("\n", "-" * 40, "\n")

    print("Linear Combination of Matrices\n")
    m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    k = [0.4, 0.6]
    result_matrix = linear_combination_matrix([m1, m2], k)

    print(
        f"Linear combination of\n{m1}and\n{m2}with coefficients {k} is:\n{result_matrix}\n")

    print(f"{m1} * {k[0]} +\n{m2} * {k[1]} =\n{m1 * k[0] + m2 * k[1]}")


if __name__ == "__main__":
    main()
