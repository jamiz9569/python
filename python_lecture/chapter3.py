# strings 
# srings are immutable

name ="jamiz qamar"
print(name)
print(name.title())
print(name.upper()) 
print(name.lower())

nameshort = name[0:6] # slicing 
namelong = name[1:5:2] # slicing with step
print(namelong)
print(nameshort)

# concatenation
first_name = "jamiz"
last_name = "qamar"
full_name = first_name + " is " + last_name
print(full_name)


print(name.endswith("r")) # check if string ends with r
print(name.startswith("j")) # check if string starts with j
print(name.find("q")) # find index of character q
print(name.replace("jamiz", "john")) # replace jamiz with john
print(name.split(" ")) # split string by space
print(",".join(["jamiz", "qamar"])) # join list of strings with comma
print(len(name)) # length of string
print(name.count("a")) # count occurrences of a
print(name.index("q")) # index of character q
print(name.isalpha()) # check if all characters are alphabetic
print(name.isdigit()) # check if all characters are digits
print(name.isspace()) # check if all characters are whitespace
print(name.strip()) # remove leading and trailing whitespace
print(name.rstrip()) # remove trailing whitespace
print(name.lstrip()) # remove leading whitespace
print(name.capitalize()) # capitalize first character
print(name.swapcase()) # swap case of characters
print(name.center(20)) # center string with padding
print(name.zfill(20)) # pad string with zeros on the left
print(name.encode()) # encode string to bytes
print(name.format()) # format string (no placeholders here)
print(name.partition(" ")) # partition string at first space
print(name.rpartition(" ")) # partition string at last space
print(name.splitlines()) # split string at line breaks
print(name.translate(str.maketrans("jamiz", "johns"))) # translate characters
print(name.casefold()) # case insensitive comparison
print(name.removeprefix("jamiz")) # remove prefix
print(name.removesuffix("qamar")) # remove suffix
print(name.islower()) # check if all characters are lowercase
print(name.isupper()) # check if all characters are uppercase


name = "   jamiz\n qamar   " # string with whitespace
print (name)

name = "   jamiz \" qamar\"  " # string with escape character
print (name)