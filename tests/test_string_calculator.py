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
    
    def test_single_number_returns_that_number(self):
        """Test that a single number returns itself"""
        result = self.calculator.add("1")
        self.assertEqual(result, 1)
        
        result = self.calculator.add("5")
        self.assertEqual(result, 5)
    
    def test_two_comma_separated_numbers(self):
        """Test that two comma-separated numbers return their sum"""
        result = self.calculator.add("1,5")
        self.assertEqual(result, 6)
        
        result = self.calculator.add("2,3")
        self.assertEqual(result, 5)
    
    def test_multiple_comma_separated_numbers(self):
        """Test that multiple comma-separated numbers return their sum"""
        result = self.calculator.add("1,2,3,4")
        self.assertEqual(result, 10)
        
        result = self.calculator.add("5,10,15,20,25")
        self.assertEqual(result, 75)
    
    def test_newlines_as_delimiters(self):
        """Test that newlines can be used as delimiters"""
        result = self.calculator.add("1\n2,3")
        self.assertEqual(result, 6)
        
        result = self.calculator.add("1\n2\n3")
        self.assertEqual(result, 6)
        
        result = self.calculator.add("4,5\n6")
        self.assertEqual(result, 15)
    
    def test_custom_delimiters(self):
        """Test custom delimiters with format '//[delimiter]\\n[numbers...]'"""
        result = self.calculator.add("//;\n1;2")
        self.assertEqual(result, 3)
        
        result = self.calculator.add("//|\n3|4|5")
        self.assertEqual(result, 12)
        
        result = self.calculator.add("//***\n1***2***3")
        self.assertEqual(result, 6)


if __name__ == '__main__':
    unittest.main()