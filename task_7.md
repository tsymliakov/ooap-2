# Решение задания 7


В Python, когда происходит запихивание объекта в коллекцию set, dict или
frozenset, у такого объекта происходит вызов метода `__hash__`. Для
осуществления такого вызова интерпретатор рассматривает последовательность из
объекта, класса, родительских классов в порядке множественного наследования на
предмет наличия метода `__hash__`. Динамическое связывание в этом случае
позволяет определить метод `__hash__` в суперклассе, а потомка этого класса
запихнуть в коллекцию.
