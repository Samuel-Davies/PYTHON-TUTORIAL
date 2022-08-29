def person(name, **data):
    print(name)
    
    # we employ the for loop to print the key value pair
    for i , j in data.items():
        print(i, j)



person('davies', city = 'accra', age = 22, mob = 7483943)