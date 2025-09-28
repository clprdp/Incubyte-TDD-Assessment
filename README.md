# Incubyte TDD Assessment - String Calculator Kata


## Test Coverage

The test suite covers:
- Empty string handling
- Single number input
- Two numbers with commas
- Multiple numbers with commas  
- Newline delimiters
- Custom delimiters (single and multi-character)
- Negative number validation (single and multiple)
- Numbers > 1000 filtering
- Multiple delimiters support
- Multiple long delimiters support

All tests pass: **10/10** part of the Incubyte assessment process.

## Overview

This project implements a String Calculator that can:
- Handle empty strings
- Add single and multiple numbers
- Support comma-separated values
- Support newline delimiters
- Support custom delimiters
- Validate against negative numbers

## Features Added

### 1. Basic Addition
- Empty string returns 0
- Single number returns itself
- Two comma-separated numbers return their sum

### 2. Multiple Numbers
- Handles any amount of comma-separated numbers

### 3. Newline Delimiters
- Supports newlines (`\n`) as delimiters alongside commas
- Example: `"1\n2,3"` returns `6`

### 4. Custom Delimiters
- Supports custom delimiters with format: `"//[delimiter]\n[numbers...]"`
- Examples:
  - `"//;\n1;2"` returns `3`
  - `"//|\n3|4|5"` returns `12`
  - `"//***\n1***2***3"` returns `6`

### 5. Negative Number Validation
- Throws `ValueError` for negative numbers
- Shows all negative numbers in error message
- Example: `"2,-4,3,-5"` throws `"negative numbers not allowed -4, -5"`

### 6. Numbers > 1000 Filtering
- Numbers bigger than 1000 are ignored in the sum
- Examples:
  - `"2,1001"` returns `2` (1001 is ignored)
  - `"1000,1001,2"` returns `1002` (only 1000 + 2)

### 7. Multiple Delimiters
- Supports multiple delimiters using format: `"//[delim1][delim2]...\n[numbers...]"`
- Examples:
  - `"//[*][%]\n1*2%3"` returns `6`
  - `"//[;][|]\n4;5|6"` returns `15`
  - `"//[a][b][c]\n1a2b3c4"` returns `10`

### 8. Multiple Long Delimiters
- Supports multiple multi-character delimiters
- Examples:
  - `"//[***][%%%]\n1***2%%%3"` returns `6`
  - `"//[abc][def]\n4abc5def6"` returns `15`

## Project structure

```
├── src/
│   ├── __init__.py
│   └── string_calculator.py    # Actual implementation
├── tests/
│   ├── __init__.py
│   └── test_string_calculator.py    # Test suite
├── README.md
└── LICENSE
```

## Running Tests

### Prerequisites
- Python 3.6+
- pytest (install with `pip install pytest`)

### Run All Tests
```bash
python -m pytest tests/test_string_calculator.py -v
```

### Run Specific Test
```bash
python -m pytest tests/test_string_calculator.py::TestStringCalculator::test_empty_string_returns_zero -v
```

## Usage Examples

```python
from src.string_calculator import StringCalculator

calc = StringCalculator()

# Basic usage
calc.add("")          # Returns 0
calc.add("1")         # Returns 1
calc.add("1,5")       # Returns 6

# Multiple numbers
calc.add("1,2,3,4")   # Returns 10

# Newlines as delimiters
calc.add("1\n2,3")    # Returns 6

# Custom delimiters
calc.add("//;\n1;2")  # Returns 3

# Numbers > 1000 ignored
calc.add("2,1001")    # Returns 2 (1001 ignored)

# Multiple delimiters
calc.add("//[*][%]\n1*2%3")      # Returns 6
calc.add("//[***][%%%]\n1***2%%%3")  # Returns 6

# Error handling
calc.add("-1")        # Raises ValueError: "negative numbers not allowed -1"
```

## Test Coverage

The test suite covers:
- Empty string handling
- Single number input
- Two numbers with commas
- Multiple numbers with commas  
- Newline delimiters
- Custom delimiters (single and multi-character)
- Negative number validation (single and multiple)

All tests pass: **7/7**
