# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Matrix.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/01 12:30:48 by alaparic          #+#    #+#              #
#    Updated: 2025/12/01 19:58:10 by alaparic         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import TypeVar, Generic, List, Tuple, Callable
import numbers
from Vector import Vector

T = TypeVar('T', bound=numbers.Number)


class Matrix(Generic[T]):
    pass


O = TypeVar('O', Vector, Matrix)


class Matrix(Generic[T]):
    def __init__(self, data: List[List[T]]):
        if not data or not all(len(row) == len(data[0]) for row in data):
            raise ValueError(
                "All rows must have the same length and matrix cannot be empty.")
        for i, row in enumerate(data):
            for j, item in enumerate(row):
                if not isinstance(item, numbers.Number):
                    raise TypeError(f"All values must be numbers. "
                                    f"Element at position ({i}, {j}) is not a number: {item}")

        self.data = data

    """ Basic matrix operations """

    def add(self, other: 'Matrix[T]') -> 'Matrix[T]':
        if self.shape() != other.shape():
            raise ValueError("Matrices must have the same dimensions to add.")

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
                "Matrices must have the same dimensions to subtract.")

        subbed_data = [
            [a - b for a, b in zip(row_self, row_other)]
            for row_self, row_other in zip(self.data, other.data)
        ]

        return Matrix(subbed_data)

    def __sub__(self, other: 'Matrix[T]') -> 'Matrix[T]':
        return self.sub(other)

    def scl(self, scalar: T) -> 'Matrix[T]':
        if not isinstance(scalar, numbers.Number):
            raise TypeError("Scalar must be a number.")

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
                "Matrix columns must match Vector/Matrix rows for multiplication.")

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
                "Matrix A's columns must match Matrix B's rows for multiplication.")

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
            raise TypeError("Unsupported type for matrix multiplication.")

    """ ex09 addition """

    def transpose(self) -> 'Matrix[T]':
        if not self.data:
            raise ValueError("Matrix is empty.")

        rows, cols = self.shape()

        result = [[self.data[j][i] for j in range(rows)] for i in range(cols)]

        return Matrix(result)

    """ Utility methods """

    def shape(self) -> Tuple[int, int]:
        return len(self.data), len(self.data[0])

    def __str__(self) -> str:
        rows = [
            '[' + ', '.join(f"{item}" for item in row) + ']' for row in self.data]
        return '[' + ',\n '.join(rows) + ']\n'

    def __repr__(self) -> str:
        rows = [
            '[' + ', '.join(f"{item}" for item in row) + ']' for row in self.data]
        return '[' + ',\n '.join(rows) + ']\n'
