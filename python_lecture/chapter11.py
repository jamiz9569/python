"""
ADVANCED PYTHON NOTES
Topics covered:
1. Modules and Packages
2. Virtual Environments
3. JSON Handling
4. Pathlib (modern file paths)
5. Logging
6. lambda function 
"""

# ============================================================
# 1. MODULES
# ============================================================

# A module is simply a Python file that contains functions,
# variables, or classes that can be reused in other files.

# Example module (save as math_utils.py)

# def add(a, b):
#     return a + b
#
# def multiply(a, b):
#     return a * b


# Example usage in another file (main.py)

# import math_utils
# print(math_utils.add(2,3))
# print(math_utils.multiply(4,5))


# ============================================================
# 2. PACKAGES
# ============================================================

# A package is a folder that contains multiple modules.

"""
Example structure

project/
│
├── main.py
│
└── utils/
    ├── __init__.py
    └── math_utils.py
"""

# Importing from package

# from utils.math_utils import add
# print(add(10,5))


# ============================================================
# 3. VIRTUAL ENVIRONMENTS
# ============================================================

"""
Virtual environments isolate project dependencies.

Create environment:
python -m venv env

Activate (Windows):
env\Scripts\activate

Activate (Linux/Mac):
source env/bin/activate

Install library:
pip install numpy

Save dependencies:
pip freeze > requirements.txt

Install from file:
pip install -r requirements.txt
"""


# ============================================================
# 4. JSON HANDLING
# ============================================================

import json

# JSON is commonly used for APIs and configuration files

data = {
    "name": "Alice",
    "age": 22,
    "skills": ["Python", "Machine Learning"]
}

# Writing JSON to file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# Reading JSON from file
with open("data.json", "r") as file:
    loaded_data = json.load(file)

print("JSON Data:", loaded_data)


# ============================================================
# 5. PATHLIB (Modern Path Handling)
# ============================================================

from pathlib import Path

# Create a Path object
file_path = Path("example.txt")

# Write text to file
file_path.write_text("Hello from pathlib!")

# Read text
content = file_path.read_text()
print("File content:", content)

# Check if file exists
print("File exists:", file_path.exists())

# List files in current directory
print("\nFiles in current directory:")
for file in Path(".").iterdir():
    print(file)


# ============================================================
# 6. LOGGING
# ============================================================

import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Program started")
logging.warning("This is a warning message")
logging.error("This is an error message")

print("\nLogging messages written to app.log")



"""
LAMBDA FUNCTIONS
Function created using an expression using ‘lambda’ keyword.

Syntax:
lambda arguments:expressions
"""
square = lambda x:x*x
square(6) # returns 36
sum = lambda a,b,c:a+b+c

"""

Map applies a function to all the items in an input_list.
Syntax.
map(function, input_list)
# the function can be lambda function



Filter creates a list of items for which the function returns true.
list(filter(function))
# the function can be lambda function


Reduce applies a rolling computation to sequential pair of elements.
from functools import reduce
val=reduce (function, list1)
# the function can be lambda function


"""


"""

import os
import sys

# os module provides operating system dependent functionality
# such as creating files/directories, working with paths,
# and interacting with the file system.

# Current working directory
print("Current directory:", os.getcwd())

# List files and folders in the current directory
print("Files and folders:", os.listdir())

# Create a new directory
os.mkdir("data")

# Rename a file or directory
os.rename("data", "data_backup")

# Check if a file or directory exists
print("data_backup exists:", os.path.exists("data_backup"))

# Join paths correctly (works on Windows, Linux, macOS)
path = os.path.join("data_backup", "file.txt")
print("Joined path:", path)

# Remove a file
# os.remove("example.txt")

# Remove an empty directory
# os.rmdir("data_backup")

"""

import sys

# Python version
print(sys.version)

# Command-line arguments
print(sys.argv)

# Exit the program
sys.exit()

# Platform information
print(sys.platform)

"""
One important note: os.rmdir() only removes empty directories. 
If a directory contains files, it raises an error.
Humans, in their infinite optimism, keep trying it anyway. 
To remove a non-empty directory, you'd typically use the shutil module:

import shutil

shutil.rmtree("data_backup")

This deletes the directory and everything inside it, so use it carefully.

"""

"""
import os
import pandas as pd

# Check current directory
print(os.getcwd())

# Move to another folder
os.chdir(r"C:\Users\Jamiz\Downloads")

# Verify
print(os.getcwd())

# Show files
print(os.listdir())

# Read CSV
df = pd.read_csv("students.csv")

print(df.head())

"""