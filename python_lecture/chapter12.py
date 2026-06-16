"""
ADVANCED PYTHON FEATURES
Topics Covered
1. Type Definitions (Type Hints)
2. Advanced Type Hints
3. Match Case (Python 3.10+)
4. Dictionary Merge & Update Operators
5. Multiple Context Managers
6. Exception Handling
7. Raising Exceptions
8. Try with Else Clause
"""

# ============================================================
# 1. TYPE DEFINITIONS (TYPE HINTS)
# ============================================================

# Type hints help describe what type of data a variable should hold.
# They improve readability and help tools detect errors.

# Variable type hint
age: int = 25

# Function with type hints
def greeting(name: str) -> str:
    return f"Hello, {name}!"

print(greeting("Alice"))


# ============================================================
# 2. ADVANCED TYPE HINTS
# ============================================================

# Python provides advanced typing through the typing module.

from typing import List, Tuple, Dict, Union

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]

# Tuple containing string and integer
person: Tuple[str, int] = ("Alice", 30)

# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}

# Union allows multiple possible types
identifier: Union[int, str] = "ID123"
identifier = 12345

print("Numbers:", numbers)
print("Person:", person)
print("Scores:", scores)
print("Identifier:", identifier)


# ============================================================
# 3. MATCH CASE (Python 3.10+)
# ============================================================

# Similar to switch statements in other languages

def http_status(status: int) -> str:
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"

print(http_status(200))
print(http_status(404))
print(http_status(500))
print(http_status(403))


# ============================================================
# 4. DICTIONARY MERGE & UPDATE OPERATORS
# ============================================================

# Python allows merging dictionaries using | operator

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

merged = dict1 | dict2

print("Merged dictionary:", merged)

# Updating dictionary using |=

dict1 |= dict2

print("Updated dict1:", dict1)


# ============================================================
# 5. MULTIPLE CONTEXT MANAGERS
# ============================================================

# Python allows multiple files to be opened in a single with statement

with (
    open("file1.txt", "w") as f1,
    open("file2.txt", "w") as f2
):
    f1.write("Hello from file1")
    f2.write("Hello from file2")

print("Files written successfully")


# ============================================================
# 6. EXCEPTION HANDLING
# ============================================================

# Exceptions occur when errors happen during program execution.
# try-except prevents the program from crashing.

try:
    x = 10 / 0
except Exception as e:
    print("Error occurred:", e)


# Catching specific exceptions

try:
    number = int("abc")
except ValueError:
    print("ValueError: Cannot convert string to integer")
except TypeError:
    print("TypeError occurred")
except:
    print("Some other error occurred")


# ============================================================
# 7. RAISING EXCEPTIONS
# ============================================================

# We can manually raise exceptions using the raise keyword

def check_age(age: int):
    if age < 18:
        raise ValueError("Age must be at least 18")
    return "Access granted"

try:
    print(check_age(15))
except ValueError as e:
    print("Custom Exception:", e)


# ============================================================
# 8. TRY WITH ELSE CLAUSE
# ============================================================

# The else block runs only if no exception occurs

try:
    num = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful:", num)

