import numpy as np

a = np.array([0, 1, 2])

print(np.tile(a, (3, 2, 2)))

b = np. array([[[1, 2], [3, 4]]])
print('\n b')
print(b)
print(np.tile(b, 2))

help(np.tile)


# print("b's shape", b.shape)
# print("b's dimension", b.ndim)
#
# c = np.array([[1, 2], [3, 4]])
# print("c's shape", c.shape)
# print("c's dimension", c.ndim)


