import pickle
from copy import deepcopy
from typing import final


class General:  # неявно наследуется от object
    def __init__(self):
        raise NotImplementedError()

    # запросы
    # глубокое копирование содержимого в другой объект
    @final
    def copy(self, other):
        other.__dict__ = deepcopy(self.__dict__)

    # создает новый объект с глубоким копированием исходного объекта
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

    # является ли тип текущего объекта типом classtype
    @final
    def is_type(self, classtype):
        return type(self) is classtype

    # получение типа класса
    # этот метод реализован в object

    # наглядное представление содержимого объекта в текстовом формате
    @final
    def __str__(self):
        return f'{self.__dict__}'

    # сравнение объектов (включая глубокий вариант)
    @final
    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Any(General):
    def __init__(self):
        return
