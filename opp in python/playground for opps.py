class Student:
    def __init__(self, name, stuID, age):
        self.name = name
        self.stuID = stuID
        self.age = age

        
    def intro(self):
        print('my name is {} and \n my studentID is {} \n i am {} years old'.format(self.name, self.stuID, self.age))


student1 = Student('davies', '040919723', 22)

student1.intro()
