import numpy as np

# Task #1 : D array of numbers from 0 to 9

array1 = np.array([0,1,2,3,4,5,6,7,8,9])
print("1D array of numbers from 0 to 9")
print(array1)

# Task #2 : 3x3 NumPy array of all Boolean value Trues

sample_arr = [True, True] 
bool_arr = np.random.choice(sample_arr, size=(3, 3))
print("3x3 NumPy array of all Boolean value Trues")
print(bool_arr)

# Task #3 : Extract all odd numbers from array of 1-10

a = np.array([1,2,3,4,5,6,7,8,9,10])
b = a[a % 2 == 1]
print("Extraction of odd numbers from array of 1-10")
print(b)

# Task #4 : Replace all odd numbers in an array of 1-10 with the value-1

a = np.array([1,2,3,4,5,6,7,8,9,10])
a[a % 2 == 1] = -1
print("Replace all odd numbers in an array of 1-10 with the value-1")
print(a)

# Task #5: Convert a 1D array to a 2D array with 2 rows
array = np.array([1,2,3,4,5,6])
newArray = array.reshape(2, 3)
print("Convert a 1D array to a 2D array with 2 rows")
print(newArray)

# Task #6: Create two arrays a and b, stack these two arrays vertically use the np.dot and np.sum to calculate totals

a = np.array([1,2,3])
b = np.array([4,5,6])

c = np.dstack((a, b))
print("Task #6: Stack two arrays")
print(c) 


d = np.dot(a, b)
print("Task #6: np.dot")
print(d)


total_sum = np.sum(d)
print("Task #6: np.sum")
print(total_sum)

