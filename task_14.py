from task_11 import General
from task_12 import NoneValue
from typing import TypeVar, List


Void = NoneValue()
T = TypeVar('T')


class Vector(General):
    def __init__(self, values: List[T]):
        self.values = values

    def __len__(self):
        return len(self.values)

    def __add__(self, other: "Vector[T]"):
        if len(self) != len(other):
            return Void

        return Vector([
            x + y for x, y in zip(self.get_values(), other.get_values())
        ])

    def get_values(self):
        return self.values
