from abc import ABCMeta, abstractmethod


class Figure(object):
    """Абстрактный класс фигуры"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def area(self) -> float:
        """Вычисляет площадь фигуры"""
        pass

    @abstractmethod
    def perimeter(self) -> float | int:
        """Вычисляет периметр фигуры"""
        pass

    @abstractmethod
    def name(self) -> str:
        """Возвращает название фигуры"""
        pass
