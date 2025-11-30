# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex01.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/30 20:55:54 by alaparic          #+#    #+#              #
#    Updated: 2025/11/30 20:55:55 by alaparic         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Vector import Vector


def linear_combination_vector(vectors: list[Vector], coefficients: list[float]) -> Vector:
    if len(vectors) != len(coefficients):
        raise ValueError(
            "The number of vectors must match the number of coefficients.")

    result = Vector([0] * len(vectors[0].data))

    for vec, coeff in zip(vectors, coefficients):
        result += vec * coeff

    return result


def main():
    print("Linear Combination of Vectors")
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])
    v3 = Vector([7, 8, 9])

    coefficients = [0.2, 0.3, 0.5]
    result = linear_combination_vector([v1, v2, v3], coefficients)

    print(
        f"Linear combination of {v1}, {v2}, and {v3} with coefficients {coefficients} is: {result}\n")

    print(f"{v1} * 0.2 + {v2} * 0.3 + {v3} * 0.5 = {v1 * 0.2 + v2 * 0.3 + v3 * 0.5}")


if __name__ == "__main__":
    main()
