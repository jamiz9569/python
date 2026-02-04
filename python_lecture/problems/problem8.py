#function and recursion 
#qustion 1
def grestes_of_thre(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(grestes_of_thre(5,10,3))  # Output: 10

#question 2
def ctof(celcius):
    farenheit = (celcius * 9/5)+32
    return farenheit
print(ctof(25))  # Output: 77.0

#question 3
#How do you prevent a python print() function to print a new line at the end.
# using end =" "

#question 4
def sum(num):
    if num==0:
        return 0
    return num + sum(num-1)
print(sum(5))  # Output: 15

#question 5
def pattern(num):
    if num==0:
     return 
    else:
        print("*" * num)
        pattern (num-1)
       
pattern(8)

#question 6
def inc_to_cm(inches):
    cm = inches * 2.54
    return cm
print(inc_to_cm(10))  # Output: 25.4

#question 7
l = ["banana", "mango", "banana"]
def rem(lst,word):
    new_list = []
    for item in lst:
        if item.strip() != word: #strip() removes any leading/trailing whitespace
           new_list.append(item.strip())
    return new_list
print(rem(l,"banana"))  

#question 8
def multi(num):
    for i in range (1,11):
        print(num* i)
multi(5)  # Output: Multiplication table of 5