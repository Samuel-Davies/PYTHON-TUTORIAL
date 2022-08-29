
counter = 1

while counter <= 10:
    print(counter)
    counter+=1



for i in 'Programming':
    print(f' {i}\t', end='')

print('')

total = 0
grade_counter = 0
grades =[98, 23,56,86,76,87,97,77,65,67]


for grade in grades:
    total = total + grade
    grade_counter +=1

average = total / grade_counter

print(f'the average of the students is {average}')