# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: alaparic <alaparic@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/30 20:56:13 by alaparic          #+#    #+#              #
#    Updated: 2025/12/01 12:57:59 by alaparic         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from typing import TypeVar, Generic, List
import numbers

T = TypeVar('T', bound=numbers.Number)


class Vector(Generic[T]):
    def __init__(self, data: List[T]) -> None:
        for i, item in enumerate(data):
            if not isinstance(item, numbers.Number):
                raise TypeError(f"All values must be numbers. "
                                f"Element at index {i} is not a number: {item}")
        self.data = data

    """ Basic vector operations """

    def add(self, other: 'Vector[T]') -> 'Vector[T]':
        if not isinstance(other, Vector):
            raise TypeError("The operand must be a Vector.")
        if len(self.data) != len(other.data):
            raise ValueError("Vectors must be of the same length to sum.")
        summed_data = [a + b for a, b in zip(self.data, other.data)]
        return Vector(summed_data)

    def __add__(self, other: 'Vector[T]') -> 'Vector[T]':
        return self.add(other)

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

    """ ex03 addition """

    def dot(self, other: 'Vector[T]') -> T:
        if len(self) != len(other):
            raise ValueError(
                "Vectors must be of the same length to compute dot product.")

        return sum(a * b for a, b in zip(self.data, other.data))

    def __matmul__(self, other: 'Vector[T]') -> T:
        return self.dot(other)

    """ ex04 addition """

    def norm_1(self) -> T:
        return sum(abs(x) for x in self.data)

    def norm(self) -> T:
        return sum(abs(x) ** 2 for x in self.data) ** 0.5

    def norm_inf(self) -> T:
        return max(abs(x) for x in self.data)

    """ Utility methods """

    def __len__(self) -> int:
        return len(self.data)

    def __str__(self) -> str:
        return f"{self.data}"

    def __repr__(self) -> str:
        return f"{self.data}"

    def __iter__(self):
        return iter(self.data)
