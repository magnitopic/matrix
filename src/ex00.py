# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex00.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/30 20:56:06 by alaparic          #+#    #+#              #
#    Updated: 2025/12/01 17:19:15 by alaparic         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Vector import Vector
from Matrix import Matrix


def main():

    print("=== Vectors ===")
    v1 = Vector([5, 2, 3])
    v2 = Vector([-1, 7, 6])

    print(f"{v1} + {v2} = {v1 + v2}")
    print(f"{v1} - {v2} = {v1 - v2}")
    print(f"{v1} * 3 = {v1 * 3}")
    print(f"3 * {v1} = {3 * v1}")

    print("\n", "-" * 40, "\n")

    print("=== Matrices ===")
    m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    print(f"{m1}+\n{m2}=\n{m1 + m2}")

    print("-"*10, "\n")

    print(f"{m1}-\n{m2}=\n{m1 - m2}")

    print("-"*10, "\n")

    print(f"{m1}* 2\n=\n{m1 * 2}")

    print("-"*10, "\n")

    print(f"2 *\n{m1}=\n{2 * m1}")


if __name__ == "__main__":
    main()
