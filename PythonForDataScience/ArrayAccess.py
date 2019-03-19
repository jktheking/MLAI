# Subset, Slice, Index and Iterate through Numpy array

import numpy as np

array_1d = np.arange(10)
print(array_1d)

# accessing array value at index 2
print(type(array_1d[2]))
print(array_1d[2])

# accessing array value at index 2, 9 , 3 in a list: note here indexes should be given in list
print(type(array_1d[[2, 9, 3]]))
print(array_1d[[2, 9, 3]])