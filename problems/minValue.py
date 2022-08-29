# determining the minimum value 

num1 = int(input('enter the first number$'))
num2 = int(input('enter the second number$'))
num3 = int(input('enter the third number$'))

min = num1

if num2 < min:
    min = num2
if num3 < min:
    min = num3

print(f'the minimum value is {min}')