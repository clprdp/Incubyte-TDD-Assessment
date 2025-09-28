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
    
    def test_negative_numbers_throw_exception(self):
        """Test that negative numbers throw exception with proper message"""
        with self.assertRaises(ValueError) as context:
            self.calculator.add("-1")
        self.assertEqual(str(context.exception), "negative numbers not allowed -1")
        
        with self.assertRaises(ValueError) as context:
            self.calculator.add("2,-4,3,-5")
        self.assertEqual(str(context.exception), "negative numbers not allowed -4, -5")
        
        with self.assertRaises(ValueError) as context:
            self.calculator.add("//;\n1;-2;3")
        self.assertEqual(str(context.exception), "negative numbers not allowed -2")
    
    def test_numbers_bigger_than_1000_ignored(self):
        """Test that numbers bigger than 1000 are ignored in the sum"""
        result = self.calculator.add("2,1001")
        self.assertEqual(result, 2)
        
        result = self.calculator.add("1000,1001,2")
        self.assertEqual(result, 1002)  # 1000 + 2, 1001 ignored
        
        result = self.calculator.add("//;\n2000;1;2000;3")
        self.assertEqual(result, 4)  # Only 1 + 3, both 2000s ignored
    
    def test_multiple_delimiters(self):
        """Test support for multiple delimiters using [delim1][delim2] format"""
        result = self.calculator.add("//[*][%]\n1*2%3")
        self.assertEqual(result, 6)
        
        result = self.calculator.add("//[;][|]\n4;5|6")
        self.assertEqual(result, 15)
        
        result = self.calculator.add("//[a][b][c]\n1a2b3c4")
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()