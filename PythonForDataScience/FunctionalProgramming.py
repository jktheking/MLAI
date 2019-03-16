# Using the Map function, create a list 'cube', which consists of the cube of numbers in input_list.
# For e.g. if the input list is [5,6,4,8,9], the output should be [125, 216, 64, 512, 729]

input_list = [5, 6, 4, 8, 9]
cube = list(map(lambda x: x ** 3, input_list))
print(cube)


# Using the function Map, count the number of words that start with ‘S’ in input_list.
input_list_S = ['San Jose', 'San Francisco', 'Santa Fe', 'Houston']

# First method is to convert the lambda into list and then count the occurrence of 1,
count = list(map(lambda x: 1 if x[0].upper() == 'S' else 0, input_list_S)).count(1)
sum = sum(map(lambda x: 1 if x[0].upper() == 'S' else 0, input_list_S))
print("sum is ",sum)

# Join the two iterables pairwise first one is list of first name and second one is tuple of last name.
print('-----executing the iterable mapper to map firstName list and lastName tuple----')
first_name_list = ["jk", "saurabh", "surya"]
last_name_tuple = ('king', 'pawar', 'gopasana Kanth')

name_mapper_lambda = lambda lElement, tElement : lElement[0].upper()+lElement[1:]+' '+tElement[0].upper()+tElement[1:]
full_name_list = list(map(name_mapper_lambda, first_name_list, last_name_tuple))
print(full_name_list)


# filter
num_list_to_filter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
multipleOf5 = list(filter(lambda x: x % 5 == 0, num_list_to_filter))
print('multipleOf5:', multipleOf5)

# You are given a list of strings such as input_list =  ['hdjk', 'salsap', 'sherpa'].
# Extract a list of names that start with an ‘s’ and end with a ‘p’ (both 's' and 'p' are lowercase) in input_list.
str_list_to_filter = ['hdjk', 'salsap', 'sherpa']
startWithSandEndWithP = list(filter(lambda x: x[0] == 's' and x[-1] == 'p', str_list_to_filter))
print("filtered list startWithSandEndWithP ", startWithSandEndWithP)

# understanding Reduce
print('-----understanding reduce----')
print("how range works: range(1,5), it excludes the end range value, if stride is not defined then defaults to 1",[i for i in range(1,5)])
print(type(range(1,5)))
from functools import reduce
aggregatedValue = reduce(lambda x,y : x+y, range(1,5))
print("summation of iterable :",aggregatedValue)

listOfNums = (10, 34, 78, 35, 54, 98, 1, 23, 45)
largestValue = reduce(lambda x, y: x if x > y else y, listOfNums)
print("largestValue is:", largestValue)


# Using the Reduce function, concatenate a list of words in input_list, and print the output as a string.
# If input_list = ['I','Love','Python'], the output should be the string 'I Love Python'.

i_love_python_list = ['I','Love','Python']
i_love_python_str = reduce(lambda first, sec: first+' '+sec, i_love_python_list)
print("reduced to i_love_python_str:", i_love_python_str)