# Решение задания 5

Язык Python, который я использую, поддерживает первый, второй, третий и пятый
принципы. С четвертым возникает проблема ввиду того, что в Python нельзя
реализовать перегрузку по аргументам различных типов.

Выполнение **первого** принцип достигается путем "утиной" типизации. **Второй**
принцип выполняется за счет гибкой системы модулей python. Выполнение
**третьего** принципа можно наблюдать в больших фреймворках и библиотеках: в
numpy множество подмодулей для решения различного рода задач, а модули, входящие
в фреймворк django, способны решать задачи от шаблонизации HTML-документов до
предложения готовых реализации ORM к множеству баз данных. Пятый принцип отчасти
следует из второго принципа, вновь, благодаря гибкой системе существует
возможность реализации модуля, содержащего в себе функционал других модулей.