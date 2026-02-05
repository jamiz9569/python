# numpy
"""
---

## 🤔 Why NumPy? (The Real Story)

Look, Python lists are slow. Really slow. Why? Because a Python list is like **keeping separate boxes inside a big container**:

```
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
```

**Real Talk:**
- Python List = City bus 🚌 (stops at every item separately)
- NumPy Array = Bullet Train 🚄 (everything in a line, zoom!)

---

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

