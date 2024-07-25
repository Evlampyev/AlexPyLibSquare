from AlexPyLibSquare.circle import Circle
from AlexPyLibSquare.triangle import Triangle

if __name__ == "__main__":
    fig_1 = Circle(10)
    print(f"{fig_1.name()}\nПлощадь:{fig_1.area()}\nПериметр: {fig_1.perimeter()}")
    print()

    fig_2 = Triangle(3, 4, 5)
    print(f"{fig_2.name()}\nПериметр: {fig_2.perimeter()}\nПлощадь: {fig_2.area()}")
    print(fig_2.is_rectangular())
    print()

    fig_3 = Triangle(3, 4, 10)
    print(fig_3.is_valid())
    print(f"{fig_3.name()}\nПериметр: {fig_3.perimeter()}\nПлощадь: {fig_3.area()}")
    print()

    fig_4 = Triangle(30, 40, 50)
    print(fig_4.is_valid())
    print(f"{fig_4.name()}\nПериметр: {fig_4.perimeter()}\nПлощадь: {fig_4.area()}")
    print(fig_4.is_rectangular())