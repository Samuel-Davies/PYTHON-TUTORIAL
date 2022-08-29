number = 18


for i in range(2,number):
    if(number % i ==0):
        print('not prime')
        break
else:
    print('prime')