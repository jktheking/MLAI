# Stacking of Numpy aray

import numpy as np

# for vertical stacking dimension of columns including there numbers must be same
array_1 = np.arange(20).reshape(5, 4)
array_2 = np.arange(12).reshape(3, 4)

print(array_1)
print('\n')
print(array_2)
print('vertical stacking:')

vstacked_array = np.vstack((array_1, array_2))
print("type of vstacked_array is {}".format(type(vstacked_array)))
print(vstacked_array)



print('\nhorizontal stacking candidate arrays:')
array_1h = np.arange(20).reshape(5, 4)
array_2h = np.arange(15).reshape(5, 3)
print(array_1h)
print('\n')
print(array_2h)

print('horizontal stacking:')

hstacked_array = np.hstack((array_1h, array_2h))
print("type of hstacked_array is {}".format(type(hstacked_array)))
print(hstacked_array)