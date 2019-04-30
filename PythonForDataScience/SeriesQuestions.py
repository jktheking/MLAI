import pandas as pd


# Create a series using list = [6,7,8,9,2,3,4,5] and print the output series as the square of each number in the list.
# Hint: If input series = 1,2,3 the output series should be 1,4,9
# Hint: First create the series and then using apply and lambda find the output series.

input_series = pd.Series([6, 7, 8, 9, 2, 3, 4, 5])
print('\n input series')
print(input_series)
square_series = input_series.apply(lambda x : x**2)
print('\n square_series')
print(square_series)

#help(pd.Series)


# Manual Indexing
# Description
# Create a panda series that contains the first ‘n’ natural numbers and their respective squares.
# The first ‘n’ numbers should appear in the index position.
# Hint: Use manual indexing.
#
# Format:
# Input: A natural number 'n'
# Output: A pandas series with the first 'n' natural numbers in the index position and their respective
# squares in the adjacent column.
#
# Example:
# Input 1:
# 4
# Output 1:
# 1  1
# 2  4
# 3  9
# 4  16

n = 8
dictionary = {num: num**2 for num in range(1, n+1)}
print('\n dictionary series')
print(pd.Series(dictionary))
