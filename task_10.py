from typing import final


class Parent():
    @final # декоратор даст понять type cheker'ам о том, что метод нельзя переопределять
    # Но переопределение метода в наследнике не приведет ни к какой ошибке
    def method(self):
        print('Parent method')


class Child(Parent):
    def method(self):
        print('Child method')
