import unittest
from src.calculator import sum, subtract, multiply, divide

class CalculatorTests(unittest.TestCase):
    def test_sum(self):
        assert sum(2,3) == 5
    
    def test_subtract(self):
        assert subtract(10,5) == 5
    
    def test_multiply(self):
        assert multiply(3,2) == 6
    
    def test_divide(self):
        result = divide(10,2)
        excepted = 5
        assert result == excepted
    
    def test_divide_with_cero(self):
        self.assertRaises(ValueError, divide, 10, 0)