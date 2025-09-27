import sys
import os

from string_calculator import StringCalculator


def main():
    calc = StringCalculator()
    
    print("String Calculator Examples")
    
    test_cases = [
        ("", "Empty string"),
        ("1", "Single number"),
        ("1,5", "Two comma-separated numbers"),
        ("1,2,3,4", "Multiple comma-separated numbers"),
        ("1\n2,3", "Mixed newlines and commas"),
        ("1\n2\n3", "Only newlines"),
        ("//;\n1;2", "Custom delimiter (semicolon)"),
        ("//|\n3|4|5", "Custom delimiter (pipe)"),
        ("//***\n1***2***3", "Multi-character with custom delimiter"),
    ]
    
    for input_str, description in test_cases:
        try:
            result = calc.add(input_str)
            print(f"PASS: {description:35} | Input: {repr(input_str):15} → {result}")
        except Exception as e:
            print(f"FAIL: {description:35} | Input: {repr(input_str):15} → Error: {e}")
    
    print("\n" + "=" * 40)
    print("Error Cases:")
    
    error_cases = [
        ("-1", "Single negative number"),
        ("2,-4,3,-5", "Multiple negative numbers"),
        ("//;\n1;-2;3", "Negative with custom delimiter"),
    ]
    
    for input_str, description in error_cases:
        try:
            result = calc.add(input_str)
            print(f"FAIL: {description:35} | Input: {repr(input_str):15} → {result} (Should have failed!)")
        except ValueError as e:
            print(f"PASS: {description:35} | Input: {repr(input_str):15} → {e}")
        except Exception as e:
            print(f"ERROR: {description:35} | Input: {repr(input_str):15} → Unexpected error: {e}")


if __name__ == "__main__":
    main()