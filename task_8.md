# Решение задания 8

Сам по себе python на типы внимания не обращает. Точнее, он принимает "утиную"
типизацию, которая разрешает использовать какие угодно типы, главное, чтобы
название атрибутов совпадали. Но если воспользоваться сторонним инструментом,
например статическим анализатором типов для python, таким как pyright, то
получится внести типизацию в python. В данном примере демонстрирована
**ковариантность**:

``` python
from collection.abc import Sequence

from animals import (
    Animal,
    cat, dog, frog, goose
)

animals_seq: Sequence[Animal] = [
    cat,
    dog,
    frog,
    goose
]
```

Примерно также можно прописать аннотации и для **контрвариантного** случая.

``` python
def func_for_animal(creature: Animal):
    pass

def func_for_cat(creature: Cat):
    pass

animal = Animal()

func_for_cat(animal) # Всё работает. Статический анализатор типов не будет ругаться
```
