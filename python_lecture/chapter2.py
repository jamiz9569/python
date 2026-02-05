# variables and datatype in python

a = 1 # int 
b = 2.5 # floating point number 
c = "hello" # string
d = True # boolean
e = None # NoneType 
f = "53.6" # string type but contains numeric value

"""
arithmatic operator = + , - , * , / , % , // , **= power 
comparison operator = (== , != , > , < , >= , <=) # return boolean value
logical operator = and , or , not 
assignment operator = = , += , -= , *= , /=
bitwise operator = & , | , ^ , ~ , << , >> , >>=
membership operator = in , not in
identity operator = is , is not

"""

# use type() function
t = type(a) # to check datatype of variable
print(t)
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

f = float(f) # type casting string to float
print(type(f))

# input function
name = input("Enter your name: ") # by default input function takes input as string
age = int(input("Enter your age: ")) # type casting input to int
print("Hello " + name + ", you are " + str(age) + " years old.")
print(f"Hello {name}, you are {age} years old.") # f-string for formatted output






    