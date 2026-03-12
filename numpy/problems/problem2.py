
import numpy as np
import random



"""
1. Array Creation

Create a NumPy array containing numbers from 1 to 20.
"""
arr = np.arange(1, 21)
print(arr)

"""
2. Range and Step

Create an array from 10 to 100 with step 5.

"""
arr = np.arange(10, 101, 5)
print(arr)

"""
3. Reshaping

Create an array from 1–16 and reshape it into a 4×4 matrix.
"""
arr= np.arange(1,17)
x = arr.reshape(4,4)
print(x)
"""
4. Random Data

Generate a 5×5 matrix of random integers between 1 and 50.
"""
arr=np.random.randint(1, 51, (5,5))
print(arr)

"""
5. Array Properties
For a given matrix find:
shape
size
number of dimensions
"""
print(arr.shape)
print(arr.size)
print(arr.ndim)  # ndim tell about dimention of matrix
"""
6. Indexing
From a 5×5 matrix, extract:
second row
third column
"""
print(arr[1])
print(arr[:,2])

"""
7. Slicing

From the same 5×5 matrix extract the center 3×3 submatrix.

"""
print(arr[1:4, 1:4])

"""

8. Boolean Masking

Create an array from 1–30 and extract all even numbers.
"""
arr = np.arange(1,31)
even = arr[arr % 2 == 0]
print(even)
"""

9. Conditional Replacement

Replace all values greater than 15 with 0 in an array.

"""
arr[arr>15]=0
print(arr)


"""

10. Mathematical Operations

Create two arrays and perform:

element-wise addition

element-wise multiplication

"""
x = np.array([1,2,3])
y = np.array([4,5,6])
print("addition : ",x+y)
print("multiplication : ",x*y)


"""

11. Statistics

Given an array calculate:

mean

standard deviation

maximum value

"""

print("mean : ",np.mean(x))
print("std : ",np.std(x))
print("max : ",np.max(x))


"""

12. Broadcasting

Add 10 to every element of a NumPy array using broadcasting.
"""
z= np.array([10])
print("broadcasting : " ,x+z)

"""

13. Dot Product

Compute the dot product of two vectors.
"""
print("dot product: " ,np.dot(x,y))

"""

14. Normalization

Normalize an array using Min-Max scaling

Formula:

(x - min) / (max - min)

"""
normalized = (arr - arr.min()) / (arr.max() - arr.min())

print(normalized)

"""
15. Matrix Operations

Create two 3×3 matrices and perform matrix multiplication.

"""
x= np.matrix([[1,2,3],
            [4,5,6],
            [7,8,9]])
y =np.matrix([[9,8,7],
             [6,5,4],
             [3,2,1]])

print("matrix multiply : " , x*y)

