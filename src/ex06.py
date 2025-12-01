# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex06.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/01 12:07:26 by alaparic          #+#    #+#              #
#    Updated: 2025/12/01 12:12:53 by alaparic         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Vector import Vector

def cross_product(u: Vector[float], v: Vector[float]) -> Vector[float]:
    if u.size() != 3 or v.size() != 3:
        raise ValueError("Both vectors must be 3-dimensional for cross product.")

    cross_data = [
        u.data[1] * v.data[2] - u.data[2] * v.data[1],
        u.data[2] * v.data[0] - u.data[0] * v.data[2],
        u.data[0] * v.data[1] - u.data[1] * v.data[0]
    ]
    return Vector(cross_data)

def main():
    u = Vector([0.0, 0.0, 1.0])
    v = Vector([1.0, 0.0, 0.0])
    result = cross_product(u, v)
    print(f"u = {u}, v = {v}")
    print(f"u × v = {result}")
    print()

    u = Vector([2.0, 1.0, 3.0])
    v = Vector([4.0, -2.0, 1.0])
    w = cross_product(u, v)
    dot_uw = u.dot(w)
    dot_vw = v.dot(w)
    print(f"u = {u}, v = {v}, w = u × v = {w}")
    print(f"u · w = {dot_uw}")
    print(f"v · w = {dot_vw}")


if __name__ == "__main__":
    main()