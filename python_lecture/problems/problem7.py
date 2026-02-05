# loops in python

#question 1
num=int(input("Enter a number: "))
for i in range(1,11):
 print(i*num)

# question 2
l = ["Harry", "Soham", "Sachin", "Rahul"]
for name in l:
    if name.startswith("S"):
        print("Hello " + name)
 #   else:
  #      continue       # optional

# question 3
num = int(input("Enter a number: "))
while i<11:
    print(i*num)
    i += 1   # was missing from my solution 

# question 4
"""
num = int(input("Enter a number: "))
for i in range(2, num):
    if num>0 and num==1 or num==2 :
      print("The number is prime")
    elif num >2 and num%i==0:
      print("The number is prime")
    else:
      print("The number is not prime")""
"""
num = int(input("Enter a number: "))
if num <= 1:
    print("Not prime")
else:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print("Prime")
    else:
        print("Not prime")

# question 5
num = int(input("Enter a number: "))
i = 1
sum = 0
while i <= num:    # equall sign was missing from my solution
   sum += i
   i += 1
print("The sum of numbers from 1 to", num, "is", sum)

# question 6
num = int(input("Enter a number: "))
factorial = 1
for i in range(1,num+1):  # +1 was missing from my solution
    factorial = factorial*i
print("The factorial of", num, "is", factorial)

# question 7
"""
for n = 3
    *
   ***
  *****
 """
num = int(input("Enter number of rows: "))
for i in range (num):
    print(" "*(num-i-1) + "*"*(2*i+1))

# question 8
num = int(input("Enter number of rows: "))
for i in range (num ):
    print("*" * (i+1 ))
    
#for i in range (num):        # no need for this loop
 #   print (" " *( num-i+1))#
    

# question 9
num = int(input("Enter number of rows: "))
for i in range (num):
    for j in range (num):
        if i==0 or i==num-1 or j==0 or j==num-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

 # end="" tells Python what to print after the current output instead of a newline.
 # By default, print() adds a newline character at the end of its output.
#  print("*", end="")
#  print("*", end="")
#  print("*")
# This will output: *** on the same line