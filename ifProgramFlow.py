greeting = 'Hello'

name = input('please enter yoour name')

age = int(input('{0} please enter your age, {1}'.format(greeting, name)))

print(age)

if age < 18:
    print('you can\'t vote')