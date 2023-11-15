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

def test_area():
    # Test with positive values
    a = 2
    b = 3
    expected_area = a * b
    calculated_area = area(a, b)
    assert calculated_area == expected_area, f"Error: Expected area = {expected_area}, Calculated area = {calculated_area}"

    # Test with zero values
    a = 0
    b = 0
    expected_area = 0
    calculated_area = area(a, b)
    assert calculated_area == expected_area, f"Error: Expected area = {expected_area}, Calculated area = {calculated_area}"

    # Test with negative values
    a = -3
    b = -4
    expected_area = a * b
    calculated_area = area(a, b)
    assert calculated_area == expected_area, f"Error: Expected area = {expected_area}, Calculated area = {calculated_area}"

def test_perimeter():
    # Test with positive values
    a = 2
    b = 3
    expected_perimeter = (a + b) * 2
    calculated_perimeter = perimeter(a, b)
    assert calculated_perimeter == expected_perimeter, f"Error: Expected perimeter = {expected_perimeter}, Calculated perimeter = {calculated_perimeter}"

    # Test with zero values
    a = 0
    b = 0
    expected_perimeter = 0
    calculated_perimeter = perimeter(a, b)
    assert calculated_perimeter == expected_perimeter, f"Error: Expected perimeter = {expected_perimeter}, Calculated perimeter = {calculated_perimeter}"

    # Test with negative values
    a = -3
    b = -4
    expected_perimeter = (a + b) * 2
    calculated_perimeter = perimeter(a, b)
    assert calculated_perimeter == expected_perimeter, f"Error: Expected perimeter = {expected_perimeter}, Calculated perimeter = {calculated_perimeter}"

# Run the tests
test_area()
test_perimeter()