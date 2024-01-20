# Рефлексия по заданию 16


Полиморфным вызовом в Python считается такой вызов, при котором переменная одного типа начинает себя вести так, будто она переменная другого типа.

Например, определив метод Method_1 в базовом классе и унаследовав от этого класса наследника Child, чтобы затем вызвать у объекта типа Child метод Method_1, будет получен полиморфный вызов.


В занятии указано, что ковариантный вызов отличается от полиморфного тем, что логика обработки входного аргумента напрямую зависит от типа этого аргумента.

Возможно сказать, что в приведенном далее примере логика обработки зависит от типа a.

``` python
def method(a):
    if type(a) is A:
        pass
    else if type(a) is B:
        pass
```

В предложенном решении производится вызов метода shake_box, который производит вызов метода make_sound у передаваемого аргумента. Что в результате приводит к тому, что вне зависимости от типа аргумента box вызывается один и тот же метод. Что фактически в python представляет собой то, что называют "утиной типизацией". Сам по себе тип не важен при вызове, а важно лишь то, чтобы он умел этот вызов обработать (имел соответствующий метод). 