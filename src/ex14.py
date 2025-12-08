# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex14.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/07 12:40:24 by alaparic          #+#    #+#              #
#    Updated: 2025/12/08 12:08:25 by alaparic         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from Matrix import Matrix
from math import tan, pi


def projection_matrix(fov: float, aspect_ratio: float, near: float, far: float) -> Matrix:
    """
    Calculates the perspective projection matrix for 3D rendering.

    The projection matrix transforms camera space coordinates to normalized
    device coordinates (NDC) in range [-1,1] for X and Y, and [0,1] for Z.

    Parameters:
    fov (float): Vertical field of view in radians
    aspect_ratio (float): Aspect ratio (width / height) of the viewport
    near (float): Distance to the near clipping plane
    far (float): Distance to the far clipping plane

    Returns:
    Matrix: 4x4 perspective projection matrix
    """
    # Convert FOV from degrees to radians if necessary
    if fov > pi:  # Probably in degrees
        fov = fov * pi / 180  # Convert degrees to radians

    # Calculate basic parameters
    f = 1.0 / tan(fov / 2.0)

    # Build projection matrix (column-major order for OpenGL compatibility)
    # This format means we specify columns first
    return Matrix([
        [f/aspect_ratio, 0,       0,                   0],
        [0,              f,       0,                   0],
        [0,              0,       (far+near)/(near-far),
         (2*far*near)/(near-far)],
        [0,              0,       -1,                  0]
    ])


def main():
    fov_deg = 60.0
    aspect_ratio = 16.0 / 9.0  # Common widescreen aspect ratio
    near = 0.1
    far = 100.0

    proj_matrix = projection_matrix(fov_deg, aspect_ratio, near, far)

    print("Projection matrix with FOV=60°, aspect=16/9, near=0.1, far=100:")
    for j in range(4):
        for i in range(4):
            print(f"{proj_matrix.data[i][j]}", end="")
            if i < 3 or j < 3:
                print(",", end=" ")
        print()
    print()

    fov_deg = 90.0
    aspect_ratio = 4.0 / 3.0  # More square aspect ratio
    near = 0.1
    far = 100.0

    proj_matrix = projection_matrix(fov_deg, aspect_ratio, near, far)

    print("Projection matrix with FOV=90°, aspect=4/3, near=0.1, far=100:")
    for j in range(4):
        for i in range(4):
            print(f"{proj_matrix.data[i][j]}", end="")
            if i < 3 or j < 3:
                print(",", end=" ")
        print()
    print()

    # Example 3: Projection with closer near/far planes
    fov_deg = 60.0
    aspect_ratio = 16.0 / 9.0
    near = 1.0
    far = 10.0

    proj_matrix = projection_matrix(fov_deg, aspect_ratio, near, far)

    print("Projection matrix with FOV=60°, aspect=16/9, near=1.0, far=10.0:")
    for j in range(4):
        for i in range(4):
            print(f"{proj_matrix.data[i][j]}", end="")
            if i < 3 or j < 3:
                print(",", end=" ")
        print()
    print()


if __name__ == "__main__":
    main()
