# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex03.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/30 20:56:11 by alaparic          #+#    #+#              #
#    Updated: 2025/11/30 21:05:59 by alaparic         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Vector import Vector


def main():
    u = Vector([0.0, 0.0])
    v = Vector([1.0, 1.0])
    print(f"{u} · {v} = {u.dot(v)}")

    u = Vector([1.0, 1.0])
    v = Vector([1.0, 1.0])
    print(f"{u} · {v} = {u.dot(v)}")

    u = Vector([-1.0, 6.0])
    v = Vector([3.0, 2.0])
    print(f"{u} · {v} = {u.dot(v)}")

    u = Vector([1.0, 0.0, 0.0])
    v = Vector([0.0, 1.0, 0.0])
    print(f"{u} · {v} = {u.dot(v)}")

    u = Vector([1.5, 2.5, 3.5])
    v = Vector([0.5, 1.0, 1.5])
    print(f"{u} · {v} = {u.dot(v)}")

    u = Vector([1.0, 2.0, 3.0, 4.0, 5.0])
    v = Vector([5.0, 4.0, 3.0, 2.0, 1.0])
    print(f"{u} · {v} = {u.dot(v)}")


if __name__ == "__main__":
    main()
