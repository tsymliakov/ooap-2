Рефлексия по заданию 11


В предложенном решении сказано, что python позвоялет создать любой класс без
предков/ потомков, не входящий в используемую систему типов, исходящую от
General, ввиду отсутствия проверки типов.


Но при этом python позволяет выполнить условие задания: создать иерархию можно.
Замкнуть - уже не слишком. Можно пойти на ухищрение, установив запрет на
переопределение методов посредством декоратора @final, а в самих методах оставив
`raise NotImplemented` или нечто похожее.