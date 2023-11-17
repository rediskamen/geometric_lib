def area(a, b):
    return a * b

def perimeter(a, b):
    return (a + b)*2

import unittest

class TestRectangleFunctions(unittest.TestCase):
    def test_area(self):
        # Тест 1: проверяем правильность вычисления площади для положительных сторон
        self.assertAlmostEqual(area(2, 3), 2 * 3)
        # Тест 2: проверяем правильность вычисления площади для нулевых сторон
        self.assertAlmostEqual(area(0, 0), 0)
        # Тест 3: проверяем правильность вычисления площади для отрицательных сторон
        self.assertAlmostEqual(area(-3, -4), (-3) * (-4))

    def test_perimeter(self):
        # Тест 4: проверяем правильность вычисления периметра для положительных сторон
        self.assertAlmostEqual(perimeter(2, 3), (2 + 3) * 2)
        # Тест 5: проверяем правильность вычисления периметра для нулевых сторон
        self.assertAlmostEqual(perimeter(0, 0), 0)
        # Тест 6: проверяем правильность вычисления периметра для отрицательных сторон
        self.assertAlmostEqual(perimeter(-3, -4), (-3 + -4) * 2)

        # Тест 7: проверяем правильность вычисления площади для очень большого числа
        self.assertAlmostEqual(area(1e100, 1e100), (1e100) * (1e100))

        # Тест 8: проверяем вызов исключения для некорректного ввода
        with self.assertRaises(TypeError):
            perimeter("side", 3)
        with self.assertRaises(TypeError):
            perimeter(None, 4)

if __name__ == '__main__':
    unittest.main()

