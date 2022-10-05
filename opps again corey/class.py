
class Employee:
    def __init__(self, firstname, lastname, pay) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        self.email = firstname + '.' + lastname + '@company.com'

    def fullname(self):
        return(f'{self.firstname} {self.lastname}')


emp1 = Employee('samuel', 'davies', 5000)
emp2 = Employee('vivian', 'mensah', 5078)

print(emp1.email)
print(emp2.fullname())
