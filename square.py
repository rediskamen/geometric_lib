
def area(a):
    return a * a


def perimeter(a):
    return 4 * a

import unittest

class TestSquareFunctions(unittest.TestCase):
    def test_area(self):
        # Тест 1: проверяем правильность вычисления площади для положительной стороны
        self.assertAlmostEqual(area(2), 2 * 2)
        # Тест 2: проверяем правильность вычисления площади для нулевой стороны
        self.assertAlmostEqual(area(0), 0)
        # Тест 3: проверяем правильность вычисления площади для отрицательной стороны
        self.assertAlmostEqual(area(-3), 3 * 3)

    def test_perimeter(self):
        # Тест 4: проверяем правильность вычисления периметра для положительной стороны
        self.assertAlmostEqual(perimeter(2), 4 * 2)
        # Тест 5: проверяем правильность вычисления периметра для нулевой стороны
        self.assertAlmostEqual(perimeter(0), 0)
        # Тест 6: проверяем правильность вычисления периметра для отрицательной стороны
        self.assertAlmostEqual(perimeter(3), 4 * 3)

        # Тест 7: проверяем правильность вычисления площади для очень большого числа
        self.assertAlmostEqual(area(1e100), (1e100) * (1e100))

        # Тест 8: проверяем вызов исключения для некорректного ввода
        with self.assertRaises(TypeError):
            perimeter("side", 3)
        with self.assertRaises(TypeError):
            perimeter(None, 4)

if __name__ == '__main__':
    unittest.main()

def test_area():
    # Test with positive value
    a = 2
    expected_area = a * a
    calculated_area = area(a)
    assert calculated_area == expected_area, f"Error: Expected area = {expected_area}, Calculated area = {calculated_area}"

    # Test with zero value
    a = 0
    expected_area = 0
    calculated_area = area(a)
    assert calculated_area == expected_area, f"Error: Expected area = {expected_area}, Calculated area = {calculated_area}"

    # Test with negative value
    a = -3
    expected_area = a * a
    calculated_area = area(a)
    assert calculated_area == expected_area, f"Error: Expected area = {expected_area}, Calculated area = {calculated_area}"

def test_perimeter():
    # Test with positive value
    a = 2
    expected_perimeter = 4 * a
    calculated_perimeter = perimeter(a)
    assert calculated_perimeter == expected_perimeter, f"Error: Expected perimeter = {expected_perimeter}, Calculated perimeter = {calculated_perimeter}"

    # Test with zero value
    a = 0
    expected_perimeter = 0
    calculated_perimeter = perimeter(a)
    assert calculated_perimeter == expected_perimeter, f"Error: Expected perimeter = {expected_perimeter}, Calculated perimeter = {calculated_perimeter}"

    # Test with negative value
    a = -3
    expected_perimeter = 4 * a
    calculated_perimeter = perimeter(a)
    assert calculated_perimeter == expected_perimeter, f"Error: Expected perimeter = {expected_perimeter}, Calculated perimeter = {calculated_perimeter}"

# Run the tests
test_area()
test_perimeter()