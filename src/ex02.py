# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex02.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/30 20:56:08 by alaparic          #+#    #+#              #
#    Updated: 2025/11/30 20:56:09 by alaparic         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import TypeVar
from Vector import Vector

T = TypeVar('T', Vector, complex)


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
    print(f"lerp({v1}, {v2}, 0.3) = {linear_interpolation(v1, v2, 0.3)}")
    print(f"lerp({v1}, {v2}, 0.5) = {linear_interpolation(v1, v2, 0.5)}")
    print(f"lerp({v1}, {v2}, 1.0) = {linear_interpolation(v1, v2, 1.0)}")

    print("\n", "-" * 40, "\n")

    print("Linear Interpolation of Matrices")


if __name__ == "__main__":
    main()
