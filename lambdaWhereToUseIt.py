from functools import reduce
nums = [4, 2, 3, 4, 6, 7, 12]
# filter function 
evens  = list(filter(lambda n : n % 2 == 0 ,nums))
# using map function
doubles = list(map(lambda n : n *2,evens))

# reduce funtion
sum = reduce(lambda a, b : a + b,doubles)
print(evens)

print(doubles)

print(sum)