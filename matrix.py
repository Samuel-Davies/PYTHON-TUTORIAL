from numpy import *
# multi dimentional arrays

# arr1 = array([
#                 [1,24,34,7,8,9],
#                 [13,3,6,34,62,81]
#             ])

# # print(arr1.ndim)  
# # print(arr1.shape)
# arr2 = arr1.flatten() # helps change a multi dimentional array into a single one

# print(arr2)

# #from single dimentional to multi dimentional

# arr3 = arr2.reshape(3,4)

# print(arr3)

# operations on matrices

m1 = matrix('1 2 3 ; 6, 4  5 ; 1 6, 7')
m2 = matrix('1 2 3 ; 6, 8  5 ; 2 6, 5')


# print(diagonal(m1))
# print(m2.max())

m3 = m2 + m2


print(m3)