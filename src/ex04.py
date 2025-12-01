# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex04.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/01 10:52:19 by alaparic          #+#    #+#              #
#    Updated: 2025/12/01 10:58:25 by alaparic         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Vector import Vector


def main():
    u = Vector([0.0, 0.0, 0.0])
    print(f"Vector: {u}")
    print(f"Norma-1: {u.norm_1()}")
    print(f"Norma-2: {u.norm()}")
    print(f"Norma-∞: {u.norm_inf()}")
    print()

    u = Vector([1.0, 2.0, 3.0])
    print(f"Vector: {u}")
    print(f"Norma-1: {u.norm_1()}")
    print(f"Norma-2: {u.norm()}")
    print(f"Norma-∞: {u.norm_inf()}")
    print()

    u = Vector([-1.0, -2.0])
    print(f"Vector: {u}")
    print(f"Norma-1: {u.norm_1()}")
    print(f"Norma-2: {u.norm()}")
    print(f"Norma-∞: {u.norm_inf()}")
    print()


if __name__ == "__main__":
    main()
