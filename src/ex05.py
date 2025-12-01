# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex05.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/01 11:01:35 by alaparic          #+#    #+#              #
#    Updated: 2025/12/01 12:57:13 by alaparic         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Vector import Vector


def angle_cos(u: Vector[float], v: Vector[float]) -> float:
    if u.norm() == 0 or v.norm() == 0:
        raise ValueError("Cannot compute angle with zero-length vector.")

    if len(u) != len(v):
        raise ValueError(
            "Vectors must be of the same length to compute angle.")

    dot_product = u.dot(v)
    norm_product = u.norm() * v.norm()

    return dot_product / norm_product


def main():
    u = Vector([1.0, 0.0])
    v = Vector([1.0, 0.0])
    print(f"1. Parallel vectors")
    print(f"u = {u}, v = {v}")
    print(f"cos(u, v) = {angle_cos(u, v)}")
    print()

    u = Vector([1.0, 0.0])
    v = Vector([0.0, 1.0])
    print(f"2. Perpendicular vectors")
    print(f"u = {u}, v = {v}")
    print(f"cos(u, v) = {angle_cos(u, v)}")
    print()

    u = Vector([-1.0, 1.0])
    v = Vector([1.0, -1.0])
    print(f"3. Opposite direction vectors")
    print(f"u = {u}, v = {v}")
    print(f"cos(u, v) = {angle_cos(u, v)}")
    print()

    u = Vector([2.0, 1.0])
    v = Vector([4.0, 2.0])
    print(f"4. Parallel vectors with different magnitudes")
    print(f"u = {u}, v = {v}")
    print(f"cos(u, v) = {angle_cos(u, v)}")
    print()

    u = Vector([1.0, 2.0, 3.0])
    v = Vector([4.0, 5.0, 6.0])
    print(f"5. Vectors with an acute angle")
    print(f"u = {u}, v = {v}")
    print(f"cos(u, v) = {angle_cos(u, v)}")
    print()

    u = Vector([3.0, 1.0, 2.0])
    v = Vector([2.0, 4.0, -1.0])
    print(f"6. Vectors in 3D")
    print(f"u = {u}, v = {v}")
    print(f"cos(u, v) = {angle_cos(u, v)}")


if __name__ == "__main__":
    main()
