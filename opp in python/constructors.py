# constructors
class Computer:
    def __init__(self):
        self.name = 'Davies'
        self.age = 22
        
    def update(self):
        self.age = 30
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
             return False



c1 = Computer() # the RHS refers to the Constructors
c2 = Computer()
c1.age = 33

if c1.compare(c2):
    print('they are the same')
else:
    print('they\'re different')


c1.update()
print(c1.name)
