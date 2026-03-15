import pandas as pd 
import numpy as np 


#series object in pandas 
"""
series object is a one-dimensional array-like object containing an array of data 
and an associated array of data labels, called its index.
The labels need not be unique but must be a hashable type. 
The object supports both integer- and label-based indexing
and provides a host of methods for performing operations involving the index.
Conceptually, it is like a fixed-size dict in that you can get and set values by index label.
It also supports many of the common array operations performed on numpy arrays, such as element-wise addition 
and multiplication, but with the addition of being able to align data based on the index labels.
"""
labels = ['a','b','c']

my_list =[10,20,30]
arr = np.array([10,20,30])
my_dict ={1:10,2:20,3:30}

series1= pd.Series(my_list)
print(series1)
type(series1)

series1= pd.Series(data=my_list,index=labels)
print(series1)

series2= pd.Series(arr,labels)
print(series2)
series3= pd.Series(my_dict)
print(series3)


# dataframe object in pandas
"""
A DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.
You can think of it like a spreadsheet or SQL table, or a dict of Series objects.
It is generally the most commonly used pandas object for data manipulation and analysis.
"""

