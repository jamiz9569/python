# strings problem
#question 1
name = input("enter your name : ")
print ("good afternoon,{name}") # incorrect way
print ("good afternoon " + name ) # correct way

# qustion 2 
name = input("enter your name : ")
date = input ("enter date : ")
letter = ( "dear " + name + "\n" + " you are selected !" + "\n" + date )
print (letter)


# question 3

name = input("enter your name : ")
#print(name.isspace())
print("  " in name )

# question 4
text = input("enter a string: ")
print(text.replace("  ", " "))


# question 5
letter = "dear jamiz ,\n this python course is nice . \n thanks "
print (letter)