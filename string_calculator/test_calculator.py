import pytest
from calculator import StringCalculator

# Create a shared instance for reuse in all tests
@pytest.fixture
def calc():
    return StringCalculator()

def test_empty_string_returns_zero(calc):
    # Empty input should return 0
    assert calc.add("") == 0

def test_single_number(calc):
    # A single number should return itself
    assert calc.add("1") == 1

def test_two_numbers(calc):
    # Two numbers separated by comma should return their sum
    assert calc.add("1,2") == 3

def test_multiple_numbers(calc):
    # Multiple numbers should be summed correctly
    assert calc.add("1,2,3,4") == 10

def test_newline_as_delimiter(calc):
    # Newline can act as a valid delimiter along with comma
    assert calc.add("1\n2,3") == 6

def test_custom_single_char_delimiter(calc):
    # Custom delimiter can be defined using //<delimiter>\n
    assert calc.add("//;\n1;2") == 3

def test_negative_numbers_throw_exception(calc):
    # If any negative numbers are present, raise ValueError
    with pytest.raises(ValueError, match="negatives not allowed:"):
        calc.add("1,-2,3,-4")

def test_ignore_numbers_bigger_than_1000(calc):
    # Numbers > 1000 should be ignored in the sum
    assert calc.add("2,1001") == 2

def test_delimiter_of_any_length(calc):
    # Delimiters of any length can be used when declared in square brackets
    assert calc.add("//[***]\n1***2***3") == 6

def test_multiple_single_char_delimiters(calc):
    # Multiple single-character delimiters can be used together
    assert calc.add("//[*][%]\n1*2%3") == 6

def test_multiple_long_delimiters(calc):
    # Multiple multi-character delimiters are also supported
    assert calc.add("//[**][%%]\n1**2%%3") == 6
