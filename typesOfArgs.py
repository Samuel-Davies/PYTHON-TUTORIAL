def person(name,age = 20): # defualt actual args, used when you don't want to pass some args but you can also overide it too
    print(name)
    print(age)


person('navin',20)  # position actual args, values are passed as they were defined

person(age = 20, name = 'davies') # keyword actual args; valuaes can be put in any order



# variable length argument concept below
# used when you want to pass more arguments, just want to make your function dynamic, yeah

def sum(*b):
    c = 0

    for i in b:
        c = c + i
    print(c)

sum(5, 4,5,3,6)