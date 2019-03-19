import numpy as np

array_1d = np.array([1, 2, 3, 4, 589, 76])
print(type(array_1d))
print(array_1d)
print("printing 1d array\n", array_1d)

array_2d = np.array([[1, 2, 3], [6, 7, 9], [11, 12, 13]])
print(type(array_2d))
print(array_2d)
print("printing 2d array\n", array_2d)


array_3d = np.array([[[1, 2, 3], [6, 7, 9]], [[11, 12, 13], [12, 19, 12]]])
print(type(array_3d))
print("printing 3d array\n")
print(array_3d)

# array multiplication, let's first see the multiplication of 2 lists
mul_list1 = [1, 2, 3, 4]
mul_list2 = [4, 3, 2, 1]
mul_list_result = list(map(lambda x, y: x*y, mul_list1, mul_list2))
print("\nmultiplication of list using lambda:", mul_list_result)

# let's see how multiplication for arrays, binary operators in numpy works element-wise.
# Note : To use binary operators on array, size of operand arrays must be  dimension-wise same.

mul_array1 = np.array(mul_list1)
mul_array2 = np.array(mul_list2)
mul_array_result = mul_array1 * mul_array2;
print("\n multiplication of array:", mul_array_result)
