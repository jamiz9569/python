import numpy as np 
 # question 1 
def solve(dimensions, value):
    return np.full(dimensions, value)

print (solve((2,3), 5)) # [[5 5 5]
                         # [5 5 5]]

#question2
arr=input("Enter the array elements separated by space: ")
arr = np.array(arr.split(), dtype=int) # convert input to numpy array of integers
np.sum(arr)
print(f"The sum of the array elements is: {np.sum(arr)}")

#question3

def top_left_sub_matrix (matrix, rows, cols):
    return matrix[:rows, :cols]
matrix = input("Enter the matrix elements row-wise, separated by space: ")
matrix = np.array(matrix.split(), dtype=int).reshape(-1, 4) # reshape to 2D array with 4 columns
rows = int(input("Enter the number of rows for the sub-matrix: "))
cols = int(input("Enter the number of columns for the sub-matrix: "))
sub_matrix = top_left_sub_matrix(matrix, rows, cols)
print("Top-left sub-matrix:")
print(sub_matrix)


#question4
def bottom_right_sub_matrix (matrix, rows, cols):
    return matrix[-rows:, -cols:]
matrix = input("Enter the matrix elements row-wise, separated by space: ")
matrix = np.array(matrix.split(), dtype=int).reshape(-1, 4) # reshape to 2D array with 4 columns
rows = int(input("Enter the number of rows for the sub-matrix: "))
cols = int(input("Enter the number of columns for the sub-matrix: "))
sub_matrix = bottom_right_sub_matrix(matrix, rows, cols)
print("Bottom-right sub-matrix:")
print(sub_matrix)


#question5
arr=input("Enter the array elements separated by space: ")
arr = np.array(arr.split(), dtype=int) # convert input to numpy array of integers
x= np.mean(arr) # calculate mean
print(f"The mean of the array elements is: {x}")
y= np.std(arr) # calculate standard deviation
print(f"The standard deviation of the array elements is: {y}")

