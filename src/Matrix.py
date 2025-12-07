# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Matrix.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/01 12:30:48 by alaparic          #+#    #+#              #
#    Updated: 2025/12/07 14:33:27 by alaparic         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import TypeVar, Generic, List, Tuple
import numbers
from unittest import result
from Vector import Vector

T = TypeVar('T', bound=numbers.Number)
O = TypeVar('O')


class Matrix(Generic[T]):
    def __init__(self, data: List[List[T]]):
        if not data or not all(len(row) == len(data[0]) for row in data):
            raise ValueError(
                "\033[0;31mAll rows must have the same length and matrix cannot be empty.\033[0m")
        for i, row in enumerate(data):
            for j, item in enumerate(row):
                if not isinstance(item, numbers.Number):
                    raise TypeError(f"\033[0;31mAll values must be numbers. "
                                    f"Element at position ({i}, {j}) is not a number: {item}\033[0m")

        self.data = data

    """ Basic matrix operations """

    def add(self, other: 'Matrix[T]') -> 'Matrix[T]':
        if self.shape() != other.shape():
            raise ValueError(
                "\033[0;31mMatrices must have the same dimensions to add.\033[0m")

        summed_data = [
            [a + b for a, b in zip(row_self, row_other)]
            for row_self, row_other in zip(self.data, other.data)
        ]

        return Matrix(summed_data)

    def __add__(self, other: 'Matrix[T]') -> 'Matrix[T]':
        return self.add(other)

    def sub(self, other: 'Matrix[T]') -> 'Matrix[T]':
        if self.shape() != other.shape():
            raise ValueError(
                "\033[0;31mMatrices must have the same dimensions to subtract.\033[0m")

        subbed_data = [
            [a - b for a, b in zip(row_self, row_other)]
            for row_self, row_other in zip(self.data, other.data)
        ]

        return Matrix(subbed_data)

    def __sub__(self, other: 'Matrix[T]') -> 'Matrix[T]':
        return self.sub(other)

    def __neg__(self) -> 'Matrix[T]':
        return self.scl(-1)

    def scl(self, scalar: T) -> 'Matrix[T]':
        if not isinstance(scalar, numbers.Number):
            raise TypeError("\033[0;31mScalar must be a number.\033[0m")

        scaled_data = [
            [item * scalar for item in row] for row in self.data
        ]

        return Matrix(scaled_data)

    def __mul__(self, scalar: T) -> 'Matrix[T]':
        return self.scl(scalar)

    def __rmul__(self, scalar: T) -> 'Matrix[T]':
        return self.scl(scalar)

    """ ex07 addition """

    def mul_vec(self, vec: 'Vector[T]') -> 'Vector[T]':
        rows, cols = self.shape()

        if cols != len(vec):
            raise ValueError(
                "\033[0;31mMatrix columns must match Vector/Matrix rows for multiplication.\033[0m")

        result = []
        for i in range(rows):
            row_vector = Vector([self.data[i][j] for j in range(cols)])
            result.append(row_vector @ vec)

        return Vector(result)

    def mul_mat(self, other: 'Matrix[T]') -> 'Matrix[T]':
        rows1, cols1 = self.shape()
        rows2, cols2 = other.shape()

        if cols1 != rows2:
            raise ValueError(
                "\033[0;31mMatrix A's columns must match Matrix B's rows for multiplication.\033[0m")

        result = [[0 for _ in range(cols2)] for _ in range(rows1)]

        for i in range(rows1):
            for j in range(cols2):
                sum_product = 0
                for k in range(cols1):
                    sum_product += self.data[i][k] * other.data[k][j]
                result[i][j] = sum_product

        return Matrix(result)

    def __matmul__(self, other: O) -> O:
        if isinstance(other, Vector):
            return self.mul_vec(other)
        elif isinstance(other, Matrix):
            return self.mul_mat(other)
        else:
            raise TypeError(
                "\033[0;31mUnsupported type for matrix multiplication.\033[0m")

    """ ex09 addition """

    def transpose(self) -> 'Matrix[T]':
        if not self.data:
            raise ValueError("\033[0;31mMatrix is empty.\033[0m")

        rows, cols = self.shape()

        result = [[self.data[j][i] for j in range(rows)] for i in range(cols)]

        return Matrix(result)

    """ ex10 addition """

    def row_echelon(self) -> 'Matrix[T]':
        rows, cols = self.shape()

        result = [row[:] for row in self.data]

        current_row = 0

        for col in range(cols):
            # Find the pivot (first non-zero element in current column)
            pivot_row = None
            for row in range(current_row, rows):
                if result[row][col] != 0:
                    pivot_row = row
                    break

            # If no pivot found, move to next column
            if pivot_row is None:
                continue

            # Swap current row with pivot row if needed
            if pivot_row != current_row:
                result[current_row], result[pivot_row] = result[pivot_row], result[current_row]

            # Eliminate all rows below the pivot
            pivot_value = result[current_row][col]
            for row in range(current_row + 1, rows):
                if result[row][col] != 0:
                    factor = result[row][col] / pivot_value
                    for c in range(cols):
                        result[row][c] -= factor * result[current_row][c]

            current_row += 1

            if current_row >= rows:
                break

        return Matrix(result)

    """ Utility methods """

    def shape(self) -> Tuple[int, int]:
        return len(self.data), len(self.data[0])

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, index: int) -> List[T]:
        return self.data[index]

    def __str__(self) -> str:
        rows = [
            '[' + ', '.join(f"{item}" for item in row) + ']' for row in self.data]
        return '[' + ',\n '.join(rows) + ']\n'

    def __repr__(self) -> str:
        rows = [
            '[' + ', '.join(f"{item}" for item in row) + ']' for row in self.data]
        return '[' + ',\n '.join(rows) + ']\n'
