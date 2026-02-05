# list and tuple 

# question 1
fruits = []

for i in range(7):
    fruit = input("Enter fruit name: ")
    fruits.append(fruit)

print(fruits)

"""my approach 
list =input("Enter a list of comma-separated values: ")
print(list)

"""


#question 2
 # same approach as question 1
marks = (input("Enter your marks: "))
print (marks)

# question 3
tuple = input("Enter a tuple of comma-separated values: ")
print(tuple)
tuple[2]= "10" # tuples are immutable, this will raise an error
print(tuple)

# question 4
sum =int(input("enter the no.s :    "))
sum1= sum[0] + sum[1] + sum[2] + sum[3]
print (sum1)

# question 5
tuple =(7,0,8,0,0,9)
count =tuple.count (0)
print (count)