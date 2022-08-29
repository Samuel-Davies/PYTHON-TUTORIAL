

class Student:
    def __init__(self,name, rollno) -> None:
        self.name = name
        self.rollno = rollno
    
    def show(self):
        print(self.name, self.rollno)

    class Laptop:
        def __init__(self) -> None:
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8


s1 = Student('davies', 23)
s2 = Student('solace', 43)

print(s1.name)

s1.show()