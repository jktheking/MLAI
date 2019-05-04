import numpy as np

# use help method to get the manual
# help(np.ones)

# creating  a 5X3 arrays all filled with 1's
print('5X3 arrays all filled with 1s')
print(np.ones((5, 3)))

# creating a 5X3 arrays all filled with 1s of data type int
print('\n5X3 arrays all filled with 1s of data type int')
print(np.ones((5, 3), dtype=np.int))


# creating a 4X2 arrays with random values between 0 and 1
# help(np.random.random)
print(np.random.random((4, 2)))
# just getting the random value between 0 to 1, no need to specify dimensions
print('\njust getting the random value between 0 to 1, no need to specify dimensions')
print(np.random.random())


# arange and linspace(linearly spaced vectors), are numpy variant of range.
# arange, when using non-integer step such as 0.1, the results will often be inconsistent,
# it is better to use linspace
print('array or vector between [18,100) with end exclusive with step of 5 using arange')
print(np.arange(18, 100, 5))

print('\narray or vector between [18,20] both range inclusive of size 12 using linspace')
print(np.linspace(18, 20, 12))


# np.full, creates 4X3 vector filled with 7 as value
print('\n np.full, creates 4X3 vector filled with 7 as value')
print(np.full((4, 3), 7))

# np.random.randint, creates 4X3 vector filled with random values between [1,50)
# low being inclusive and high being exclusive
# help(np.random.randint)
print(' np.random.randint, creates 4X3 vector filled with random values between [1,50)\n')
print(np.random.randint(1, 50, (4, 3)))

# np.tile()
# help(np.eye)




