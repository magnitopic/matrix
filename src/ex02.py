# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex02.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/30 20:56:08 by alaparic          #+#    #+#              #
#    Updated: 2025/12/01 13:19:50 by alaparic         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import TypeVar
from Vector import Vector
from Matrix import Matrix

T = TypeVar('T', Vector, Matrix, complex)


def linear_interpolation(u: T, v: T, t: int | float) -> T:
    if not isinstance(t, (int, float)):
        raise TypeError("t must be a number")
    if not 0 <= t <= 1:
        raise ValueError("t must be in the range [0, 1]")

    return (1 - t) * u + t * v


def main():
    print("Linear Interpolation of Vectors")
    v1 = Vector([2.0, 1.0])
    v2 = Vector([4.0, 2.0])

    print(f"lerp({v1}, {v2}, 0.0) = {linear_interpolation(v1, v2, 0.0)}")
    print(f"lerp({v1}, {v2}, 0.5) = {linear_interpolation(v1, v2, 0.5)}")
    print(f"lerp({v1}, {v2}, 1.0) = {linear_interpolation(v1, v2, 1.0)}")

    print("\n", "-" * 40, "\n")

    print("Linear Interpolation of Matrices")
    m1 = Matrix([[1.0, 2.0], [3.0, 4.0]])
    m2 = Matrix([[5.0, 6.0], [7.0, 8.0]])
    print(f"lerp(\n{m1},\n{m2}, 0.0) \n=\n{linear_interpolation(m1, m2, 0.0)}")
    print("-" * 10)
    print(f"lerp(\n{m1},\n{m2}, 0.5) \n=\n{linear_interpolation(m1, m2, 0.5)}")
    print("-" * 10)
    print(f"lerp(\n{m1},\n{m2}, 1.0) \n=\n{linear_interpolation(m1, m2, 1.0)}")


if __name__ == "__main__":
    main()
