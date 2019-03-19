import numpy as np

row = 3
col = 4
value = 8
print(np.full((row, col), value, dtype=int))


# Given an even integer ‘n’, create an ‘n*n’
# checkerboard matrix with the values 0 and 1, using the tile function.
# Example:
# Input 1:
# 2
# Output 1:
# [[0 1]
#  [1 0]]
# Input 2:
# 4
# Output 2:
# [[0 1 0 1]
#  [1 0 1 0]
#  [0 1 0 1]
#  [1 0 1 0]]

n = 3
baseArray = np.array([[0, 1], [1, 0]])
print(np.tile(baseArray, (n//2, n//2)))

#help(np.tile)
