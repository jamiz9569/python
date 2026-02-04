#dictionaries and sets

#question 1
words ={"angoor" : "grapes", "saeb" : "apple", "kela" : "banana"}
#print(words)   this is not a look u option 
print(words.get(word, "Word not found"))

# question 2
number =set()
for i in range(8):
    number.add(int(input("enter the number : ")))
    print(number)

# question 3
num = {"18": '18'} # wrong approach 
n = {10,"18"} # correct approach
print(n)

#question 4
s = set()
s.add(20)
s.add(20.0)
s.add('20')
s.length =len(s)
print(s.length)

#question 5
s = {}
print(type(s))

#question 6
friend={}
for i in range(3):
    key = input("enter the key : ")
    value = input("enter the value : ")
    friend[key] = value
print(friend)


#question 7
"""
If two friends have the same name
Answer:
The second entry overwrites the first one.
Why:
Dictionary keys must be unique. No error. Silent replacement.

"""
# question8
"""
If two friends have the same language
Answer:
Nothing happens. Completely allowed.
Why:
Dictionary values can repeat. Only keys must be unique.

"""

