import numpy as np

# Task: Extension #1

# arr1 = np.arr
# n = 1
# arr2 = np.arr([n, n + 1, n + 3])
# np.tile(arr2, 3)

# Task: Extsion #2

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8, 9]

for i in a:
    for j in b:
        if j == i:
            b.remove(j)
print("Task: Extesion #2")
print(a)
print(b)

#Task: Exteion #3

combinedArr = a + b
index7 = combinedArr[7]
index3 = combinedArr[3]

print("Task: Extesion #3")
print("Sum of index at 3 and 7:", index7 + index3)


