# sample 1 : squared comprehensions
n = 4
squared_list = [num**2 for num in range(1, n+1)]
print(squared_list)

# Extract the words that start with a vowel from a list input_list=[wood, old, apple, big, item, euphoria]
# using list comprehensions.
input_list = ['wood', 'old', 'apple', 'big', 'item', 'euphoria']
vowels = ['a','e','i','o','u']
list_vowel = [word for word in input_list if word[0].lower() in vowels]
print(list_vowel)


# Write a program to generate a dictionary that contains the key-value pairs i: i**2 where ' i ' is an integer number
# from 1 to n (both 1 and n included).

dictionary = {num: num**2 for num in range(1, 8)}
print(dictionary)