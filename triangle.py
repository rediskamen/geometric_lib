def area(a, h):
    return a * h / 2

def perimeter(a, b, c):
    return a + b + c

import unittest

class TestTriangleFunctions(unittest.TestCase):
    def test_area(self):
        # Тест 1: проверяем правильность вычисления площади для положительных чисел
        self.assertAlmostEqual(area(3, 4), 6)
        # Тест 2: проверяем правильность вычисления площади для нулевых значений
        self.assertAlmostEqual(area(0, 7), 0)
        # Тест 3: проверяем правильность вычисления площади для отрицательных чисел
        self.assertAlmostEqual(area(-2, 5), -5)

    def test_perimeter(self):
        # Тест 4: проверяем правильность вычисления периметра для положительных чисел
        self.assertAlmostEqual(perimeter(3, 4, 5), 12)
        # Тест 5: проверяем правильность вычисления периметра для нулевых значений
        self.assertAlmostEqual(perimeter(0, 7, 9), 16)
        # Тест 6: проверяем правильность вычисления периметра для отрицательных чисел
        self.assertAlmostEqual(perimeter(-2, 5, 8), 11)

        # Тест 7: проверяем правильность вычисления периметра для очень большого числа
        self.assertAlmostEqual(perimeter(1e100, 2, 3), 1e100 + 2 + 3)

        # Тест 8: проверяем вызов исключения для некорректного ввода
        with self.assertRaises(TypeError):
            perimeter("a", 5, 6)
        with self.assertRaises(TypeError):
            perimeter(3, None, 6)

if __name__ == '__main__':
    unittest.main()

def test_area():
    # Test with positive values
    a = 2
    h = 3
    expected_area = a * h / 2
    calculated_area = area(a, h)
    assert calculated_area == expected_area, f"Error: Expected area = {expected_area}, Calculated area = {calculated_area}"

    # Test with zero values
    a = 0
    h = 0
    expected_area = 0
    calculated_area = area(a, h)
    assert calculated_area == expected_area, f"Error: Expected area = {expected_area}, Calculated area = {calculated_area}"

    # Test with negative values
    a = -3
    h = -4
    expected_area = a * h / 2
    calculated_area = area(a, h)
    assert calculated_area == expected_area, f"Error: Expected area = {expected_area}, Calculated area = {calculated_area}"


def test_perimeter():
    # Test with positive values
    a = 2
    b = 3
    c = 4
    expected_perimeter = a + b + c
    calculated_perimeter = perimeter(a, b, c)
    assert calculated_perimeter == expected_perimeter, f"Error: Expected perimeter = {expected_perimeter}, Calculated perimeter = {calculated_perimeter}"

    # Test with zero values
    a = 0
    b = 0
    c = 0
    expected_perimeter = 0
    calculated_perimeter = perimeter(a, b, c)
    assert calculated_perimeter == expected_perimeter, f"Error: Expected perimeter = {expected_perimeter}, Calculated perimeter = {calculated_perimeter}"

    # Test with negative values
    a = -3
    b = -4
    c = -5
    expected_perimeter = a + b + c
    calculated_perimeter = perimeter(a, b, c)
    assert calculated_perimeter == expected_perimeter, f"Error: Expected perimeter = {expected_perimeter}, Calculated perimeter = {calculated_perimeter}"


# Run the tests
test_area()
test_perimeter()