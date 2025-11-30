# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/30 20:56:13 by alaparic          #+#    #+#              #
#    Updated: 2025/11/30 20:56:46 by alaparic         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import TypeVar, Generic, List, Tuple, Callable
import numbers
import copy

T = TypeVar('T', bound=numbers.Number)


class Vector(Generic[T]):
    def __init__(self, data: List[T]) -> None:
        for i, item in enumerate(data):
            if not isinstance(item, numbers.Number):
                raise TypeError(f"All values must be numbers. "
                                f"Element at index {i} is not a number: {item}")
        self.data = data

    """ Basic vector operations """

    def sum(self, other: 'Vector[T]') -> 'Vector[T]':
        if not isinstance(other, Vector):
            raise TypeError("The operand must be a Vector.")
        if len(self.data) != len(other.data):
            raise ValueError("Vectors must be of the same length to sum.")
        summed_data = [a + b for a, b in zip(self.data, other.data)]
        return Vector(summed_data)

    def __add__(self, other: 'Vector[T]') -> 'Vector[T]':
        return self.sum(other)

    def sub(self, other: 'Vector[T]') -> 'Vector[T]':
        if not isinstance(other, Vector):
            raise TypeError("The operand must be a Vector.")
        if len(self.data) != len(other.data):
            raise ValueError("Vectors must be of the same length to subtract.")
        subbed_data = [a - b for a, b in zip(self.data, other.data)]
        return Vector(subbed_data)

    def __sub__(self, other: 'Vector[T]') -> 'Vector[T]':
        return self.sub(other)

    def scl(self, scalar: T) -> 'Vector[T]':
        if not isinstance(scalar, numbers.Number):
            raise TypeError("Scalar must be a number.")
        scaled_data = [a * scalar for a in self.data]
        return Vector(scaled_data)

    def __mul__(self, scalar: T) -> 'Vector[T]':
        return self.scl(scalar)

    def __rmul__(self, scalar: T) -> 'Vector[T]':
        return self.scl(scalar)

    """ Utility methods """

    def __str__(self) -> str:
        return f"{self.data}"

    def __repr__(self) -> str:
        return f"{self.data}"
