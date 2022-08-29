from numpy import *

# arr1 = array([1, 4, 45, 5, 3])
# arr2 = array([12,45,53,74,6])

# arr3 = concatenate([arr1, arr2])
# print(arr3)

# print(sort(arr1))


#copying an array

arr1 = array([12,4,36,37])

arr2 = arr1.view()  # for shallow copy
arr2 = arr1.copy() # for deep copy; meaning the arrays are not linked with each other


print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))