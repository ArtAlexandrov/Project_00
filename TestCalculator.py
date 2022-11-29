import unittest
from Calculator import Calculator
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
    def test_add(self):
        self.assertEqual(self.calculator.add(7, 3),10)
    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(7,3), 21)
    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(7,3), 4)
    def test_divide(self):
        self.assertEqual(self.calculator.divide(82,16), 5.125)
    def test_pow(self):
        self.assertEqual(self.calculator.pow(3,3), 27)
    def test_common(self):
        self.assertEqual(self.calculator.common(16), 4)
if __name__ == "__main__":
    unittest.main()