import numpy as np

# Convert the input list to a NumPy array
array_2d = np.array([[11, 12, 13, 14],
                    [21, 22, 23, 24],
                    [31, 32, 33, 34]])

# Extract the first column, first row, last column and last row respectively using
# appropriate indexing
col_first = array_2d[:, 0]
print(col_first)
row_first = array_2d[0, :]
print(row_first)
col_last = array_2d[:, array_2d.shape[1] - 1]
print(col_last)
row_last = array_2d[array_2d.shape[0] - 1, :]
print(row_last)