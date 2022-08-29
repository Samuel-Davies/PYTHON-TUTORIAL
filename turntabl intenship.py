from numpy import *
n1 = int(input("enter the size of arr1: "))
n2 = int(input("enter the size of arr2: "))

arr1 = list(map(int,input("Enter the elements of the array1: ").split()))
arr2 = list(map(int,input("Enter the elements of the array2: ").split()))

arr = arr1 + arr2

arr.sort(reverse=True)
print(*arr) 