# class average program that uses sentiniel control 

# intialization 

total = 0
gradeCounter = 0

# this is where the processing happens

grade = int(input('Enter  grade , press -1 to end: '))

while grade != -1:
    total += grade
    gradeCounter +=1
    grade = int(input('Enter  grade , press -1 to end: '))

# termination the program 

if gradeCounter != 0:
    average = total / gradeCounter
    print(f'the average is : {average:.2f}')
else:
    print('No grade was entered')

