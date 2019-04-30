import numpy as np

input_list = [[1, 2, 3], [2, 3, 4],[4, 2, 6]]

list_1 = input_list[0]
list_2 = input_list[1]
list_3 = input_list[2]

import numpy as np
array_1 = np.array([list_1,list_2,list_3])
eigen = np.linalg.eig(array_1)
inv = np.linalg.inv(array_1)
det = np.linalg.det(array_1)
print(eigen)
print(inv)
print(det)