import resource


a = 5 
b = 2
 
try:
    print('resource Open')
    print(a / b)
    k = int(input("please enter a number"))
    print(k)
    
except ZeroDivisionError as e:
    print("here you can\'t divide a number by zero", e)

except ValueError as e:
    print('Invalid Input')

except Exception as e:
    print('Something went wrong')
finally:
    print('resource Closed')



print('bye')