import pandas as pd

num_series = pd.Series([1, 2, 3, 4])
print("num_series", type(num_series))
print(num_series)

str_series = pd.Series(['a', 'cbf', 'e'])
print("\nstr_series", type(str_series))
print(str_series)

date_series = pd.date_range(start='11-10-2016', end='22-10-2016')
print(type(date_series))
print(date_series)

# creating Series with custom index
custom_index_series = pd.Series([1, 2, 3], index=['a', 'b', 'cd'])
print("\n custom index series")
print(custom_index_series)
