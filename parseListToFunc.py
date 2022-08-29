#  parsing a list to a function in python 


def count(lst):
    even = 0 
    odd = 0

    for i in lst:
        if(i % 2 ==0):
            even +=1
        else:
            odd+=1
    
    return even, odd


lst = [12,3,9,5,46,45,3,2,34,64, 56,77]
even, odd = count(lst)

# printing the ouput in two different sintax
print('Even : {0} and odd : {1}'.format(even, odd))

print(f'Even : {even} and odd : {odd}')