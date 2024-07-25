from AlexPyLibSquare.figure import Figure
from AlexPyLibSquare.validate import NumberValidator
import math


class Circle(Figure):
    radius = NumberValidator()

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def name(self):
        return "Круг"

    def __str__(self):
        return f"Круг с радиусом {self.radius}"
