# Scope
a = 10

def something():
    a = 15
    x = globals()['a'] #getting a a specific global variables
    print(a)

    globals()['a'] = 11 # changing the global variables

something()

print(a)