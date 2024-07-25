from unittest import TestCase, main
from AlexPyLibSquare.circle import Circle
from AlexPyLibSquare.triangle import Triangle


class TestCircle(TestCase):

    def test_name(self):
        self.assertEqual(Circle(1).name(), "Круг")

    def test_area(self):
        self.assertEqual(Circle(1).area(), 3.141592653589793)

    def test_perimeter(self):
        self.assertEqual(Circle(1).perimeter(), 6.283185307179586)


class TestTriangle(TestCase):

    def setUp(self):
        self.triangles = [(1, 1), (1, 2), (2, 3, 4), (3, 4, 5), (3, 4, 10)]
        self.count = len(self.triangles)
        self.areas = [0.4330127018922193, 0.9682458365518543, 2.9047375096555625, 6.0,
                      f"ValueError('Треугольника с такими сторонами не существует')"]
        self.perimeters = [3.0, 5.0, 9.0, 12.0, f"ValueError('Треугольника с такими сторонами не существует')"]
        self.is_rectangular = [False, False, False, True,
                               f"ValueError('Треугольника с такими сторонами не существует')"]
        # self.tr_0 = 1  # равносторонний
        # self.tr_1 = (1, 2)  # равнобедренный
        # self.tr_2 = (2, 3, 4)  # не прямоугольный
        # self.tr_3 = (3, 4, 5)  # прямоугольный
        # self.tr_4 = (3, 4, 10)  # не существует

    def test_is_valid(self):
        for i, param in enumerate(self.triangles):
            if i != 4:
                self.assertTrue(Triangle(*param).is_valid())
            else:
                self.assertFalse(Triangle(*param).is_valid())

    def test_name(self):
        for i, param in enumerate(self.triangles):
            self.assertEqual(Triangle(*param).name(), "Треугольник")

    def test_area(self):
        for i in range(self.count):
            self.assertEqual(Triangle(*self.triangles[i]).area(), self.areas[i])

    def test_perimeter(self):
        for i in range(self.count):
            self.assertEqual(Triangle(*self.triangles[i]).perimeter(), self.perimeters[i])

    def test_is_rectangular(self):
        for i in range(self.count):
            self.assertEqual(Triangle(*self.triangles[i]).is_rectangular(), self.is_rectangular[i])


if __name__ == '__main__':
    main()
