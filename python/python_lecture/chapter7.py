#Loops in Python
# For Loop Example
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# While Loop Example
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

# Nested Loop Example
for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")

# Loop with Break and Continue
for number in range(10):
    if number == 5:
        print("Breaking the loop at number 5")
        break
    if number % 2 == 0:
        print(f"Skipping even number: {number}")
        continue
    print(f"Odd number: {number}")

# Loop with Else
for n in range(3):
    print(f"Number: {n}")
else:
    print("Loop completed without break")

#using range() in loops
for i in range(1, 6):
    print(f"Range number: {i}")

#using enumerate() in loops
colors = ["red", "green", "blue"]
for index, color in enumerate(colors): #enumerate returns both index and value
    print(f"Index: {index}, Color: {color}")

#using zip() in loops
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages): #zip combines two lists
    print(f"Name: {name}, Age: {age}")

# List Comprehension with Loops
squares = [x**2 for x in range(10)]
print("Squares:", squares)
# Dictionary Comprehension with Loops
cubes = {x: x**3 for x in range(5)}
print("Cubes:", cubes)
# Set Comprehension with Loops
unique_squares = {x**2 for x in range(-3, 4)}
print("Unique Squares:", unique_squares)
# Generator Expression with Loops
even_numbers = (x for x in range(10) if x % 2 == 0)
print("Even Numbers:", list(even_numbers))
# Looping through a string
for char in "Hello":
    print(f"Character: {char}")
# Looping through a dictionary
person = {"name": "Alice", "age": 30, "city": "New York"}
for key, value in person.items():
    print(f"{key}: {value}")
# Using else with while loop
count = 0
while count < 3:
    print(f"Count is: {count}")
    count += 1
else:
    print("While loop completed without break")
# Using pass in loops
for i in range(5):
    if i % 2 == 0:
        pass  # Do nothing for even numbers
    else:
        print(f"Odd number: {i}")

# Using nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print("Flattened Matrix:", flattened)

# Using itertools for advanced looping
import itertools
for combination in itertools.combinations(['A', 'B', 'C'], 2):
    print("Combination:", combination)

