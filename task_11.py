import pickle
from copy import deepcopy
from typing import final


class General:  # неявно наследуется от object
    def __init__(self):
        raise NotImplementedError()

    @final
    def copy(self, other):
        other.__dict__ = deepcopy(self.__dict__)

    @final
    def clone(self):
        return deepcopy(self)

    @final
    def serialize(self):
        return pickle.dumps(self)

    @final
    @staticmethod
    def deserialize(serialized_obj):
        return pickle.loads(serialized_obj)

    @final
    def is_type(self, classtype):
        return type(self) is classtype

    @final
    def __str__(self):
        return f'{self.__dict__}'

    @final
    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Any(General):
    def __init__(self):
        return


class Vector(Any):
    def __init__(self, *values):
        self._vector = values


class Matrix(Any):
    def __init__(self, *values):
        self._matrix = values


# Замыкание системы типов снизу, поскольку python
# разрешает множественное значение
class NoneValue(Vector, Matrix):
    pass


# Если я все правильно понял, замыкание системы типов проекта на NoneValue
# позволяет мне использовать его в тех случаях, в которых я бы применил
# стандартное для Python значение None. При этом не выходя за рамки типов моего
# проекта. Не ясно, а что за этим стоит, но наверное, Type Theory не зря
# существует, и я уверен, что она способна дать ответ на мой вопрос.
Void = NoneValue()

V = Vector(1, 2, 3)
M = Matrix([1, 2], [1, 2])


# Воот, каким- то образом в переменной V могло бы оказаться отсутствие значения.
# В принципе, я мог бы сделать и так: V == None.
print(V == Void)


# Полиморфность значения Void заключается в том, что его можно использовать
# в операциях как со значениями как типа Matrix, так и типа Vector
print(M == Void)
