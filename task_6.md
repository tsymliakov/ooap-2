# Решение задания 6


Если у модуля есть публичная связь с другим модулем- существует вероятность, что
дизайн этого модуля предполагает возможность настраивать эту связь. Например, в
наследнике поменять связумый модуль на другой. Исходя из этих размышлений я
отвечу положительно, такие ситуации существуют.


По поводу метрик- хочется предложить метрику, говорящую о том, как много не
базовых типов использует конкретная функция модуля. Чем меньше не базовых типов
используется- тем более автономной является функция.


По предложенной мной метрике это, пожалуй, никак не определить.
