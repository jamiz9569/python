#conditional staement

#question 1
a= int (input("Enter first number: "))
b= int (input("Enter second number: "))
c = int (input("Enter third number: "))
d = int (input("Enter fourth number: "))
if a>b and a>c and a>d:
    print("The greatest number is:", a)
elif b>a and b>c and b>d:
    print("The greatest number is:", b)
elif c>a and c>b and c>d:
    print("The greatest number is:", c)
else:
    print("The greatest number is:", d)


"""
Question 1: Greatest of four numbers

This works only if all numbers are different. If two numbers are equal and greatest, your logic collapses and quietly lies.

Better version, simpler and correct:

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d = int(input("Enter fourth number: "))

print("The greatest number is:", max(a, b, c, d))

"""

#question 2
sub1 = int (input("Enter marks of subject 1: "))
sub2 = int (input("Enter marks of subject 2: "))
sub3 = int (input("Enter marks of subject 3: "))
total = sub1 + sub2 + sub3 
percentage = total / 3
if percentage>=40 and sub1>=33 and sub2>=33 and sub3>=33:
    print("You have passed the exam")
else:
    print("You have failed the exam")

#question 3
text1 ="Make a lot of money"
text2 ="buy now"
text3 ="subscribe this"
text4 ="click this"
if (text1 or text2 or text3 or text4) in input("enter the comment : "):
    print("This is a spam ")
else:
    print ("this is not a spam ")

    """
    Better version:
    comment = input("Enter the comment: ").lower()

if ("make a lot of money" in comment or
    "buy now" in comment or
    "subscribe this" in comment or
    "click this" in comment):
    print("This is a spam")
else:
    print("This is not a spam")

    """

#question 4
username = input("Enter your username: ")
if len(username)<10:
    print("Username is valid")
else:
    print("Username is invalid")

#question 5
list =[]
for i in range (5):
    num = int (input("Enter a number: "))
    list.append(num)
name =input("Enter a name to search: ")
if  name in list:
    print("name is present in the list")
else:
    print("name is not present in the list")

#question 6
english = int (input("Enter marks of English: "))
maths = int (input("Enter marks of Maths: "))
science = int (input("Enter marks of Science: "))
hindi = int (input("Enter marks of Hindi: "))
social_science = int (input("Enter marks of Social Science: "))
total_marks = english + maths + science + hindi + social_science
percentage = (total_marks / 500) * 100
if percentage>90 and percentage<=100:
    print("Grade ex")
elif percentage>80 and percentage<=90:
    print("Grade A")
elif percentage>70 and percentage<=80:
    print("Grade B")
elif percentage>60 and percentage<=70:
    print("Grade C")
elif percentage>50 and percentage<=60:
    print("Grade D")
else :
    print("Grade F")

#question 7
post = input("Enter the name of the post: ").lower()
if post == "harry":
    print ("yes")
else:
    print("no")



