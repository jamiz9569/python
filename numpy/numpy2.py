import numpy as np 


#array comparison 
a= [1,2,4]
b = [2,4,4]
c= [1,2,4]
np.array_equal(a,b) # element wise comparison
print(np.array_equal(a,b)) #false
np.array_equal(a,b) #false  #whole array comparison
print(np.array_equal(a,c)) #true
np.array_equal(a,c) #true   
print(np.array_equal(a,c)) #true




#aggregate functions
a=np.sum(a) #7
b=np.min(a) #1
c=np.max(a) #4
d=np.mean(a) #2.3333333333333335
e=np.median(a) #2.0
f=np.std(a) #1.247219128924647

print(f"Sum: {a}, Min: {b}, Max: {c}, Mean: {d}, Median: {e}, Std Dev: {f}")


#concept of broadcasting 
x = np.array([1,2,3])
y = np.array([4,5,6])
z = x + y # element wise addition
print(z) # [5 7 9]

# array manipulation 
arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape) # (2,3)
print(arr.reshape(3,2)) # reshape to 3 rows and 2 columns
print(arr.flatten()) # flatten to 1d array
print(arr.T) # transpose of the array
np.concatenate((arr, arr), axis=0) # concatenate along rows
print(np.concatenate((arr, arr), axis=0)) # [[1 2 3]
                                            #  [4 5 6]
                                            #  [1 2 3]
                                            #  [4 5 6]]


np.vstack((arr, arr)) # stack along rows
print(np.vstack((arr, arr))) # [[1 2 3]
                                            #  [4 5 6]
                                            #  [1 2 3]
                                            #  [4 5 6]]


np.hstack((arr, arr)) # stack along columns
print(np.hstack((arr, arr))) # [[1 2 3 1 2 3]
                                            #  [4 5 6 4 5 6]]

np.split(arr, 2) # split into 2 arrays along rows
print(np.split(arr, 2)) # [array([[1, 2, 3]]), array([[4, 5, 6]])]

np.split(arr, 3, axis=1) # split into 3 arrays along columns
print(np.split(arr, 3, axis=1)) # [array([[1], [4]]), array([[2], [5]]), array([[3], [6]])]




#indexing and slicing 
arr = np.array([[1,2,3],[4,5,6]])
print(arr[0,0]) #1
print(arr[1,2]) #6
print(arr[0,:]) #[1 2 3]
print(arr[:,1]) #[2 5]
print(arr[0:2,0:2]) # [[1 2]
                    #  [4 5]]
print(arr[::2,::2]) # [[1 3]]

