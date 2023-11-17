import unittest
import math

import circle
import square
import rectangle
import triangle

class TestCircleFunctions(unittest.TestCase):
    def test_circle_area(self):
        # Тест 1: проверяем правильность вычисления площади для положительного радиуса
        self.assertAlmostEqual(circle.area(2), math.pi * 2 * 2)
        # Тест 2: проверяем правильность вычисления площади для нулевого радиуса
        self.assertAlmostEqual(circle.area(0), 0)
        # Тест 3: проверяем правильность вычисления площади для отрицательного радиуса
        self.assertAlmostEqual(circle.area(3), math.pi * 3 * 3)
        # Тест 8: проверяем правильность вычисления площади для очень большого числа
        self.assertAlmostEqual(circle.area(1e100), math.pi * (1e100) * (1e100))

    def test_circle_perimeter(self):
        # Тест 4: проверяем правильность вычисления периметра для положительного радиуса
        self.assertAlmostEqual(circle.perimeter(2), 2 * math.pi * 2)
        # Тест 5: проверяем правильность вычисления периметра для нулевого радиуса
        self.assertAlmostEqual(circle.perimeter(0), 0)
        # Тест 6: проверяем правильность вычисления периметра для отрицательного радиуса
        self.assertAlmostEqual(circle.perimeter(3), 2 * math.pi * 3)
        # Тест 9: проверяем правильность вычисления площади для очень большого числа
        self.assertAlmostEqual(circle.area(1e100), math.pi * (1e100) * (1e100))

    def test_square_area(self):
        # Тест 1: проверяем правильность вычисления площади для положительной стороны
        self.assertEqual(square.area(5), 5 * 5)
        # Тест 2: проверяем правильность вычисления площади для нулевой стороны
        self.assertEqual(square.area(0), 0)
        # Тест 3: проверяем правильность вычисления площади для отрицательной стороны
        self.assertEqual(square.area(-3), 3 * 3)
        # Тест 10: проверяем правильность вычисления площади для очень большого числа
        self.assertAlmostEqual(circle.area(1e100), math.pi * (1e100) * (1e100))

    def test_square_perimeter(self):
        # Тест 1: проверяем правильность вычисления периметра для положительной стороны
        self.assertEqual(square.perimeter(5), 4 * 5)
        # Тест 2: проверяем правильность вычисления периметра для нулевой стороны
        self.assertEqual(square.perimeter(0), 0)
        # Тест 3: проверяем правильность вычисления периметра для отрицательной стороны
        self.assertEqual(square.perimeter(3), 4 * 3)
        # Тест 10: проверяем правильность вычисления площади для очень большого числа
        self.assertAlmostEqual(circle.area(1e100), math.pi * (1e100) * (1e100))


    def test_rectangle_area(self):
        # Тест 1: проверяем правильность вычисления площади для положительных сторон
        self.assertEqual(rectangle.area(5, 10), 5 * 10)
        # Тест 2: проверяем правильность вычисления площади для нулевых сторон
        self.assertEqual(rectangle.area(0, 0), 0)
        # Тест 3: проверяем правильность вычисления площади для отрицательных сторон
        self.assertEqual(rectangle.area(-3, -5), 3 * 5)
        # Тест 11: проверяем правильность вычисления площади для очень больших чисел
        self.assertAlmostEqual(rectangle.area(1e100, 1e200), 1e100 * 1e200)


    def test_rectangle_perimeter(self):
        # Тест 1: проверяем правильность вычисления периметра для положительных сторон
        self.assertEqual(rectangle.perimeter(5, 10), 2 * (5 + 10))
        # Тест 2: проверяем правильность вычисления периметра для нулевых сторон
        self.assertEqual(rectangle.perimeter(0, 0), 0)
        # Тест 3: проверяем правильность вычисления периметра для отрицательных сторон
        self.assertEqual(rectangle.perimeter(3, 5), 2 * (3 + 5))
        # Тест 11: проверяем правильность вычисления площади для очень больших чисел
        self.assertAlmostEqual(rectangle.area(1e100, 1e200), 1e100 * 1e200)

    def test_triangle_area(self):
        # Тест 1: проверяем правильность вычисления площади для положительных основания и высоты
        self.assertEqual(triangle.area(4, 3), 0.5 * 4 * 3)
        # Тест 2: проверяем правильность вычисления площади для нулевых основания и высоты
        self.assertEqual(triangle.area(0, 0), 0)
        # Тест 3: проверяем правильность вычисления площади для отрицательных основания и высоты
        self.assertEqual(triangle.area(-4, -3), 0.5 * 4 * 3)
        # Тест 12: проверяем правильность вычисления площади для очень больших чисел
        self.assertAlmostEqual(triangle.area(1e100, 1e200), 0.5 * 1e100 * 1e200)


    def test_triangle_perimeter(self):
        # Тест 1: проверяем правильность вычисления периметра для положительных сторон
        self.assertEqual(triangle.perimeter(5, 4, 3), 5 + 4 + 3)
        # Тест 2: проверяем правильность вычисления периметра для нулевых сторон
        self.assertEqual(triangle.perimeter(0, 0, 0), 0)
        # Тест 3: проверяем правильность вычисления периметра для отрицательных сторон
        self.assertEqual(triangle.perimeter(-5, -4, -3), -5 + -4 + -3)
        # Тест 12: проверяем правильность вычисления площади для очень больших чисел
        self.assertAlmostEqual(triangle.area(1e100, 1e200), 0.5 * 1e100 * 1e200)

    if __name__ == '__main__':
        unittest.main()
