# 🧮 String Calculator TDD Kata

This is a simple **String Calculator** implementation built using **Test-Driven Development (TDD)** in Python. The core function is:

📋 Requirements & Rules
1. Basic Input Handling
The method can take up to two numbers, separated by commas.

It should return their sum.

Examples:

`"" ➝ 0`

`"1" ➝ 1`

`"1,2" ➝ 3`

💡 Start with the simplest test case and build incrementally.

2. Support Unknown Number of Inputs
The method should handle any number of numbers.

Example:
`"1,2,3,4" ➝ 10`

3. Handle Newline as Delimiter
Newlines (\n) should be supported as valid delimiters, in addition to commas.

Example:

`"1\n2,3" ➝ 6`

Invalid Case (No need to handle):

`"1,\n"` ➝ ❌ (malformed)

4. Support Custom Delimiters
A custom delimiter can be defined using the format:

`//[delimiter]\n[numbers...]`
Example:

`"//;\n1;2" ➝ 3`

This line is optional. Existing formats must still work.

5. Negative Numbers Raise Exceptions
If the string contains negative numbers, raise an exception.

The message should include all negative numbers.

Example:

`"1,-2,-3" ➝ raises ValueError("negatives not allowed: -2, -3")`

6. Ignore Numbers Greater Than 1000
Any number greater than 1000 should be ignored.

Examples:

`"2,1001" ➝ 2`

`"1000,1" ➝ 1001`

7. Delimiters of Any Length
Delimiters can be of any length.

Format:

`//[***]\n1***2***3`
Example: `"//[***]\n1***2***3" ➝ 6`

8. Multiple Custom Delimiters
Support multiple delimiters using this format:

`//[*][%]\n1*2%3`

Delimiters can also be longer than one character:

`"//[***][%%]\n1***2%%3" ➝ 6`

✅ How to Run

* Clone the repository.

* (Optional) Create a virtual environment.

Install dependencies:

```pip install pytest```

Run tests:

`pytest`

📁 Project Structure

```
├── calculator.py         # Implementation file
├── test_calculator.py    # Test cases using pytest
└── README.md             # Documentation
```

🛠️ Tech Stack

```
Python 3.10+

Pytest
```

TDD methodology

🧪 TDD Tips

Write the simplest failing test.

* Implement just enough code to make it pass.

* Refactor.

* Repeat.

