import pytest
from task_14 import Vector


def test_sum_usual_vectors():
    v1 = Vector([1, 2, 3])
    v2 = Vector([4, 5, 6])

    assert v1 + v2 == Vector([5, 7, 9])


def test_sum_complex_vectors():
    v1_1 = Vector([1, 1, 1])
    v1_2 = Vector([1, 1, 1])

    v2_1 = Vector([v1_1, 5])
    v2_2 = Vector([v1_2, 5])

    assert v2_1 + v2_2 == Vector([Vector([2, 2, 2]), 10])
