# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex13.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/05 14:20:37 by alaparic          #+#    #+#              #
#    Updated: 2025/12/05 18:07:41 by alaparic         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from Matrix import Matrix


def matrix_rank(matrix: 'Matrix[T]') -> int:
    # Get the row echelon form of the matrix
    echelon_form = matrix.row_echelon()

    # Count the number of non-zero rows
    rows, cols = echelon_form.shape()
    rank = 0

    # Tolerance for considering a value as zero
    epsilon = 1e-10

    for i in range(rows):
        # Check if the row contains any non-zero element
        is_zero_row = True
        for j in range(cols):
            if abs(echelon_form.data[i][j]) > epsilon:
                is_zero_row = False
                break

        if not is_zero_row:
            rank += 1

    return rank


def main():
    # Case 1: 3x3 identity matrix (full rank = 3)
    mat = Matrix([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    rank_value = matrix_rank(mat)
    print("Case 1: 3x3 Identity Matrix")
    print(f"Matrix:\n{mat}")
    print(f"Row echelon form:\n{mat.row_echelon()}")
    print(f"Rank: {rank_value}")  # Should be 3
    print()

    # Case 2: Matrix with dependent rows
    mat = Matrix([
        [1.0, 2.0, 0.0, 0.0],
        [2.0, 4.0, 0.0, 0.0],
        [-1.0, 2.0, 1.0, 1.0]
    ])
    rank_value = matrix_rank(mat)
    print("Case 2: Matrix with Dependent Rows")
    print(f"Matrix:\n{mat}")
    print(f"Row echelon form:\n{mat.row_echelon()}")
    print(f"Rank: {rank_value}")  # Should be 2
    print()

    # Case 3: 4x3 rectangular matrix with full rank by columns
    mat = Matrix([
        [8.0, 5.0, -2.0],
        [4.0, 7.0, 20.0],
        [7.0, 6.0, 1.0],
        [21.0, 18.0, 7.0]
    ])
    rank_value = matrix_rank(mat)
    print("Case 3: 4x3 Rectangular Matrix")
    print(f"Matrix:\n{mat}")
    print(f"Row echelon form:\n{mat.row_echelon()}")
    print(f"Rank: {rank_value}")  # Should be 3
    print()

    # Case 4: Null matrix (rank 0)
    mat = Matrix([[0.0, 0.0], [0.0, 0.0]])
    rank_value = matrix_rank(mat)
    print("Case 4: Null Matrix")
    print(f"Matrix:\n{mat}")
    print(f"Row echelon form:\n{mat.row_echelon()}")
    print(f"Rank: {rank_value}")  # Should be 0
    print()

    # Case 5: 2x4 rectangular matrix with full rank by rows
    mat = Matrix([
        [1.0, 2.0, 3.0, 4.0],
        [5.0, 6.0, 7.0, 8.0]
    ])
    rank_value = matrix_rank(mat)
    print("Case 5: 2x4 Rectangular Matrix")
    print(f"Matrix:\n{mat}")
    print(f"Row echelon form:\n{mat.row_echelon()}")
    print(f"Rank: {rank_value}")  # Should be 2
    print()

    # Case 6: Matrix with a row of zeros
    mat = Matrix([
        [1.0, 2.0, 3.0],
        [0.0, 0.0, 0.0],
        [4.0, 5.0, 6.0]
    ])
    rank_value = matrix_rank(mat)
    print("Case 6: Matrix with a Row of Zeros")
    print(f"Matrix:\n{mat}")
    print(f"Row echelon form:\n{mat.row_echelon()}")
    print(f"Rank: {rank_value}")  # Should be 2
    print()

    # Case 7: Rank explanation
    print("Interpretation of Matrix Rank:")
    print("1. The rank of a matrix is the number of linearly independent rows (or columns).")
    print("2. It is the dimension of the image space of the linear transformation represented by the matrix.")
    print("3. For an m×n matrix, the rank r satisfies: 0 ≤ r ≤ min(m,n).")
    print("4. If the rank equals the number of rows, the matrix has full row rank.")
    print("5. If the rank equals the number of columns, the matrix has full column rank.")
    print("6. A square matrix is invertible if and only if its rank equals its dimension.")
    print("7. By the rank-nullity theorem: dim(ker(A)) + rank(A) = n, where n is the number of columns.")
    print("   This relates the dimension of the null space with the rank of the matrix.")


if __name__ == "__main__":
    main()
