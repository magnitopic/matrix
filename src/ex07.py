# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex07.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/01 17:22:04 by alaparic          #+#    #+#              #
#    Updated: 2025/12/07 14:22:45 by alaparic         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Vector import Vector
from Matrix import Matrix


def main():
    print("=== Matrix-Vector Multiplication ===")
    m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    v = Vector([1, 0, -1])
    result = m.mul_vec(v)
    print(f"Result of multiplying matrix\n{m}by vector {v} is:\n{result}")

    result = m @ v
    print(f"Using @ operator, the result is:\n{result}")

    print("\n", "-" * 40, "\n")
    print("=== Matrix-Matrix Multiplication ===")
    m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
    result = m1.mul_mat(m2)
    print(f"Result of multiplying matrix\n{m1}by matrix\n{m2}is:\n{result}")

    result = m1 @ m2
    print(f"Using @ operator, the result is:\n{result}")

    m1 = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    m2 = Matrix([[7.0, 8.0], [9.0, 10.0], [11.0, 12.0]])
    result = m1 @ m2
    print(f"\nMultiplying non-square matrices:\n{m1}by\n{m2}gives:\n{result}")


if __name__ == "__main__":
    main()
