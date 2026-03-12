# file inpur and output
"""
The random-access memory is volatile, and all its contents are lost once a program
terminates. In order to persist the data forever, we use files.

A file is data stored in a storage device. A python program can talk to the file by reading
content from it and writing content to it

There are 2 types of files:
1. Text files (.txt, .c, etc)
2. Binary files (.jpg, .dat, etc)
Python has a lot of functions for reading, updating, and deleting files.

"""
# open("filename", "mode of opening(read mode by default)")
open("this.txt", "r")  # open file in read mode
open("this.txt", "w")  # open file in write mode
open("this.txt", "a")  # open file in append mode
open("this.txt", "r+")  # open file in read and write mode

# reading from a file
f = open("this.txt", "r")
data = f.read()  # read the whole file
print(data) # print the content of the file


f.readline()  # read one line from the file
f.readlines()  # read all lines and return as a list of strings
f.close()  # close the file after use
"""
MODES OF OPENING A FILE
r – open for reading
w - open for writing
a - open for appending
+ - open for updating.
‘rb’ will open for read in binary mode.
‘rt’ will open for read in text mode.
"""
# writing to a file
f = open("this.txt", "w")
f.write("Hello, World!\n")  # write to the file
f.write("This is a new line.\n")
f.close()  # close the file after use


#The best way to open and close the file automatically is the with statement

# Open the file in read mode using 'with', which automatically closes the file 
with open("this.txt", "r") as f:   

# Read the contents of the file
 text = f.read()

# Print the contents
print(text)
# No need to explicitly close the file, it's done automatically

# Append mode example
with open("this.txt", "a") as f:
    f.write("Appending a new line.\n")  
    f.write("Another appended line.\n")
# File is automatically closed after the with block

# Read the updated file content
with open("this.txt", "r") as f:
    updated_text = f.read()
    print(updated_text)
# No need to explicitly close the file, it's done automatically

# Binary file example
# Writing binary data to a file
with open("image.dat", "wb") as f:
    f.write(b'\x89PNG\r\n\x1a\n')  # Writing PNG file signature
# File is automatically closed after the with block
# Reading binary data from a file
with open("image.dat", "rb") as f:
    binary_data = f.read()
    print(binary_data)
# No need to explicitly close the file, it's done automatically

# File handling exceptions
try:
    with open("this.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("The file does not exist.")
    print("File opened successfully.")
    print(text)
    print("File content:")
    print(updated_text)
    print("Binary file content:")
    print(binary_data)
    print("Please check the file name and try again.")
    print(content)
    print("File opened successfully.")
except IOError:
    print("An error occurred while reading the file.")
    print("Please check the file name and try again.")
    print("The file does not exist.")

#these re very importnt to handle files 
