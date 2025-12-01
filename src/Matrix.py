# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Matrix.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/01 12:30:48 by alaparic          #+#    #+#              #
#    Updated: 2025/12/01 13:05:32 by alaparic         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import TypeVar, Generic, List, Tuple, Callable
import numbers

T = TypeVar('T', bound=numbers.Number)


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

    """ Utility methods """

    def shape(self) -> Tuple[int, int]:
        return len(self.data), len(self.data[0])

    def __str__(self) -> str:
        rows = [
            '[' + ', '.join(f"{item}" for item in row) + ']' for row in self.data]
        return '[' + ',\n '.join(rows) + ']\n'
