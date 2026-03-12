# file input and output 
#question1
with open("poem.txt" , "r+") as f:
      data =f.read()

if "twinkle" in data :
      print("word found")
else:
      print ("not found")

#question2

"""
Understand that game() must return an integer score, not True or False.
Run the game and store the returned score in a variable.
Open Hi-score.txt in read mode first.
Handle two cases:
File is blank
File does not exist
Convert the file content to an integer hi score.
Compare current score with stored hi score.
Only if the current score is higher:
Open the file in write mode
Write the new score
Otherwise do nothing.
"""
import random
def game():
     win_count = 0
     for i in range(5):
         computer = random.randint(1, 9)
         you = int(input("Enter a number between 1 and 9: "))
         if you >= computer:
             print("You win")
             win_count += 1
         else:
             print("You lose")
     return win_count
win_count = game()
score = game()
print("Your score:", score)
try:
    with open("Hi-score.txt", "r") as f:
        content = f.read()
        if content == "":
            hi_score = 0
        else:
            hi_score = int(content)
except FileNotFoundError:
    hi_score = 0
if score > hi_score:
    with open("Hi-score.txt", "w") as f:
        f.write(str(score))
    print("New Hi-score!")
else:
    print("Hi-score remains:", hi_score)

#question3
with open("table.txt" , "w") as f:

 for i in range(2,21):
    f.write("\n")
    for j in range(1,11):
      f.write(f"{i} x {j} = {i*j}\n")

#question4

with open("foul.txt","r") as f :
    content =f.read()
concent=content.replace("donkey","##########")
with open("foul.txt","r") as f :
    f.write(content)

#question5
file_path = "file.txt"
censor_words = ["Donkey", "stupid", "ugly"]

with open(file_path, "r") as f:
    content = f.read()

for word in censor_words:
    content = content.replace(word, "#####")

with open(file_path, "w") as f:
    f.write(content)

#question6
file_path = "log.txt"

with open(file_path, "r") as f:
    for line_num, line in enumerate(f, 1):
        if "python" in line.lower():
            print(f"'python' found at line {line_num}")

#question 
import shutil

source = "this.txt"
destination = "this_copy.txt"

shutil.copy(source, destination)
print("File copied successfully")

#question9
import filecmp

file1 = "file1.txt"
file2 = "file2.txt"

if filecmp.cmp(file1, file2):
    print("Files are identical")
else:
    print("Files are different")

#question10
file_path = "file.txt"

open(file_path, "w").close()  # opens file in write mode and closes immediately
print("File content wiped out")

#question11
import os

old_name = "file.txt"
new_name = "renamed_by_python.txt"

os.rename(old_name, new_name)
print(f"File renamed to {new_name}")

