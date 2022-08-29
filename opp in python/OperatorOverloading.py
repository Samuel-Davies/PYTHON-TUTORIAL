
class Student:
    def __init__(self,m1,m2) -> None:
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m1 + other.m2
        s3 = Student(m1,m2)
        return s3
    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2

        if r1 > r2:
            return True
        else: 
            return False

    #  to override
    def __str__(self):
        return '{} , {}'.format(self.m1, self.m2)


s1 = Student(12,45)
s2 = Student(12,98)


s3  = s1 + s2

# print(s3.m1)


# another example

if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')


print(s2) # prints out the address instead