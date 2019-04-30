list_access = [1, 5, 8, 19, 23, 45, 89, 90, 76, 56, 89]
print("list access does not contain comma", list_access[1::2])

list_access2 = [[1, 2, 3, 5], [8, 19, 20, 45]]
# how to access normal multi-dimensional list
print("list_access2", list_access2[1][2])


# Accessing multi-dimensional array: typically works how mathematical notation to access multi-dimensional array works
# See file ArrayAccess to access elements of 1d array

import numpy as np

array_2d = np.array([[2, 3, 7, 5], [4, 6, 8, 10], [10, 12, 15, 19]])
print("prints 2nd  element of 3rd sublist ",array_2d[2, 1])
print("\nprints all the element of  2nd sublist, i.e. 2nd row of the vector:", array_2d[1, :])
print("\n prints 3rd column of the vector i.e. 3rd element from each sublist", array_2d[:, 2])


print("\n array_2d[:, :3] prints all the rows for column 0,1,2 excluding the 3:")
print(array_2d[:, :3])



# iterating over 2d array
print("\niterating over 2d array: array_2d")
for row in array_2d:
    print(row)

# iterating over 3d array
array_3d = np.arange(0, 24).reshape((3, 4, 2))
print("\n3d array on np.arange(0, 24).reshape((3, 4, 2))")
print(array_3d)
print("iterating over 3d array, each element would be 2d array")
for row in array_3d:
    print("\n", row)



