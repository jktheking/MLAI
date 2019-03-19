import numpy as np

array_1d = np.arange(24)
print("1d array generated using arange:", array_1d)

print("\nreshaping the 1d array to 3 dimension")
# total multiplication of dimensions should be equal to 24, here 2X3X4 means there are two 3X4 array block in outer part
array_3d = array_1d.reshape((2, 3, 4))
print(array_3d)



# Create an 2d array using list list_1 = [10,11,12,13] and list_2 = [15,12,13,14]
# and print the shape and dimension of the array created.
list_1 = [10, 11, 12, 13]
list_2 = [15, 12, 13, 14]

list_array_2d = np.array([list_1, list_2])
print(list_array_2d.shape)
print(list_array_2d.ndim)