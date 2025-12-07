# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ex15.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/07 12:43:33 by alaparic          #+#    #+#              #
#    Updated: 2025/12/07 13:16:16 by alaparic         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


from Vector import Vector
from Matrix import Matrix
from ex01 import linear_combination_vector, linear_combination_matrix
from ex02 import linear_interpolation as lerp
from ex05 import angle_cos
from ex08 import trace
from ex11 import determinant
from ex12 import inverse
from ex13 import matrix_rank


class ComplexMatrix(Matrix):
    """Matrix with specific operations for complex numbers"""

    def mul_vec(self, vec: 'Vector[float]') -> 'Vector[float]':
        """
        Multiply this matrix by a vector (complex linear transformation).
        Unlike the base implementation, does not apply conjugation.
        """
        rows, cols = self.shape()

        if cols != len(vec):
            raise ValueError(f"Incompatible dimensions for matrix-vector multiplication: "
                             f"matrix {rows}×{cols}, vector of dimension {len(vec)}")

        # Create a result vector
        result = []

        # For each row of the matrix
        for i in range(rows):
            # Calculate the dot product without conjugation
            sum_product = 0
            for j in range(cols):
                sum_product += self.data[i][j] * vec.data[j]  # No conjugation
            result.append(sum_product)

        return Vector(result)

    # Overload the @ operator
    def __matmul__(self, other):
        if isinstance(other, Vector):
            return self.mul_vec(other)
        elif isinstance(other, Matrix):
            return self.mul_mat(other)
        else:
            raise TypeError(
                f"Cannot multiply a matrix with an object of type {type(other).__name__}")


def main():
    # ex00 - Add, Subtract, and Scale
    j = 1j  # define variable j to use notation like -j
    # Vectors
    w1 = Vector([1.0, 2, 3-1j])
    w2 = Vector([-2-2j, 0, -3-j])
    w3 = Vector([-2-2j, -1, -3-j])
    print("Vector sum:", w1 + w2 + w3)
    print("Vector subtraction:", w1 - w2)
    print("Vector scaling:", w1 * 2.0)

    # Matrices
    m1 = Matrix([[1.0 + j, 2 - j], [3 - 2j, 4]])
    m2 = Matrix([[5 + 3j, 6 - 2j], [7 - 2j, 3]])
    m3 = Matrix([[0, j], [-j, -1]])
    print("\nMatrix sum:\n", m1 + m2 + m3)
    print("\nMatrix subtraction:\n", m1 - m2)
    print("\nMatrix scaling:\n", m1 * 2.0)

    # ex01 - Linear combination
    # Linear combination with complex vectors
    w1 = Vector([1.0, 2.0, 3.0-1j])
    w2 = Vector([-2.0-2j, 0.0, -3.0-j])
    w3 = Vector([-2.0-2j, -1.0, -3.0-j])
    coefs = [2.0, -1.0+1j, 3.0-2j]
    result = linear_combination_vector([w1, w2, w3], coefs)
    print(f"Linear combination of complex vectors = {result}")

    # Linear combination with complex matrices
    m1 = Matrix([[1.0+j, 2.0-j], [3.0-2j, 4.0]])
    m2 = Matrix([[5.0+3j, 6.0-2j], [7.0-2j, 8.0]])
    m3 = Matrix([[0.0, j], [-j, -1.0]])
    coefs = [1.5+0.5j, -0.5-j, 2.0+j]
    result = linear_combination_matrix([m1, m2, m3], coefs)
    print("Linear combination of complex matrices:")
    print(result)

    # ex02 - Linear interpolation
    # Linear interpolation with complex vectors
    v1 = Vector([1.0, 2.0+1j])
    v2 = Vector([3.0-j, 4.0+2j])
    print(f"lerp({v1}, {v2}, 0.5) = {lerp(v1, v2, 0.5)}")
    # Linear interpolation with complex matrices
    m1 = Matrix([[1.0+j, 2.0-j], [3.0-2j, 4.0]])
    m2 = Matrix([[5.0+3j, 6.0-2j], [7.0-2j, 8.0]])
    print("Matrix m1:")
    print(m1)
    print("\nMatrix m2:")
    print(m2)
    print(f"\nlerp(m1, m2, 0.5) = ")
    print(lerp(m1, m2, 0.5))

    # ex03 - Dot product
    u = Vector([1+2j, 3-1j])
    v = Vector([2-1j, 1+1j])
    print(f"{u} · {v} = {u.dot(v)}")

    # ex04 - Norm
    u = Vector([1+2j, 3-4j, -2+5j])
    print(f"Vector: {u}")
    print(f"Norm-1: {u.norm_1()}")
    print(f"Norm-2: {u.norm()}")
    print(f"Norm-∞: {u.norm_inf()}")

    # ex05 - Cosine
    u = Vector([1+1j, 2-2j])
    v = Vector([2+0j, 0+3j])
    print(f"u = {u}, v = {v}")
    print(f"cos(u, v) = {angle_cos(u, v)}")

    # ex06 - Cross product
    # The vector product is defined in R^3
    # where it produces a vector perpendicular to the originals

    # ex07 - Linear transformation, Matrix multiplication
    # Test with identity matrix
    print("Test with identity matrix:")
    M = ComplexMatrix([[1+0j, 0+0j], [0+0j, 1+0j]])
    v = Vector([1+j, 2-j])
    result = M @ v
    print(f"Original vector: {v}")
    print(f"Matrix @ Vector: {result}")
    print(f"Are they equal? {v.data == result.data}")

    # ex08 - Trace
    mat = Matrix([[1+2j, 3-4j], [5+6j, 7-8j]])
    print(f"Matrix:\n{mat}")
    print(f"Trace: {trace(mat)}")  # (1+2j) + (7-8j) = 8-6j

    # ex09 - Transpose
    mat = Matrix([[1+2j, 3-4j], [5+6j, 7-8j]])
    print(f"\nOriginal matrix:\n{mat}")
    print(f"\nTransposed matrix:\n{mat.transpose()}")

    # ex10 - Row echelon form
    # 3x2 rectangular matrix with complex values
    mat = Matrix([
        [1+j, 2-j],
        [3, 4+2j],
        [5-j, 6+j]
    ])
    print(mat)
    print("\nRow echelon form:")
    print(mat.row_echelon())

    # ex11 - Determinant
    mat = Matrix([[1+j, 2-j],
                  [3-2j, 4+j]])
    print(mat)
    print(f"Determinant: {determinant(mat)}")

    # ex12 - Inverse
    mat = Matrix([[1+j, 2-j],
                  [3-2j, 4+j]])

    print("Complex 2x2 matrix:")
    print(mat)
    print(f"\nDeterminant: {determinant(mat)}")
    inv = inverse(mat)
    print(f"\nInverse matrix:\n{inv}")

    # ex13 - Rank
    # Complex 3x3 matrix with linear dependence
    # The third row is the sum of the first two
    mat = Matrix([
        [1+j, 2-j, 3],
        [0, 2+j, 4-2j],
        [1+j, 4, 7-2j]  # (row 1) + (row 2)
    ])

    rank_value = matrix_rank(mat)
    print("Case 2: Complex matrix with linear dependence")
    print(f"Matrix:\n{mat}")
    print(f"Row echelon form:\n{mat.row_echelon()}")
    print(f"Rank: {rank_value}")  # Should be 2


if __name__ == "__main__":
    main()
