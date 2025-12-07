# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex14.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/07 12:40:24 by alaparic          #+#    #+#              #
#    Updated: 2025/12/07 13:11:16 by alaparic         ###   ########.fr        #
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
    # Example 1: Standard projection with 60° FOV
    fov_deg = 60.0
    aspect_ratio = 16.0 / 9.0  # Common widescreen aspect ratio
    near = 0.1
    far = 100.0

    proj_matrix = projection_matrix(fov_deg, aspect_ratio, near, far)

    print("Projection matrix with FOV=60°, aspect=16/9, near=0.1, far=100:")
    print(proj_matrix)
    print("\nColumn-major format (for use with visualizer):")
    for j in range(4):
        for i in range(4):
            print(f"{proj_matrix.data[i][j]}", end="")
            if i < 3 or j < 3:
                print(",", end=" ")
        print()
    print()

    # Example 2: Wider projection (90° FOV)
    fov_deg = 90.0
    aspect_ratio = 4.0 / 3.0  # More square aspect ratio
    near = 0.1
    far = 100.0

    proj_matrix = projection_matrix(fov_deg, aspect_ratio, near, far)

    print("Projection matrix with FOV=90°, aspect=4/3, near=0.1, far=100:")
    print(proj_matrix)
    print()

    # Example 3: Projection with closer near/far planes
    fov_deg = 60.0
    aspect_ratio = 16.0 / 9.0
    near = 1.0
    far = 10.0

    proj_matrix = projection_matrix(fov_deg, aspect_ratio, near, far)

    print("Projection matrix with FOV=60°, aspect=16/9, near=1.0, far=10.0:")
    print(proj_matrix)
    print()

    # Projection matrix parameters explanation
    print("Projection matrix parameters explanation:")
    print("1. Field of view (FOV) controls how much of the world is visible.")
    print("   - Smaller FOV produces 'telephoto' (zoom) effect.")
    print("   - Larger FOV produces 'wide angle' effect.")
    print()
    print("2. Aspect ratio adjusts matrix for non-square viewports.")
    print("   - Prevents objects from appearing stretched when width ≠ height.")
    print()
    print("3. Near and far planes define the view frustum:")
    print("   - Objects closer than 'near' or farther than 'far' are clipped.")
    print("   - Narrower near-far range improves z-buffer precision.")
    print("   - Very small 'near' can cause numerical precision issues.")
    print()
    print("4. The matrix performs several transformations:")
    print("   - Projects 3D points to 2D with depth information.")
    print("   - Converts coordinates to [-1,1] range for X/Y, [0,1] for Z.")
    print("   - Inverts Z-axis for OpenGL coordinate system compatibility.")
    print()
    print("5. For complete transformation pipeline:")
    print("   - Screen position = P × V × M × object_position")
    print("   - P = this projection matrix")
    print("   - V = view matrix (camera)")
    print("   - M = model matrix (object transform)")


if __name__ == "__main__":
    main()
