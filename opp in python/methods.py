# methods are for the behaviour
# tyoes of methods, instance method, class methods, static methods


class Student:
    school = 'GTUC'
    def __init__(self, m1, m2,m3) -> None:
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        # the below function is an instances method
        # because we're parsing self 
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3
    # @classmothod is decorator
    @classmethod
    def getSchool(cls):
        return cls.school

    # Static class 
    @staticmethod
    def info():
        print('this is Student class... in abc molude')




s1 = Student(23,46,85)
s2 = Student(12,452,4)

a1 = s1.avg()
a2 = s2.avg()
print(a1)
print(a2)


print(Student.getSchool())


