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

    def test_circle_perimeter(self):
        # Тест 4: проверяем правильность вычисления периметра для положительного радиуса
        self.assertAlmostEqual(circle.perimeter(2), 2 * math.pi * 2)
        # Тест 5: проверяем правильность вычисления периметра для нулевого радиуса
        self.assertAlmostEqual(circle.perimeter(0), 0)
        # Тест 6: проверяем правильность вычисления периметра для отрицательного радиуса
        self.assertAlmostEqual(circle.perimeter(3), 2 * math.pi * 3)

        # Тест 7: проверяем правильность вычисления площади для очень большого числа
        self.assertAlmostEqual(circle.area(1e100), math.pi * (1e100) * (1e100))

        # Тест 8: проверяем вызов исключения для некорректного ввода
        with self.assertRaises(TypeError):
            circle.perimeter("radius")
        with self.assertRaises(TypeError):
            circle.perimeter(None)

    def test_square_area(self):
        # Тест 1: проверяем правильность вычисления площади для положительной стороны
        self.assertEqual(square.area(5), 5 * 5)
        # Тест 2: проверяем правильность вычисления площади для нулевой стороны
        self.assertEqual(square.area(0), 0)
        # Тест 3: проверяем правильность вычисления площади для отрицательной стороны
        self.assertEqual(square.area(-3), 3 * 3)

    def test_square_perimeter(self):
        # Тест 1: проверяем правильность вычисления периметра для положительной стороны
        self.assertEqual(square.perimeter(5), 4 * 5)
        # Тест 2: проверяем правильность вычисления периметра для нулевой стороны
        self.assertEqual(square.perimeter(0), 0)
        # Тест 3: проверяем правильность вычисления периметра для отрицательной стороны
        self.assertEqual(square.perimeter(3), 4 * 3)

    def test_rectangle_area(self):
        # Тест 1: проверяем правильность вычисления площади для положительных сторон
        self.assertEqual(rectangle.area(5, 3), 5 * 3)
    def test_rectangle_perimeter(self):
        # Тест 1: проверяем правильность вычисления периметра для положительных сторон
        self.assertEqual(rectangle.perimeter(5, 3), 2 * (5 + 3))

    def test_triangle_area(self):
        # Тест 1: проверяем правильность вычисления площади для положительной основы и высоты
        self.assertEqual(triangle.area(4, 3), 4 * 3 / 2)
        # Тест 2: проверяем правильность вычисления площади для нулевой основы
        self.assertEqual(triangle.area(0, 3), 0)
        # Тест 3: проверяем правильность вычисления площади для отрицательной основы
        self.assertEqual(triangle.area(-4, 3), -4 * 3 / 2)
        # Тест 4: проверяем правильность вычисления площади для нулевой высоты
        self.assertEqual(triangle.area(4, 0), 0)
        # Тест 5: проверяем правильность вычисления площади для отрицательной высоты
        self.assertEqual(triangle.area(4, -3), 4 * -3 / 2)

    def test_triangle_perimeter(self):
        # Тест 1: проверяем правильность вычисления периметра для положительных сторон
        self.assertEqual(triangle.perimeter(5, 3, 4), 5 + 3 + 4)

if __name__ == '__main__':
    unittest.main()