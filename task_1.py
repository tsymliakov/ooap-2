INFO = 0
WARNING = 1
ERROR = 2


class Logger:
    def __init__(self, *drivers):
        # Тут применяю композицию совместно с полиморфизмом.
        # Множество разных классов, тем не менее обладающих интерфейсом
        # AbstractLogDriver заключены внутрь поля drivers класса Logger
        self.drivers = list(drivers)

    def _log(self, level, message):
        for driver in self.drivers:
            driver.emit(level, message)

    def info(self, message):
        self._log(INFO, message)

    def warning(self, message):
        self._log(WARNING, message)

    def error(self, message):
        self._log(ERROR, message)


class AbstractLogDriver:
    """
    Базовый класс log-driver'а. LogDriver'ы реализуют способ
    журналируемого сообщения из приложения.
    """

    def __init__(self):
        raise NotImplemented

    def emit(self, level, message):
        raise NotImplemented

    def format(self, message):
        raise NotImplemented


# Применяю наследование. Благодаря ему не забуду реализовать нужный метод
class FileLogDriver(AbstractLogDriver):
    """
    Реализует отправку журналируемого сообщения в файл в формате RFC5424.
    """

    def __init__(self, path):
        pass

    def emit(self, level, message):
        pass

    def format(self, message):
        # тут можно реализовать форматирование сообщения по RFC5424
        # вручную, а можно применить композицию и воспользоваться сторонней
        # библиотекой

        pass
