#dictionary and sets 
#dictionaries are used to store key value pairs
"""
PROPERTIES OF PYTHON DICTIONARIES
1. It is unordered.
2. It is mutable.
3. It is indexed.
4. Cannot contain duplicate keys

"""
fruits ={"apple": "red", "banana": "yellow", "cherry": "red"}
print(fruits)

#accessing values
print(fruits["apple"]) # access value by key
print(fruits.get("banana")) # access value by key using get()

#adding items
fruits["orange"] = "orange" # add item
print(fruits)
fruits.update({"grape": "purple"}) # add item using update()
print(fruits)
#removing items
del fruits["banana"] # remove item by key
print(fruits)
fruits.pop("cherry") # remove item by key using pop()
print(fruits)
fruits.popitem() # remove last inserted item
print(fruits)

#keys, values, items
print(fruits.keys()) # get all keys
print(fruits.values()) # get all values
print(fruits.items()) # get all key-value pairs
#looping through dictionary
for key, value in fruits.items():
    print(f"{key}: {value}")

#sets are unordered collection of unique items
"""
Set is a collection of non-repetitive elements.

PROPERTIES OF SETS
1. Sets are unordered => Element’s order doesn’t matter
2. Sets are unindexed => Cannot access elements by index
3. There is no way to change items in sets.
4. Sets cannot contain duplicate values.

"""
myset = {"apple", "banana", "cherry"}
print(myset)
myset.add("orange") # add item
print(myset)
myset.update(["grape", "melon"]) # add multiple items
print(myset)
myset.remove("banana") # remove item
print(myset)
myset.discard("kiwi") # remove item if exists
print(myset)
myset.pop() # remove arbitrary item
print(myset)
print(len(myset)) # length of set
#looping through set
for item in myset:
    print(item)
#set operations
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "cherry", "date", "fig"}
print(set1.union(set2)) # union
print(set1.intersection(set2)) # intersection
print(set1.difference(set2)) # difference
print(set1.symmetric_difference(set2)) # symmetric difference
print(set1.issubset(set2)) # subset
print(set1.issuperset(set2)) # superset
print(set1.isdisjoint(set2)) # disjoint check

#converting list to set and vice versa
list1 = ["apple", "banana", "cherry", "apple"]
set_from_list = set(list1) # list to set
print(set_from_list)
list_from_set = list(myset) # set to list
print(list_from_set)
#nested set
nested_set = {frozenset({"apple", "banana"}), frozenset({"cherry", "date"})}
print(nested_set)
#frozen set - immutable set
frozen = frozenset(["apple", "banana", "cherry"])
print(frozen)

