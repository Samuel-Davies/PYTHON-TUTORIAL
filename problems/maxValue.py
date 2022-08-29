
num1 = int(input('enter num1$'))
num2 = int(input('enter num3$'))
num3 = int(input('enter num3$'))

max = num1

if num2 > max:
    max = num2
if num3 > max:
    max = num3

print(f' the maximum number is ${max}')