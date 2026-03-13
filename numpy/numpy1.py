# numpy


"""
---

## 🤔 Why NumPy?

Look, Python lists are slow. Really slow. Why?
Because a Python list is like **keeping separate boxes inside a big container**:

Python List (Slow 🐌):
┌─────────────────────────────────────────────────┐
│  📦 → points to → [1]                           │
│  📦 → points to → [2]                           │
│  📦 → points to → [3]                           │
│  (Each box must be searched separately!)        │
└─────────────────────────────────────────────────┘

NumPy Array (Fast 🚀):
┌─────────────────────────────────────────────────┐
│  [1][2][3][4][5] ← All in one line, direct!     │
│  (Continuous memory, no searching!)             │
└─────────────────────────────────────────────────┘


- Python List = City bus 🚌 (stops at every item separately)
- NumPy Array = Bullet Train 🚄 (everything in a line, zoom!)

"""
import numpy as np

#1d array
a =np.array([1,2,3])
print(a)

#2d array
b = np.array([[4,5,6],[7,8,9]])
print(b)

#initialize xXy array with zeros
c = np.zeros((2,3))
print(c)

#initialize xXy array with ones
d = np.ones((3,2)) 
print(d)

#arranging numbers between a range
e = np.arange(10,20,2)
print(e)

#linear spacing between two numbers
f = np.linspace(1,10,5)
print(f)

#identity matrix
g = np.eye(3) 
print(g)

#filling same numbers between array of dimention in x X y
h = np.full((2,3),7)
print(h)

#random numbers between 0 and 1
i = np.random((2,2))
print(i)

### 📊 Data Types (`dtype`) - The Array's DNA

# In NumPy, every array has a **dtype** - meaning all elements must be the same type:


# Integer array
int_arr = np.array([1, 2, 3])
print(f"Integer Array: {int_arr}, dtype: {int_arr.dtype}")

# Float array
float_arr = np.array([1.5, 2.5, 3.5])
print(f"Float Array: {float_arr}, dtype: {float_arr.dtype}")

# Mixed? NumPy will "promote" to the bigger type!
mixed = np.array([1, 2, 3.5])  # int + float = everything becomes float!
print(f"Mixed Array: {mixed}, dtype: {mixed.dtype}")

# Force a specific dtype
forced = np.array([1, 2, 3], dtype=np.float32)
print(f"Forced Float32: {forced}, dtype: {forced.dtype}")

"""
**Output:**
```
Integer Array: [1 2 3], dtype: int64
Float Array: [1.5 2.5 3.5], dtype: float64
Mixed Array: [1.  2.  3.5], dtype: float64    ← See? All became floats!
Forced Float32: [1. 2. 3.], dtype: float32
```
"""

#2d array with different data type
j = np.array([[1,2,3],[4,5,6]], dtype=np.float64)
print(j)

#3d array with different data type
k = np.array([[[1,2],[3,4]],[[5,6],[7,8]]], dtype=np.int32)
print(k)

#array with string data type
l = np.array(['apple', 'banana', 'cherry'], dtype=np.str_)
print(l) 

#array with boolean data type
m = np.array([True, False, True], dtype=np.bool_) 
print(m)

#array with complex data type
n = np.array([1+2j, 3+4j], dtype=np.complex128) 
print(n)

# mathematical function in array 
o = np.array([1, 2, 3])

print(np.sin(o))  # sine of each element
print(np.cos(o))  # cosine of each element
print(np.exp(o))  # exponential of each element
print(np.sqrt(o)) # square root of each element
print(np.sum(o)) # sum of all elements
print(np.subtract(o, 1)) # subtract 1 from each element
print(np.multiply(o, 2)) # multiply each element by 2
print(np.divide(o, 2)) # divide each element by 2

p = np.array([[1, 2], [3, 4]])
print(np.sum(p, axis=0))  # sum along columns (result: [4, 6] )
print(np.sum(p, axis=1))  # sum along rows (result: [3, 7] )
