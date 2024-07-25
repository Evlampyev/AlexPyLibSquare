from AlexPyLibSquare.figure import Figure
from AlexPyLibSquare.validate import NumberValidator


class Triangle(Figure):
    a = NumberValidator()
    b = NumberValidator()
    c = NumberValidator()

    def __init__(self, *args):

        if len(args) > 3 or len(args) == 0:
            raise ValueError("Количество аргументов должно быть от 1 до 3")
        elif len(args) == 1:
            a, b, c = args[0], args[0], args[0]
        elif len(args) == 2:
            a, b, c = args[0], args[1], args[1]
        else:
            a, b, c = args
        self.a = a
        self.b = b
        self.c = c
        self.validate = self.is_valid()

    def area(self):
        if self.validate:
            p = (self.a + self.b + self.c) / 2
            return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
        else:
            return f"ValueError('Треугольника с такими сторонами не существует')"

    def perimeter(self):
        if self.validate:
            return self.a + self.b + self.c
        else:
            return f"ValueError('Треугольника с такими сторонами не существует')"

    def name(self):
        return "Треугольник"

    def is_rectangular(self):
        """Проверка на прямоугольность"""
        if self.validate:
            if (self.a ** 2 + self.b ** 2 == self.c ** 2 or self.a ** 2 + self.c ** 2 == self.b ** 2 or
                    self.b ** 2 + self.c ** 2 == self.a ** 2):
                return True
            else:
                return False
        else:
            return f"ValueError('Треугольника с такими сторонами не существует')"

    def is_valid(self):
        """Проверка на существование"""
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            return True
        else:
            return False

    def __str__(self):
        return f"Треугольник со сторонами {self.a}, {self.b}, {self.c}"
