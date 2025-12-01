# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex09.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/01 18:22:50 by alaparic          #+#    #+#              #
#    Updated: 2025/12/01 20:03:18 by alaparic         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Matrix import Matrix


def main():
    mat = Matrix([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
    print("Original Matrix:")
    for row in mat.data:
        print(row)
    transposed = mat.transpose()
    print("\nTransposed Matrix:")
    for row in transposed.data:
        print(row)
    print()

    mat = Matrix([[7, 8], [9, 10], [11, 12]])
    print("Original Matrix:")
    for row in mat.data:
        print(row)
    transposed = mat.transpose()
    print("\nTransposed Matrix:")
    for row in transposed.data:
        print(row)
    print()

    mat = Matrix([[1, 2]])
    print("Original Matrix:")
    for row in mat.data:
        print(row)
    transposed = mat.transpose()
    print("\nTransposed Matrix:")
    for row in transposed.data:
        print(row)
    print()


if __name__ == "__main__":
    main()
