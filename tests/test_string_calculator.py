import unittest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from string_calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calculator = StringCalculator()
    
    def test_empty_string_returns_zero(self):
        """Test that an empty string returns 0"""
        result = self.calculator.add("")
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()