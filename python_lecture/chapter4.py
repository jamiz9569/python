# list AND TUPLES

# list are mutable 
fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.append("orange") # add item to end
print(fruits)
fruits.insert(1, "kiwi") # add item at index 1
print(fruits)
fruits.remove("banana") # remove item by value
print(fruits)
fruits.pop() # remove last item
print(fruits)
fruits.sort() # sort list
print(fruits)
fruits.reverse() # reverse list
print(fruits)
print(fruits[0]) # access first item
print(fruits[1:3]) # slicing
print(len(fruits)) # length of list


# tuples are immutable

colors = ("red", "green", "blue")
print(colors)
print(colors[0]) # access first item
print(colors[1:3]) # slicing
print(len(colors)) # length of tuple


# converting list to tuple and vice versa
fruits_tuple = tuple(fruits) # list to tuple
print(fruits_tuple)
colors_list = list(colors) # tuple to list
print(colors_list)

# nested list
nested_list = [["apple", "banana"], ["cherry", "date"]]
print(nested_list)

# nested tuple
nested_tuple = (("red", "green"), ("blue", "yellow"))
print(nested_tuple)

# mixed list
mixed_list = ["apple", 1, 2.5, True, ["nested", "list"]]
print(mixed_list)

# mixed tuple
mixed_tuple = ("red", 1, 2.5, False, ("nested", "tuple"))
print(mixed_tuple)

# unpacking list
a, b, c = fruits
print(a)
print(b)
print(c)
# unpacking tuple
x, y, z = colors    
print(x)
print(y)
print(z)

# looping through list
for fruit in fruits:
    print(fruit)

# looping through tuple
for color in colors:
    print(color)

# list comprehension
squared_numbers = [x**2 for x in range(10)]
print(squared_numbers)
# tuple comprehension (actually creates a generator)
squared_numbers_tuple = tuple(x**2 for x in range(10))
print(squared_numbers_tuple)
# checking membership
print("apple" in fruits)
print("red" in colors)
print("banana" not in fruits)
print("blue" not in colors)
# copying list
fruits_copy = fruits.copy()
print(fruits_copy)
# copying tuple (tuples are immutable, so this is just a reference)
colors_copy = colors
print(colors_copy)

# clearing list
fruits.clear()
print(fruits)
# tuples cannot be cleared as they are immutable
# del keyword to delete list or tuple
del fruits_copy
del colors_copy
# print(fruits_copy) # this will raise an error
# print(colors_copy) # this will raise an error

