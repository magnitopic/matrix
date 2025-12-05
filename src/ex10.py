# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex10.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/03 12:59:05 by alaparic          #+#    #+#              #
#    Updated: 2025/12/05 14:12:39 by alaparic         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Matrix import Matrix


def main():
    m = Matrix([
        [0.0, 1.0, 2.0],
        [3.0, 0.0, 4.0],
        [5.0, 6.0, 0.0]
    ])
    rref = m.row_echelon()
    print("Original Matrix:")
    print(m)
    print("\nRow Echelon Form:")
    print(rref)
    print()
    m = Matrix([
        [8.0, 5.0, -2.0, 4.0, 28.0],
        [4.0, 2.5, 20.0, 4.0, -4.0],
        [8.0, 5.0, 1.0, 4.0, 17.0]
    ])
    try:
        print("Original Matrix:")
        print(m)
        print("\nRow Echelon Form:")
        rref = m.row_echelon()
    except Exception as e:
        print(e)
    print()
    m = Matrix([
        [1, 2],
        [3, 4]
    ])
    print("Original Matrix:")
    print(m)
    print("\nRow Echelon Form:")
    rref = m.row_echelon()
    print(rref)


if __name__ == "__main__":
    main()
