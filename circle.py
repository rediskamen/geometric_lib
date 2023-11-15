import math


def area(r):
    return math.pi * r * r


def perimeter(r):
    return 2 * math.pi * r


import unittest
import math

class TestCircleFunctions(unittest.TestCase):
    def test_area(self):
        # Тест 1: проверяем правильность вычисления площади для положительного радиуса
        self.assertAlmostEqual(area(2), math.pi * 2 * 2)
        # Тест 2: проверяем правильность вычисления площади для нулевого радиуса
        self.assertAlmostEqual(area(0), 0)
        # Тест 3: проверяем правильность вычисления площади для отрицательного радиуса
        self.assertAlmostEqual(area(-3), math.pi * 3 * 3)

    def test_perimeter(self):
        # Тест 4: проверяем правильность вычисления периметра для положительного радиуса
        self.assertAlmostEqual(perimeter(2), 2 * math.pi * 2)
        # Тест 5: проверяем правильность вычисления периметра для нулевого радиуса
        self.assertAlmostEqual(perimeter(0), 0)
        # Тест 6: проверяем правильность вычисления периметра для отрицательного радиуса
        self.assertAlmostEqual(perimeter(3), 2 * math.pi * 3)

        # Тест 7: проверяем правильность вычисления площади для очень большого числа
        self.assertAlmostEqual(area(1e100), math.pi * (1e100) * (1e100))

        # Тест 8: проверяем вызов исключения для некорректного ввода
        with self.assertRaises(TypeError):
            perimeter("radius")
        with self.assertRaises(TypeError):
            perimeter(None)

if __name__ == '__main__':
    unittest.main()
import math

def test_area():
    # Тест для положительного радиуса
    r = 2
    expected_area = math.pi * r * r
    calculated_area = area(r)
    assert calculated_area == expected_area, f"Ошибка: Ожидаемая площадь = {expected_area}, Рассчитанная площадь = {calculated_area}"

    # Тест для нулевого радиуса
    r = 0
    expected_area = 0
    calculated_area = area(r)
    assert calculated_area == expected_area, f"Ошибка: Ожидаемая площадь = {expected_area}, Рассчитанная площадь = {calculated_area}"

    # Тест для отрицательного радиуса
    r = -3
    expected_area = math.pi * r * r
    calculated_area = area(r)
    assert calculated_area == expected_area, f"Ошибка: Ожидаемая площадь = {expected_area}, Рассчитанная площадь = {calculated_area}"

def test_perimeter():
    # Тест для положительного радиуса
    r = 2
    expected_perimeter = 2 * math.pi * r
    calculated_perimeter = perimeter(r)
    assert calculated_perimeter == expected_perimeter, f"Ошибка: Ожидаемый периметр = {expected_perimeter}, Рассчитанный периметр = {calculated_perimeter}"

    # Тест для нулевого радиуса
    r = 0
    expected_perimeter = 0
    calculated_perimeter = perimeter(r)
    assert calculated_perimeter == expected_perimeter, f"Ошибка: Ожидаемый периметр = {expected_perimeter}, Рассчитанный периметр = {calculated_perimeter}"

    # Тест для отрицательного радиуса
    r = -3
    expected_perimeter = 2 * math.pi * r
    calculated_perimeter = perimeter(r)
    assert calculated_perimeter == expected_perimeter, f"Ошибка: Ожидаемый периметр = {expected_perimeter}, Рассчитанный периметр = {calculated_perimeter}"

# Запуск тестов
test_area()
test_perimeter()