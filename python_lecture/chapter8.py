# FUNCTIONS & RECURSIONS

"""
A function is a group of statements performing a specific task.
When a program gets bigger in size and its complexity grows, it gets difficult for a
program to keep track on which piece of code is doing what!
"""
# Defining a function
def greet():
    print("Hello, welcome to the Python lecture!")  

# Calling a function
greet()

"""
TYPES OF FUNCTIONS IN PYTHON
There are two types of functions in python:
• Built in functions (Already present in python)
• User defined functions (Defined by the user)
Examples of built in functions includes len(), print(), range() etc
"""
#FUNCTIONS WITH ARGUMENTS
def add(a, b):
    return a + b
result = add(5, 3)
print("The sum is:", result)

#FUNCTIONS WITH DEFAULT ARGUMENTS
def greet_user(name="Guest"):
    print("Hello,", name)
greet_user()  # Uses default argument
greet_user("Alice")  # Uses provided argument

# RECURSION
"""
Recursion is a programming technique where a function calls itself in order to solve a problem.
It is commonly used for problems that can be broken down into smaller, similar subproblems.
"""
# Example of a recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1: # Base case
        return 1
    else:
        return n * factorial(n - 1) # Recursive case
print("Factorial of 5 is:", factorial(5)) # Output: 120



